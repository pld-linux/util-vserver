# TODO:
# - split into core/build/sysv/legacy subpackages
#   (see util-vserver.spec inside of tarball)
#
Summary:	Linux virtual server utilities
Summary(pl):	Narzêdzia dla linuksowych serwerów wirtualnych
Name:		util-vserver
Version:	0.27.199
Release:	1
Epoch:		0
License:	GPL
Group:		Base
Source0:	http://www.13thfloor.at/vserver/d_release/v1.3.6/%{name}-%{version}.tar.bz2
# Source0-md5:	d5d4330dc95dbf70bac9b24d53d1e779
Patch0:		%{name}-maxpath.patch
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
Summary:        Libraries for the linux vserver programs
Summary(pl):    Biblioteki u¿ywane do sterowania linuksowym vserwerem
Group:          Development/Libraries

%description devel
This package contains the header and object files necessary for
developing programs which use vserver library.

%description devel -l pl
Ten pakiet zawiera pliki nag³ówkowe i bibliotekê konieczn± do rozwoju
programów u¿ywaj±cych biblioteki vserver.

%package static
Summary:        Static Libraries for the linux vserver programs
Summary(pl):    Biblioteki statyczne u¿ywane do sterowania linuksowym vserwerem
Group:          Development/Libraries

%description static
This package contains the header and object files necessary for
developing programs which use vserver library.

%description static -l pl
Ten pakiet zawiera pliki nag³ówkowe i bibliotekê konieczn± do rozwoju
programów u¿ywaj±cych biblioteki vserver.

%prep
%setup -q
%patch0 -p1

%build
%configure \
#	--with-kerneldir=%{_kernelsrcdir}
%{__make}


%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/vservers

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_sbindir}/util-vserver-vars

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS THANKS doc/intro.txt
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man8/*
%attr(0,root,root) %dir /vservers
%attr(-,root,root) %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/lib*.so.*

%files devel
%defattr(644,root,root,755)
%{_includedir}/vserver.h
%{_libdir}/lib*.la
%attr(755,root,root) %{_libdir}/lib*.so
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libvserver.a
