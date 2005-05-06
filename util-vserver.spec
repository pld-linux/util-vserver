# TODO:
# - split into core/build/sysv/legacy subpackages
#   (see util-vserver.spec inside of tarball)
#
Summary:	Linux virtual server utilities
Summary(pl):	Narzêdzia dla linuksowych serwerów wirtualnych
Name:		util-vserver
Version:	0.30.207
Release:	0.2
Epoch:		0
License:	GPL
Group:		Base
Source0:	http://www.13thfloor.at/~ensc/util-vserver/files/alpha/%{name}-%{version}.tar.bz2
# Source0-md5:	1c8457a687643ae8a7b1f1d34ebbdd68
Patch0:		%{name}-no-kernel-includes.patch
URL:		http://savannah.nongnu.org/projects/util-vserver/
BuildRequires:	automake >= 1.9
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
%patch0 -p1

%build
%configure
#	--with-kerneldir=%{_kernelsrcdir}
%{__make}

cd doc
xsltproc --stringparam confdir '%{_sysconfdir}/vservers' -o compatibility.html compatibility-xhtml.xsl compatibility.xml
xsltproc --stringparam confdir '%{_sysconfdir}/vservers' -o configuration.html configuration-xhtml.xsl configuration.xml

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
%doc AUTHORS ChangeLog NEWS THANKS doc/intro.txt doc/*.html
%dir %{_sysconfdir}/vservers
%dir %{_sysconfdir}/vservers/.distributions
%{_sysconfdir}/vservers/.distributions/*
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/vservers.conf
%attr(755,root,root) %{_sbindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/defaults
%dir %{_libdir}/%{name}/distributions
%dir %{_libdir}/%{name}/legacy
%{_libdir}/%{name}/defaults/*
%{_libdir}/%{name}/distributions/*
%{_libdir}/%{name}/legacy/*
%attr(755,root,root) %{_libdir}/%{name}/FEATURES.txt
%attr(755,root,root) %{_libdir}/%{name}/capchroot
%attr(755,root,root) %{_libdir}/%{name}/chain-echo
%attr(755,root,root) %{_libdir}/%{name}/chcontext-compat
%attr(755,root,root) %{_libdir}/%{name}/check-unixfile
%attr(755,root,root) %{_libdir}/%{name}/chroot-*
%attr(755,root,root) %{_libdir}/%{name}/exec-ulimit
%attr(755,root,root) %{_libdir}/%{name}/fakerunlevel
%attr(755,root,root) %{_libdir}/%{name}/filetime
%{_libdir}/%{name}/functions
%attr(755,root,root) %{_libdir}/%{name}/keep-ctx-alive
%attr(755,root,root) %{_libdir}/%{name}/lockfile
%attr(755,root,root) %{_libdir}/%{name}/mask2prefix
%attr(755,root,root) %{_libdir}/%{name}/pkgmgmt
%attr(755,root,root) %{_libdir}/%{name}/readlink
%attr(755,root,root) %{_libdir}/%{name}/rpm-fake*
%attr(755,root,root) %{_libdir}/%{name}/save_ctxinfo
%attr(755,root,root) %{_libdir}/%{name}/secure-mount
%attr(755,root,root) %{_libdir}/%{name}/sigexec
%attr(755,root,root) %{_libdir}/%{name}/start-vservers
%{_libdir}/%{name}/util-vserver-vars
%attr(755,root,root) %{_libdir}/%{name}/vapt-get-worker
%attr(755,root,root) %{_libdir}/%{name}/vbuild
%attr(755,root,root) %{_libdir}/%{name}/vcheck
%attr(755,root,root) %{_libdir}/%{name}/vcopy
%attr(755,root,root) %{_libdir}/%{name}/vhashify
%attr(755,root,root) %{_libdir}/%{name}/vpkg
%attr(755,root,root) %{_libdir}/%{name}/vprocunhide
%attr(755,root,root) %{_libdir}/%{name}/vrpm-*
%attr(755,root,root) %{_libdir}/%{name}/vserver-build
%{_libdir}/%{name}/vserver-build.*
%{_libdir}/%{name}/vserver-setup.functions
%attr(755,root,root) %{_libdir}/%{name}/vserver-wrapper
%{_libdir}/%{name}/vserver.*
%attr(755,root,root) %{_libdir}/%{name}/vservers.grabinfo.sh
%attr(755,root,root) %{_libdir}/%{name}/vshelper
%attr(755,root,root) %{_libdir}/%{name}/vshelper-sync
%attr(755,root,root) %{_libdir}/%{name}/vsysvwrapper
%attr(755,root,root) %{_libdir}/%{name}/vunify
%attr(755,root,root) %{_libdir}/%{name}/vyum-worker
%{_mandir}/man8/*
%attr(0,root,root) %dir /vservers

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/vserver.h
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libvserver.a
