#
# m68k and mips are the only not supported archs
#
# Conditional build:
%bcond_without	doc		# don't build documentation which needed LaTeX
#
%define		_pre	pre20051120
Summary:	Linux virtual server utilities
Summary(pl):	Narzêdzia dla linuksowych serwerów wirtualnych
Name:		util-vserver
Version:	1.0
Release:	0.%{_pre}.0.1
License:	GPL
Group:		Applications/System
Source0:	http://dev.gentoo.org/~hollow/vserver/util-vserver/%{name}-%{version}_%{_pre}.tar.bz2
# Source0-md5:	0720eed5a0bacae22d541cb1fdc5f2ed
Source2:	vservers.init
Source5:	vservers.sysconfig
URL:		http://savannah.nongnu.org/projects/util-vserver/
BuildRequires:	autoconf
BuildRequires:	automake >= 1.9
BuildRequires:	beecrypt-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 1.5.14
BuildRequires:	libvserver-devel >= 1.0-0.pre20051119
%ifarch %{x8664}
BuildRequires:	sed >= 4.0
%endif
Requires:	rc-scripts
Requires:	util-linux
Requires(post,preun):	/sbin/chkconfig
Requires:	%{name}-lib = %{version}-%{release}
Obsoletes:	util-vserver-core
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# for adapter
%define		_usrlib		/usr/lib

%description
This package provides the components and a framework to setup virtual
servers. A virtual server runs inside a Linux server. It is
nevertheless highly independent. As such, you can run various services
with normal configuration. The various vservers can't interact with
each other and can't interact with services in the main server.

This requires a special kernel supporting the new new_s_context and
set_ipv4root system call.

This package contains utilities which are required to communicate with
the Linux-Vserver enabled kernel.

%description -l pl
Ten pakiet dostarcza sk³adniki i szkielet do tworzenia wirtualnych
serwerów. Wirtualny serwer dzia³a wewn±trz serwera linuksowego, lecz
jest od niego w du¿ym stopniu niezale¿ny. Jako taki mo¿e uruchamiaæ
ró¿ne us³ugi z normaln± konfiguracj±. Ró¿ne vserwery nie mog± wchodziæ
w interakcjê z innymi ani z us³ugami na g³ównym serwerze.

Wymaga to specjalnego j±dra obs³uguj±cego nowe wywo³ania systemowe
new_s_context i set_ipv4root.

Ten pakiet zawiera narzêdzia wymagane do komunikacji z j±drem z
w³±czonym mechanizmem Linux-Vserver.

%package build
Summary:	Tools which can be used to build vservers
Summary(pl):	Narzêdzia do budowania vserverów
Group:		Applications/System
Conflicts:	poldek < 0.20
Requires:	%{name} = %{version}-%{release}

%description build
util-vserver provides the components and a framework to setup virtual
servers. A virtual server runs inside a linux server. It is
nevertheless highly independent. As such, you can run various services
with normal configuration. The various vservers can't interact with
each other and can't interact with services in the main server.

This package contains utilities which assist in building Vservers.

%description build -l pl
util-vserver dostarcza sk³adniki i szkielet do tworzenia wirtualnych
serwerów. Wirtualny serwer dzia³a wewn±trz serwera linuksowego, lecz
jest od niego w du¿ym stopniu niezale¿ny. Jako taki mo¿e uruchamiaæ
ró¿ne us³ugi z normaln± konfiguracj±. Ró¿ne vserwery nie mog± wchodziæ
w interakcjê z innymi ani z us³ugami na g³ównym serwerze.

Ten pakiet zawiera narzêdzia pomagaj±ce przy budowaniu Vserwerów.

%prep
%setup -q -n %{name}-%{version}_%{_pre}

%build
%configure \
	--with-initrddir=/etc/rc.d/init.d

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/vservers,/etc/{sysconfig,rc.d/init.d}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

sed 's|%{_usrlib}/util-vserver|%{_libdir}/%{name}|g' %{SOURCE2} > \
	$RPM_BUILD_ROOT/etc/rc.d/init.d/vservers
sed 's|%{_usrlib}/util-vserver|%{_libdir}/%{name}|g' %{SOURCE5} > \
	$RPM_BUILD_ROOT/etc/sysconfig/vservers

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_sbindir}/setattr --barrier /vservers || :
/sbin/chkconfig --add vprocunhide
/sbin/chkconfig --add vservers
if [ ! -f /var/lock/subsys/vservers ]; then
	echo "Type \"/etc/rc.d/init.d/vservers start\" to start vservers" 1>&2
fi

%preun
if [ "$1" = "0" ]; then
	if [ -r /var/lock/subsys/vservers ]; then
		/etc/rc.d/init.d/vservers stop >&2
	fi
	/sbin/chkconfig --del vservers
	/sbin/chkconfig --del vprocunhide
fi


%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%dir %{_sysconfdir}/vservers
%dir %{_sysconfdir}/vservers/.defaults
%{_sysconfdir}/vservers/.defaults/vdirbase
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/vservers
%attr(754,root,root) /etc/rc.d/init.d/vservers
%attr(755,root,root) %{_sbindir}/nidof
%attr(755,root,root) %{_sbindir}/vattr
%attr(755,root,root) %{_sbindir}/vcontext
%attr(755,root,root) %{_sbindir}/vdlimit
%attr(755,root,root) %{_sbindir}/vexec
%attr(755,root,root) %{_sbindir}/vflags
%attr(755,root,root) %{_sbindir}/vinfo
%attr(755,root,root) %{_sbindir}/vkill
%attr(755,root,root) %{_sbindir}/vlimit
%attr(755,root,root) %{_sbindir}/vmount
%attr(755,root,root) %{_sbindir}/vnamespace
%attr(755,root,root) %{_sbindir}/vncontext
%attr(755,root,root) %{_sbindir}/vnflags
%attr(755,root,root) %{_sbindir}/vpstree
%attr(755,root,root) %{_sbindir}/vsched
%attr(755,root,root) %{_sbindir}/vserver
%attr(755,root,root) %{_sbindir}/vtop
%attr(755,root,root) %{_sbindir}/vuname
%attr(755,root,root) %{_sbindir}/vwait
%attr(755,root,root) %{_sbindir}/xidof
%dir %{_datadir}/%{name}/commands
%dir %{_datadir}/%{name}/defaults
%dir %{_datadir}/%{name}/lib
%{_datadir}/%{name}/commands/*
%{_datadir}/%{name}/defaults/*
%{_datadir}/%{name}/lib/*
%{_datadir}/%{name}/pathconfig
%attr(000,root,root) %dir /vservers

%files build
%defattr(644,root,root,755)
