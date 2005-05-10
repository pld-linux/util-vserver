#
# Conditional build:
%bcond_with	dietlibc	# use dietlibc instead of glibc
%bcond_with	xalan		# use the xalan xslt processor

Summary:	Linux virtual server utilities
Summary(pl):	Narzêdzia dla linuksowych serwerów wirtualnych
Name:		util-vserver
Version:	0.30.207
Release:	0.6
Epoch:		0
License:	GPL
Group:		Base
Source0:	http://www.13thfloor.at/~ensc/util-vserver/files/alpha/%{name}-%{version}.tar.bz2
# Source0-md5:	1c8457a687643ae8a7b1f1d34ebbdd68
Source1:	vprocunhide.init
Source2:	vservers-default.init
Source3:	vservers-legacy.init
Source4:	rebootmgr.init
Source5:	vservers-default.sysconfig
Source6:	vservers-legacy.sysconfig
Patch0:		%{name}-no-kernel-includes.patch
Patch1:		%{name}-vsysvwrapper.patch
URL:		http://savannah.nongnu.org/projects/util-vserver/
BuildRequires:	e2fsprogs-devel
BuildRequires:	libxslt-progs
BuildRequires:	vlan
BuildRequires:	doxygen
%{?with_dietlibc:BuildRequires:	dietlibc >= 0:0.25}
%{?with_xalan:BuildRequires:	xalan-j}
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

%package lib
Summary:	Dynamic libraries for util-vserver
Summary(pl):	Biblioteki dynamiczne dla pakietu util-vserver
Group:		Libraries

%description lib
util-vserver provides the components and a framework to setup virtual
servers. A virtual server runs inside a linux server. It is
nevertheless highly independent. As such, you can run various services
with normal configuration. The various vservers can't interact with
each other and can't interact with services in the main server.

This package contains the shared libraries needed by all other
'util-vserver' subpackages.

%description lib -l pl
util-vserver dostarcza sk³adniki i szkielet do tworzenia wirtualnych
serwerów. Wirtualny serwer dzia³a wewn±trz serwera linuksowego, lecz
jest od niego w du¿ym stopniu niezale¿ny. Jako taki mo¿e uruchamiaæ
ró¿ne us³ugi z normaln± konfiguracj±. Ró¿ne vserwery nie mog± wchodziæ
w interakcjê z innymi ani z us³ugami na g³ównym serwerze.

Ten pakiet zawiera biblioteki wspó³dzielone wymagane przez wszystkie
podpakiety util-vserver.

%package core
Summary:	The core-utilities for util-vserver
Summary(pl):	Podstawowe narzêdzia dla util-vserver
Group:		Applications/System
Requires:	util-linux

%description core
util-vserver provides the components and a framework to setup virtual
servers. A virtual server runs inside a linux server. It is
nevertheless highly independent. As such, you can run various services
with normal configuration. The various vservers can't interact with
each other and can't interact with services in the main server.

This package contains utilities which are required to communicate with
the Linux-Vserver enabled kernel.

%description core -l pl
util-vserver dostarcza sk³adniki i szkielet do tworzenia wirtualnych
serwerów. Wirtualny serwer dzia³a wewn±trz serwera linuksowego, lecz
jest od niego w du¿ym stopniu niezale¿ny. Jako taki mo¿e uruchamiaæ
ró¿ne us³ugi z normaln± konfiguracj±. Ró¿ne vserwery nie mog± wchodziæ
w interakcjê z innymi ani z us³ugami na g³ównym serwerze.

Ten pakiet zawiera narzêdzia wymagane do komunikacji z j±drem z
w³±czonym mechanizmem Linux-Vserver.

%package build
Summary:	Tools which can be used to build vservers
Summary(pl):	Narzêdzia do budowania vserverów
Group:		Applications/System
Requires:	binutils
Requires:	e2fsprogs
Requires:	rpm
Requires:	tar
Requires:	wget
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

%package init
Summary:	initscripts for vserver
Summary(pl):	Skrypty inicjalizuj±ce dla vserwera
Group:		Base
Requires(post,preun):	/sbin/chkconfig
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-core = %{version}-%{release}
Requires:	diffutils
Requires:	make
Requires:	rc-scripts

%description init
util-vserver provides the components and a framework to setup virtual
servers. A virtual server runs inside a linux server. It is
nevertheless highly independent. As such, you can run various services
with normal configuration. The various vservers can't interact with
each other and can't interact with services in the main server.

This package contains the SysV initscripts which start and stop
Vservers and related tools.

%description init -l pl
util-vserver dostarcza sk³adniki i szkielet do tworzenia wirtualnych
serwerów. Wirtualny serwer dzia³a wewn±trz serwera linuksowego, lecz
jest od niego w du¿ym stopniu niezale¿ny. Jako taki mo¿e uruchamiaæ
ró¿ne us³ugi z normaln± konfiguracj±. Ró¿ne vserwery nie mog± wchodziæ
w interakcjê z innymi ani z us³ugami na g³ównym serwerze.

Ten pakiet zawiera skrypty inicjalizuj±ce SysV uruchamiaj±ce i
zatrzymuj±ce Vserwery oraz powi±zane narzêdzia.

%package legacy
Summary:	Legacy utilities for util-vserver
Summary(pl):	Stare narzêdzia dla util-vserver
Group:		Applications/System
Requires(post,preun):	/sbin/chkconfig
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-core = %{version}-%{release}
Requires:	rc-scripts

%description legacy
util-vserver provides the components and a framework to setup virtual
servers. A virtual server runs inside a linux server. It is
nevertheless highly independent. As such, you can run various services
with normal configuration. The various vservers can't interact with
each other and can't interact with services in the main server.

This package contains the tools which are needed to work with Vservers
having an old-style configuration.

%description legacy -l pl
util-vserver dostarcza sk³adniki i szkielet do tworzenia wirtualnych
serwerów. Wirtualny serwer dzia³a wewn±trz serwera linuksowego, lecz
jest od niego w du¿ym stopniu niezale¿ny. Jako taki mo¿e uruchamiaæ
ró¿ne us³ugi z normaln± konfiguracj±. Ró¿ne vserwery nie mog± wchodziæ
w interakcjê z innymi ani z us³ugami na g³ównym serwerze.

Ten pakiet zawiera narzêdzia potrzebne do pracy z Vserwerami maj±cymi
konfiguracjê w starym stylu.

%package -n vserver-dev
Summary:	/dev entries for systems in Vservers
Summary(pl):	Pliki specjalne /dev/* dla systemów w Vserwerach
Group:		Base
PreReq:		setup >= 2.4.1-2
Provides:	dev = 2.9.0-19
Obsoletes:	dev
Provides:	devfs
AutoReqProv:	no

%description -n vserver-dev
Unix and unix like systems (including Linux) use file system entries
to represent devices attached to the machine. All of these entries are
in the /dev tree (though they don't have to be), and this package
contains only entries needed for a system running inside Vserver.

DO NOT install this package for a normal system!

%description -n vserver-dev -l pl
Wszystkie systemy klasy unices, w tym Linux, u¿ywaj± plików do
przedstawiania urz±dzeñ pod³±czonych do komputera. Wszystkie te pliki
znajduj± siê zwykle w katalogu /dev. Pakiet ten wy³±cznie te pliki
specjalne które s± potrzebne do uruchomienia systemu w Vserwerze.

NIE INSTALUJ tego pakietu na zwyk³ym systemie!

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%configure \
	--with-initrddir=/etc/rc.d/init.d \
	--enable-release \
	%{?with_dietlibc:--enable-dietlibc} \
	%{!?with_dietlibc:--disable-dietlibc}

%{__make} all
%{__make} doc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/vservers,/etc/{sysconfig,rc.d/init.d},/dev/pts}

%{__make} install install-distribution \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/etc/vservices
install -d $RPM_BUILD_ROOT/vservers/.pkg
ln -s /vservers $RPM_BUILD_ROOT%{_sysconfdir}/vservers/vdirbase
ln -s %{_localstatedir}/run/vservers.rev $RPM_BUILD_ROOT%{_sysconfdir}/vservers/run.rev

for i in $RPM_BUILD_ROOT/etc/rc.d/init.d/v_* ; do
	s=`basename $i | sed s/v_//`
	cat >$RPM_BUILD_ROOT/etc/vservices/$s << EOF
# IP addresses/interfaces to bound $s service to
#IP=10.0.0.1
#IP=eth0
EOF
done

install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/vprocunhide
install %{SOURCE2} $RPM_BUILD_ROOT/etc/rc.d/init.d/vservers-default
install %{SOURCE3} $RPM_BUILD_ROOT/etc/rc.d/init.d/vservers-legacy
install %{SOURCE4} $RPM_BUILD_ROOT/etc/rc.d/init.d/rebootmgr
install %{SOURCE5} $RPM_BUILD_ROOT/etc/sysconfig/vservers-default
install %{SOURCE6} $RPM_BUILD_ROOT/etc/sysconfig/vservers-legacy

ln -sf /dev/null $RPM_BUILD_ROOT/dev/initctl

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_sbindir}/setattr --barrier /vservers || :

%post	lib -p /sbin/ldconfig
%postun	lib -p /sbin/ldconfig

%post init
/sbin/chkconfig --add vservers-default
/sbin/chkconfig --add vprocunhide
#if [ -r /var/lock/subsys/vprocunhide ]; then
#	/etc/rc.d/init.d/vprocunhide restart >&2
#fi
#if [ -r /var/lock/subsys/vservers-default ]; then
#	/etc/rc.d/init.d/vservers-default restart >&2
#fi

%preun init
if [ "$1" = "0" ]; then
        if [ -r /var/lock/subsys/vprocunhide ]; then
		/etc/rc.d/init.d/vprocunhide stop >&2
        fi
        if [ -r /var/lock/subsys/vservers-default ]; then
		/etc/rc.d/init.d/vservers-default stop >&2
        fi
        /sbin/chkconfig --del vprocunhide
        /sbin/chkconfig --del vservers-default
fi

%post legacy
/sbin/chkconfig --add rebootmgr
/sbin/chkconfig --add vservers-legacy
#if [ -r /var/lock/subsys/rebootmgr ] ; then
#	/etc/rc.d/init.d/rebootmgr restart >&2
#fi
#if [ -r /var/lock/subsys/vservers-legacy ] ; then
#	/etc/rc.d/init.d/vservers-legacy restart >&2
#fi

%preun legacy
if [ "$1" = "0" ]; then
	if [ -r /var/lock/subsys/rebootmgr ] ; then
		/etc/rc.d/init.d/rebootmgr stop >&2
	fi
	if [ -r /var/lock/subsys/vservers-legacy ] ; then
		/etc/rc.d/init.d/vservers-legacy stop >&2
	fi
	/sbin/chkconfig --del rebootmgr
	/sbin/chkconfig --del vservers-legacy
fi

%post -n vserver-dev
cat << EOF

 **************************************************
 *                                                *
 *  	         BIG FAT WARNING!!!               *
 *                                                *
 *  This package is for use inside Vserver ONLY!  *
 *  DO NOT install it on normal system!           *
 *                                                *
 **************************************************

EOF

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS THANKS doc/intro.txt doc/*.html
%dir %{_sysconfdir}/vservers
%dir %{_sysconfdir}/vservers/.defaults
%dir %{_sysconfdir}/vservers/.defaults/apps
%dir %{_sysconfdir}/vservers/.defaults/files
%{_sysconfdir}/vservers/.defaults/vdirbase
%{_sysconfdir}/vservers/.defaults/run.rev
%{_sysconfdir}/vservers/vdirbase
%{_sysconfdir}/vservers/run.rev
/sbin/vshelper
%attr(755,root,root) %{_sbindir}/exec-cd
%attr(755,root,root) %{_sbindir}/vdu
%attr(755,root,root) %{_sbindir}/vps
%attr(755,root,root) %{_sbindir}/vpstree
%attr(755,root,root) %{_sbindir}/vserver
%attr(755,root,root) %{_sbindir}/vserver-stat
%attr(755,root,root) %{_sbindir}/vsomething
%attr(755,root,root) %{_sbindir}/vtop
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/defaults
%{_libdir}/%{name}/defaults/*
%attr(755,root,root) %{_libdir}/%{name}/capchroot
%attr(755,root,root) %{_libdir}/%{name}/chain-echo
%attr(755,root,root) %{_libdir}/%{name}/check-unixfile
%attr(755,root,root) %{_libdir}/%{name}/chroot-*
%attr(755,root,root) %{_libdir}/%{name}/exec-ulimit
%attr(755,root,root) %{_libdir}/%{name}/fakerunlevel
%attr(755,root,root) %{_libdir}/%{name}/filetime
%{_libdir}/%{name}/functions
%attr(755,root,root) %{_libdir}/%{name}/keep-ctx-alive
%attr(755,root,root) %{_libdir}/%{name}/lockfile
%attr(755,root,root) %{_libdir}/%{name}/mask2prefix
%attr(755,root,root) %{_libdir}/%{name}/readlink
%attr(755,root,root) %{_libdir}/%{name}/save_ctxinfo
%attr(755,root,root) %{_libdir}/%{name}/secure-mount
%attr(755,root,root) %{_libdir}/%{name}/sigexec
%attr(755,root,root) %{_libdir}/%{name}/start-vservers
%attr(755,root,root) %{_libdir}/%{name}/vprocunhide
%{_libdir}/%{name}/vserver.*
%attr(755,root,root) %{_libdir}/%{name}/vservers.grabinfo.sh
%attr(755,root,root) %{_libdir}/%{name}/vshelper
%attr(755,root,root) %{_libdir}/%{name}/vshelper-sync
%{_mandir}/man8/*
%attr(0,root,root) %dir /vservers
%attr(755,root,root) %dir /vservers/.pkg
%dir %{_localstatedir}/run/vservers
%dir %{_localstatedir}/run/vservers.rev
%dir %{_localstatedir}/run/vshelper

%files devel
%defattr(644,root,root,755)
%doc lib/apidoc/latex/refman.pdf lib/apidoc/html
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/vserver.h
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libvserver.a

%files lib
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files init
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/vsysvwrapper
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/vservers-default
%attr(754,root,root) /etc/rc.d/init.d/vprocunhide
%attr(754,root,root) /etc/rc.d/init.d/vservers-default

%files core
%defattr(644,root,root,755)
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/FEATURES.txt
%{_libdir}/%{name}/util-vserver-vars
%attr(755,root,root) %{_libdir}/%{name}/chcontext-compat
%attr(755,root,root) %{_sbindir}/chbind
%attr(755,root,root) %{_sbindir}/chcontext
%attr(755,root,root) %{_sbindir}/chxid
%attr(755,root,root) %{_sbindir}/lsxid
%attr(755,root,root) %{_sbindir}/reducecap
%attr(755,root,root) %{_sbindir}/setattr
%attr(755,root,root) %{_sbindir}/showattr
%attr(755,root,root) %{_sbindir}/vattribute
%attr(755,root,root) %{_sbindir}/vcontext
%attr(755,root,root) %{_sbindir}/vdlimit
%attr(755,root,root) %{_sbindir}/vnamespace
%attr(755,root,root) %{_sbindir}/vkill
%attr(755,root,root) %{_sbindir}/vlimit
%attr(755,root,root) %{_sbindir}/vrsetup
%attr(755,root,root) %{_sbindir}/vsched
%attr(755,root,root) %{_sbindir}/vserver-info
%attr(755,root,root) %{_sbindir}/vuname
%{_mandir}/man8/chbind*
%{_mandir}/man8/chcontext*
%{_mandir}/man8/reducecap*

%files build
%defattr(644,root,root,755)
%doc contrib/yum*.patch
%dir %{_sysconfdir}/vservers/.distributions
%{_sysconfdir}/vservers/.distributions/.common
%{_sysconfdir}/vservers/.distributions/*
%dir %{_sysconfdir}/vservers/.defaults/apps/vunify
%dir %{_sysconfdir}/vservers/.defaults/apps/vunify/hash
%attr(755,root,root) %{_libdir}/%{name}/rpm-fake*
%dir %{_libdir}/%{name}/distributions
%{_libdir}/%{name}/distributions/*
%{_libdir}/%{name}/vserver-build.*
%{_libdir}/%{name}/vserver-setup.functions
%{_libdir}/%{name}/defaults/fstab
%{_libdir}/%{name}/defaults/debootstrap.uri
%{_libdir}/%{name}/defaults/vunify-exclude
%attr(755,root,root) %{_libdir}/%{name}/pkgmgmt
%attr(755,root,root) %{_libdir}/%{name}/vapt-get-worker
%attr(755,root,root) %{_libdir}/%{name}/vbuild
%attr(755,root,root) %{_libdir}/%{name}/vcheck
%attr(755,root,root) %{_libdir}/%{name}/vcopy
%attr(755,root,root) %{_libdir}/%{name}/vhashify
%attr(755,root,root) %{_libdir}/%{name}/vpkg
%attr(755,root,root) %{_libdir}/%{name}/vrpm-*
%attr(755,root,root) %{_libdir}/%{name}/vserver-build
%attr(755,root,root) %{_libdir}/%{name}/vunify
%attr(755,root,root) %{_libdir}/%{name}/vyum-worker
%attr(755,root,root) %{_sbindir}/vapt-get
%attr(755,root,root) %{_sbindir}/vfiles
%attr(755,root,root) %{_sbindir}/vrpm
%attr(755,root,root) %{_sbindir}/vyum
%{_mandir}/man8/vserver-copy*

%files legacy
%defattr(644,root,root,755)
%dir /etc/vservices
/etc/vservices/*
%dir %{_libdir}/%{name}/legacy
%attr(755,root,root) %{_libdir}/%{name}/legacy/*
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/vservers-legacy
%attr(754,root,root) /etc/rc.d/init.d/v_*
%attr(754,root,root) /etc/rc.d/init.d/rebootmgr
%attr(754,root,root) /etc/rc.d/init.d/vservers-legacy
%attr(755,root,root) %{_sbindir}/vserver-copy
%{_mandir}/man8/distrib-info*
%{_mandir}/man8/rebootmgr*
%{_mandir}/man8/vps.*

%files -n vserver-dev
%defattr(644,root,root,755)
%dir /dev/pts
%dev(c,1,7) %attr(666,root,root) /dev/full
%dev(c,1,3) %attr(666,root,root) /dev/null
%dev(c,5,2) %attr(666,root,root) /dev/ptmx
%dev(c,1,8) %attr(644,root,root) /dev/random
%dev(c,5,0) %attr(666,root,root) /dev/tty
%dev(c,1,9) %attr(644,root,root) /dev/urandom
%dev(c,1,5) %attr(666,root,root) /dev/zero
/dev/initctl
