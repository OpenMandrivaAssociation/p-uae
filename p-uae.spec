%define cdrname		cdrtools
%define cdrmainvers	2.01
%define cdrvers 	%{cdrmainvers}a38
%define wiprel		beta

# For building with SCSI support

Summary: A software emulation of the Amiga system
Name: p-uae
Version: 2.3.1
Release: %mkrel 1.%{wiprel}.3
URL: http://sourceforge.net/projects/uaedev/
Source0: %{name}-%{version}.%{wiprel}.tar.bz2
License: GPL
Group: Emulators
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildRequires: X11-devel
BuildRequires: gtk+-devel
BuildRequires: gtk+2-devel
BuildRequires: glib-devel
BuildRequires: SDL-devel
BuildRequires: attr-devel
BuildRequires: GL-devel
BuildRequires: qt4-devel
Conflicts: uae
Obsoletes: uaedev
Provides: uaedev

%description
UAE is a software emulation of the Amiga system hardware, which
enables you to run most available Amiga software.  Since it is a
software emulation, no extra or special hardware is needed.  The Amiga
hardware is emulated accurately, so that Amiga software is tricked
into thinking it is running on the real thing.  Your computer's
display, keyboard, hard disk and mouse assume the roles of their
emulated counterparts.

Note that to fully emulate the Amiga you need the Amiga KickStart ROM
images, which are copyrighted and, of course, not included here.

[This is in an unofficial branch of UAE (the Ubiquitous Amiga Emulator)
with the aim of bringing the features of WinUAE to non-Windows platforms
such as Linux, Mac OS X and BeOS.]

%prep
%setup -q -n p-uae-%{version}.%{wiprel} 

aclocal -I m4 && automake --foreign --add-missing && autoconf
cd src/tools
aclocal
autoconf

%build

./bootstrap.sh
%configure --with-sdl --with-sdl-gl --with-sdl-gfx --with-sdl-sound --enable-drvsnd \
	--with-gtk \
	--enable-cd32 \
	--enable-cd32 \
	--enable-gayle \
	--enable-scsi-device --enable-ncr --enable-a2091 \
	--with-caps --enable-amax
%make


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_prefix}/bin \
	$RPM_BUILD_ROOT%{_libdir}/uae/amiga/source
%makeinstall
cp -pR amiga/* $RPM_BUILD_ROOT/%{_libdir}/uae/amiga/.

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=UAE
Comment=Amiga Emulator
Exec=%{_bindir}/uae
Terminal=false
Type=Application
StartupNotify=true
Categories=GNOME;GTK;Emulator;
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc docs/*
%{_bindir}/*
%{_libdir}/uae
%{_datadir}/applications/mandriva-%{name}.desktop
%doc docs/*


