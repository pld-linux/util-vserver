# TODO:
# - split into core/build/sysv/legacy subpackages
#   (see util-vserver.spec inside of tarball)
#
Summary:	Linux virtual server utilities
Summary(pl):	Narzêdzia dla linuksowych serwerów wirtualnych
Name:		util-vserver
Version:	0.30.207
Release:	0.1
Epoch:		0
License:	GPL
Group:		Base
Source0:	http://www.13thfloor.at/~ensc/util-vserver/files/alpha/%{name}-%{version}.tar.bz2
# Source0-md5:	1c8457a687643ae8a7b1f1d34ebbdd68
URL:		http://savannah.nongnu.org/projects/util-vserver/
BuildRequires:	e2fsprogs-devel
PreReq:		rc-scripts
Requires(post,preun):	/sbin/chkconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides the components and a framework to setup virtual
servers. A virtual server runs inside a Linux server. It is
nevertheless highly independent. As such, you can run various services
with normal configuration. The various vservers can't interact with
each other and can't interact with services in the main server.

This requires a special kernel supporting the new new_s_context and
set_ipv4root system call.

%description -l pl
Ten pakiet dostarcza sk³adniki i szkielet do tworzenia wirtualnych
serwerów. Wirtualny serwer dzia³a wewn±trz serwera linuksowego, lecz
jest od niego w du¿ym stopniu niezale¿ny. Jako taki mo¿e uruchamiaæ
ró¿ne us³ugi z normaln± konfiguracj±. Ró¿ne vserwery nie mog± wchodziæ
w interakcjê z innymi ani z us³ugami na g³ównym serwerze.

Wymaga to specjalnego j±dra obs³uguj±cego nowe wywo³ania systemowe
new_s_context i set_ipv4root.

%package devel
Summary:	Development files for Linux vserver libraries
Summary(pl):	Pliki programistyczne dla bibliotek linuksowego vserwera
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains the development files necessary for developing
programs which use vserver library.

%description devel -l pl
Ten pakiet zawiera pliki programistyczne konieczne do rozwijania
programów u¿ywaj±cych biblioteki vserver.

%package static
Summary:	Static vserver library
Summary(pl):	Biblioteka statyczna vservera
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
This package contains the static version of vserver library.

%description static -l pl
Ten pakiet zawiera statyczn± wersjê biblioteki vservera.

%prep
%setup -q

%build
%configure
#	--with-kerneldir=%{_kernelsrcdir}
%{__make}


%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/vservers

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_sbindir}/util-vserver-vars

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS THANKS doc/intro.txt
%attr(755,root,root) %{_sbindir}/*
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/distrib-info
%attr(755,root,root) %{_libdir}/%{name}/legacy
%attr(755,root,root) %{_libdir}/%{name}/capchroot
%attr(755,root,root) %{_libdir}/%{name}/fakerunlevel
%attr(755,root,root) %{_libdir}/%{name}/filetime
%attr(755,root,root) %{_libdir}/%{name}/ifspec
%attr(755,root,root) %{_libdir}/%{name}/listdevip
%attr(755,root,root) %{_libdir}/%{name}/parserpmdump
%attr(755,root,root) %{_libdir}/%{name}/readlink
%attr(755,root,root) %{_libdir}/%{name}/rootshell
%{_libdir}/%{name}/sample.conf
%attr(755,root,root) %{_libdir}/%{name}/sample.sh
%attr(755,root,root) %{_libdir}/%{name}/save_s_context
%attr(755,root,root) %{_libdir}/%{name}/setattr
%attr(755,root,root) %{_libdir}/%{name}/showattr
%attr(755,root,root) %{_libdir}/%{name}/showperm
%{_libdir}/%{name}/util-vserver-vars
%attr(755,root,root) %{_libdir}/%{name}/vbuild
%attr(755,root,root) %{_libdir}/%{name}/vcheck
%attr(755,root,root) %{_libdir}/%{name}/vprofile
%attr(755,root,root) %{_libdir}/%{name}/vreboot
%attr(755,root,root) %{_libdir}/%{name}/vserverkillall
%attr(755,root,root) %{_libdir}/%{name}/vservers.grabinfo.sh
%attr(755,root,root) %{_libdir}/%{name}/vsysvwrapper
%attr(755,root,root) %{_libdir}/%{name}/vunify
%{_libdir}/%{name}/*-minimum
%attr(755,root,root) %{_libdir}/%{name}/install-*
%{_mandir}/man8/*
%attr(0,root,root) %dir /vservers

%files devel
%defattr(644,root,root,755)
%{_libdir}/lib*.a
%{_includedir}/vserver.h

%if 0
%files static
%defattr(644,root,root,755)
%{_libdir}/libvserver.a
%endif
