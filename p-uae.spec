%define Werror_cflags	%nil

%define cdrname		cdrtools
%define cdrmainvers	2.01
%define cdrvers 	%{cdrmainvers}a38
%define wiprel		gitf2fc773b75

# For building with SCSI support

Summary:	A software emulation of the Amiga system
Name:		p-uae
Version:	2.3.3
Release:	1.%{wiprel}.2
License:	GPLv2+
Group:		Emulators
Url:		https://sourceforge.net/projects/uaedev/
Source0:	%{name}-%{version}.%{wiprel}.tar.xz
Source10:	%{name}.rpmlintrc
BuildRequires:	qt4-devel
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(zlib)
Conflicts:	uae
Provides:	uaedev = %{EVRD}

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

%files
%doc docs/*
%{_bindir}/*
%{_libdir}/uae/
%{_datadir}/applications/%{name}.desktop

#----------------------------------------------------------------------------

%prep
%setup -q -n p-uae-%{version}.%{wiprel} 

aclocal -I m4 && automake --foreign --add-missing && autoconf
cd src/tools
aclocal
autoconf

%build
./bootstrap.sh
%configure2_5x \
	--with-sdl \
	--with-sdl-gl \
	--with-sdl-gfx \
	--with-sdl-sound \
	--enable-drvsnd \
	--with-sdl-gui \
	--with-qt \
	--enable-cd32 \
	--enable-gayle \
	--enable-scsi-device \
	--enable-ncr \
	--enable-a2091 \
	--with-caps \
	--enable-amax \
	--disable-jit
make


%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_libdir}/uae/amiga/source
%makeinstall
cp -pR amiga/* %{buildroot}%{_libdir}/uae/amiga/

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=UAE
Comment=Amiga Emulator
Exec=%{_bindir}/uae
Terminal=false
Type=Application
StartupNotify=true
Categories=Game;Emulator;
EOF

