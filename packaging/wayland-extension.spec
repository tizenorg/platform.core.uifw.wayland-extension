Name:		wayland-extension
Version:	0.0.1
Release:	0
Summary:	Wayland Extension Protocol
License:	MIT
Group:		Graphics & UI Framework/Wayland Window System
URL:		http://www.tizen.org/
Source:		%name-%version.tar.xz
BuildRequires:	autoconf >= 2.64, automake >= 1.11
BuildRequires:	libtool >= 2.2
BuildRequires:	pkgconfig
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(wayland-client)

%description
wayland-extension is a protocol for tizen window system.

%package -n libwayland-extension-client
Group:		Graphics & UI Framework/Wayland Window System
Summary:	Wayland Extension client library
Requires:   libwayland-client

%description -n libwayland-extension-client
wayland-extension is a protocol for tizen window system.

%package -n libwayland-extension-server
Group:		Graphics & UI Framework/Wayland Window System
Summary:	Wayland Extension server library
Requires:   libwayland-server

%description -n libwayland-extension-server
wayland-extension is a protocol for tizen window system.

%package -n wayland-extension-client-devel
Summary:	Client development files for the Wayland Extension Protocol
Group:		Graphics & UI Framework/Development
Requires:	libwayland-extension-client = %version

%description -n wayland-extension-client-devel
wayland-extension is a protocol for tizen window system.

This package contains all necessary include files and libraries needed
to develop applications that require these.

%package -n wayland-extension-server-devel
Summary:	Server development files for the Wayland Extension Protocol
Group:		Graphics & UI Framework/Development
Requires:	libwayland-extension-server = %version

%description -n wayland-extension-server-devel
wayland-extension is a protocol for tizen window system.

This package contains all necessary include files and libraries needed
to develop a compositor that require these.

%prep
%setup -q

%build
export CFLAGS+=" -Wall -Werror"
%reconfigure --disable-static
make %{?_smp_mflags}

%install
%make_install

%post -n libwayland-extension-client -p /sbin/ldconfig
%postun -n libwayland-extension-client -p /sbin/ldconfig
%post -n libwayland-extension-server -p /sbin/ldconfig
%postun -n libwayland-extension-server -p /sbin/ldconfig

%files -n libwayland-extension-client
%license COPYING
%defattr(-,root,root)
%_libdir/wayland-extension/*-client.so.0*

%files -n libwayland-extension-server
%license COPYING
%defattr(-,root,root)
%_libdir/wayland-extension/*-server.so.0*

%files -n wayland-extension-client-devel
%defattr(-,root,root)
%_includedir/wayland-extension/wayland-extension-version.h
%_includedir/wayland-extension/*-client-protocol.h
%_libdir/wayland-extension/*-client.so
%_libdir/pkgconfig/*-client.pc

%files -n wayland-extension-server-devel
%defattr(-,root,root)
%_includedir/wayland-extension/wayland-extension-version.h
%_includedir/wayland-extension/*-server-protocol.h
%_libdir/wayland-extension/*-server.so
%_libdir/pkgconfig/*-server.pc

%changelog
