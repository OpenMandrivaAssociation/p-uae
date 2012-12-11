%define Werror_cflags	%nil
%define cdrname		cdrtools
%define cdrmainvers	2.01
%define cdrvers 	%{cdrmainvers}a38
%define wiprel		gitf2fc773b75

# For building with SCSI support

Summary: A software emulation of the Amiga system
Name: p-uae
Version: 2.3.3
Release: %mkrel 1.%{wiprel}.1.2
URL: http://sourceforge.net/projects/uaedev/
Source0: %{name}-%{version}.%{wiprel}.tar.xz
License: GPL
Group: Emulators
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildRequires: gtk-devel
BuildRequires: SDL-devel
BuildRequires: GL-devel zlib-devel gtk+-devel qt4-devel
BuildRequires: mesaglu-devel
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
%configure2_5x \
	--with-sdl --with-sdl-gl --with-sdl-gfx --with-sdl-sound --enable-drvsnd \
	--with-sdl-gui \
	--with-qt \
	--enable-cd32 \
	--enable-gayle \
	--enable-scsi-device --enable-ncr --enable-a2091 \
	--with-caps --enable-amax --disable-jit
make


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




%changelog
* Mon Jan 16 2012 Zombie Ryushu <ryushu@mandriva.org> 2.3.3-1.gitf2fc773b75.1.1mdv2011.0
+ Revision: 761851
- Use SDL for GUI
- Use SDL for GUI
- Use SDL for GUI
- Use SDL for GUI

* Mon Jan 16 2012 Zombie Ryushu <ryushu@mandriva.org> 2.3.3-1.gitf2fc773b75.1
+ Revision: 761657
- QT Build
- zlib dependancy
- zlib dependancy
- Upgrade to 2.3.3
- update to latest GIT
- Back to GTK
- disable jit
- Upgrade GIT revision and switch to QT
- Upgrade GIT revision and switch to QT

* Wed Mar 23 2011 Zombie Ryushu <ryushu@mandriva.org> 2.3.2-1.gita2b6937.1
+ Revision: 647758
- Upgrade to latest git

* Sun Mar 13 2011 Funda Wang <fwang@mandriva.org> 2.3.2-1.git6ccc562.1
+ Revision: 644149
- cleanup BRs
- rebuild to obsolete old packages

  + Zombie Ryushu <ryushu@mandriva.org>
    - Update to 2.3.2
    - Upgrade to git7da6740
    - update to latest GIT release
    - update latest git
    - Include the GitHub Build in the Beta ID

* Mon Feb 07 2011 Zombie Ryushu <ryushu@mandriva.org> 2.3.1-1.beta.3
+ Revision: 636765
- Enable GTK mode

* Mon Feb 07 2011 Zombie Ryushu <ryushu@mandriva.org> 2.3.1-1.beta.2
+ Revision: 636560
- Fix qt4 dep
- imported package p-uae

