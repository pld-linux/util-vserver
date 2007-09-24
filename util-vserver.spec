# TODO
# - somewhy empty /var/cache/vservers is needed when building pld vserver
# - make build create /dev/std{in,out,err} links
# - reject install in %pre if /proc/virtual/info has incompatible version
#
# m68k and mips are the only not supported archs
#
# Conditional build:
%bcond_without	dietlibc		# don't use dietlibc (ask for troubles)
%bcond_without	doc			# don't build documentation which needed LaTeX
%bcond_without	no_dynamic_context	# disable enforcement of disabled dynamic context
%bcond_with	xalan			# use the xalan xslt processor
#
%define	_vproc_version 0.01
# diet compile fails with ccache in %{__cc}
%undefine	with_ccache
#
Summary:	Linux virtual server utilities
Summary(pl.UTF-8):	Narzędzia dla linuksowych serwerów wirtualnych
Name:		util-vserver
Version:	0.30.214
Release:	2
License:	GPL
Group:		Applications/System
Source0:	http://ftp.linux-vserver.org/pub/utils/util-vserver/%{name}-%{version}.tar.bz2
# Source0-md5:	8bad879e36a6a1b9b4858d0d6d3c8c76
Source1:	vprocunhide.init
Source2:	vservers.init
Source3:	vservers-legacy.init
Source4:	rebootmgr.init
Source5:	vservers.sysconfig
Source6:	vservers-legacy.sysconfig
Source7:	vrootdevices.init
Source8:	vrootdevices.sysconfig
# A bit of documentation explaining package management
# http://www.paul.sladen.org/vserver/archives/200505/0078.html
Source9:	%{name}-pkgmgmt.txt
Source10:	%{name}-initpost.sh
Source11:	http://www.13thfloor.at/vserver/s_release/v1.2.10/vproc-%{_vproc_version}.tar.bz2
# Source11-md5:	1d030717bdbc958ea4b35fd2410dad85
Source12:	%{name}-vhashify.cron
Patch0:		%{name}-vsysvwrapper.patch
Patch1:		%{name}-pld.patch
Patch2:		%{name}-vrpm.patch
Patch3:		%{name}-include.patch
Patch4:		%{name}-m4-diet.patch
Patch6:		%{name}-build-umask.patch
Patch7:		%{name}-utmpx.patch
Patch8:		%{name}-vprocunhide.patch
Patch9:		%{name}-dev.patch
Patch10:	%{name}-no-dynamic-ctx.patch
Patch11:	%{name}-more-ip.patch
Patch12:	%{name}-rpm-fake-resolver-badperm-errorlogging.patch
Patch13:	%{name}-tmpdir.patch
URL:		http://savannah.nongnu.org/projects/util-vserver/
BuildRequires:	autoconf
BuildRequires:	automake >= 1.9
BuildRequires:	beecrypt-devel
%{?with_dietlibc:BuildRequires:	dietlibc-static >= 2:0.29}
BuildRequires:	e2fsprogs-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 1.5.14
%ifarch %{x8664}
BuildRequires:	sed >= 4.0
%endif
BuildRequires:	rpmbuild(macros) >= 1.268
%if %{with doc}
BuildRequires:	doxygen
BuildRequires:	graphviz
BuildRequires:	libxslt-progs
BuildRequires:	tetex-format-pdflatex
BuildRequires:	tetex-makeindex
# To be removed when tetex-format-pdflatex, tetex-pdftex...
# ...and graphviz packages get fixed
BuildRequires:	ghostscript
BuildRequires:	ghostscript-fonts-std
BuildRequires:	tetex-fonts-jknappen
BuildRequires:	tetex-metafont
%{?with_xalan:BuildRequires:	xalan-j}
%endif
Requires(post,preun):	/sbin/chkconfig
Requires:	%{name}-lib = %{version}-%{release}
Requires:	issue
Requires:	mktemp >= 1.5-18
Requires:	rc-scripts
Requires:	tar
Requires:	util-linux
Obsoletes:	util-vserver-core
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# for adapter
%define		_usrbin		/usr/bin
%define		_usrsbin	/usr/sbin
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

%description -l pl.UTF-8
Ten pakiet dostarcza składniki i szkielet do tworzenia wirtualnych
serwerów. Wirtualny serwer działa wewnątrz serwera linuksowego, lecz
jest od niego w dużym stopniu niezależny. Jako taki może uruchamiać
różne usługi z normalną konfiguracją. Różne vserwery nie mogą wchodzić
w interakcję z innymi ani z usługami na głównym serwerze.

Wymaga to specjalnego jądra obsługującego nowe wywołania systemowe
new_s_context i set_ipv4root.

Ten pakiet zawiera narzędzia wymagane do komunikacji z jądrem z
włączonym mechanizmem Linux-Vserver.

%package lib
Summary:	Dynamic libraries for util-vserver
Summary(pl.UTF-8):	Biblioteki dynamiczne dla pakietu util-vserver
Group:		Libraries

%description lib
util-vserver provides the components and a framework to setup virtual
servers. A virtual server runs inside a linux server. It is
nevertheless highly independent. As such, you can run various services
pith normal configuration. The various vservers can't interact with
each other and can't interact with services in the main server.

This package contains the shared libraries needed by all other
'util-vserver' subpackages.

%description lib -l pl.UTF-8
util-vserver dostarcza składniki i szkielet do tworzenia wirtualnych
serwerów. Wirtualny serwer działa wewnątrz serwera linuksowego, lecz
jest od niego w dużym stopniu niezależny. Jako taki może uruchamiać
różne usługi z normalną konfiguracją. Różne vserwery nie mogą wchodzić
w interakcję z innymi ani z usługami na głównym serwerze.

Ten pakiet zawiera biblioteki współdzielone wymagane przez wszystkie
podpakiety util-vserver.

%package devel
Summary:	Development files for Linux vserver libraries
Summary(pl.UTF-8):	Pliki programistyczne dla bibliotek linuksowego vserwera
Group:		Development/Libraries
Requires:	%{name}-lib = %{version}-%{release}

%description devel
This package contains the development files necessary for developing
programs which use vserver library.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki programistyczne konieczne do rozwijania
programów używających biblioteki vserver.

%package static
Summary:	Static vserver library
Summary(pl.UTF-8):	Biblioteka statyczna vservera
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
This package contains the static version of vserver library.

%description static -l pl.UTF-8
Ten pakiet zawiera statyczną wersję biblioteki vservera.

%package build
Summary:	Tools which can be used to build vservers
Summary(pl.UTF-8):	Narzędzia do budowania vserverów
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}
Requires:	/etc/pld-release
Requires:	e2fsprogs
Requires:	which
Conflicts:	poldek < 0.18.8-10

%description build
util-vserver provides the components and a framework to setup virtual
servers. A virtual server runs inside a linux server. It is
nevertheless highly independent. As such, you can run various services
with normal configuration. The various vservers can't interact with
each other and can't interact with services in the main server.

This package contains utilities which assist in building Vservers.

%description build -l pl.UTF-8
util-vserver dostarcza składniki i szkielet do tworzenia wirtualnych
serwerów. Wirtualny serwer działa wewnątrz serwera linuksowego, lecz
jest od niego w dużym stopniu niezależny. Jako taki może uruchamiać
różne usługi z normalną konfiguracją. Różne vserwery nie mogą wchodzić
w interakcję z innymi ani z usługami na głównym serwerze.

Ten pakiet zawiera narzędzia pomagające przy budowaniu Vserwerów.

%package init
Summary:	initscripts for vserver
Summary(pl.UTF-8):	Skrypty inicjalizujące dla vserwera
Group:		Applications/System
Requires(post,preun):	/sbin/chkconfig
Requires:	%{name} = %{version}-%{release}
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

%description init -l pl.UTF-8
util-vserver dostarcza składniki i szkielet do tworzenia wirtualnych
serwerów. Wirtualny serwer działa wewnątrz serwera linuksowego, lecz
jest od niego w dużym stopniu niezależny. Jako taki może uruchamiać
różne usługi z normalną konfiguracją. Różne vserwery nie mogą wchodzić
w interakcję z innymi ani z usługami na głównym serwerze.

Ten pakiet zawiera skrypty inicjalizujące SysV uruchamiające i
zatrzymujące Vserwery oraz powiązane narzędzia.

%package legacy
Summary:	Legacy utilities for util-vserver
Summary(pl.UTF-8):	Stare narzędzia dla util-vserver
Group:		Applications/System
Requires(post,preun):	/sbin/chkconfig
Requires:	%{name} = %{version}-%{release}
Requires:	rc-scripts

%description legacy
util-vserver provides the components and a framework to setup virtual
servers. A virtual server runs inside a linux server. It is
nevertheless highly independent. As such, you can run various services
with normal configuration. The various vservers can't interact with
each other and can't interact with services in the main server.

This package contains the tools which are needed to work with Vservers
having an old-style configuration.

%description legacy -l pl.UTF-8
util-vserver dostarcza składniki i szkielet do tworzenia wirtualnych
serwerów. Wirtualny serwer działa wewnątrz serwera linuksowego, lecz
jest od niego w dużym stopniu niezależny. Jako taki może uruchamiać
różne usługi z normalną konfiguracją. Różne vserwery nie mogą wchodzić
w interakcję z innymi ani z usługami na głównym serwerze.

Ten pakiet zawiera narzędzia potrzebne do pracy z Vserwerami mającymi
konfigurację w starym stylu.

%package -n vserver-distro-debian
Summary:	VServer build templates for Debian
Summary(pl):	Szablony do tworzenia VServerów dla dystrybucji Debian
Group:		Applications/System
Requires:	%{name}-build = %{version}-%{release}
Requires:	dpkg

%description -n vserver-distro-debian
VServer build templates for Debian.

%description -n vserver-distro-debian -l pl
Szablony do tworzenia VServerów dla dystrybucji Debian.

%package -n vserver-distro-centos
Summary:	VServer build template for CentOS
Summary(pl.UTF-8):	Szablon budowania VServerów dla dystrybucji CentOS
Group:		Applications/System
Requires:	%{name}-build = %{version}-%{release}
Requires:	yum

%description -n vserver-distro-centos
VServer build template for CentOS 4.2 and 5.

%description -n vserver-distro-centos -l pl.UTF-8
Szablon budowania VServerów dla dystrybucji CentOS 4.2 i 5.

%package -n vserver-distro-fedora
Summary:	VServer build templates for Fedora
Summary(pl.UTF-8):	Szablony do tworzenia VServerów dla dystrybucji Fedora
Group:		Applications/System
Requires:	%{name}-build = %{version}-%{release}
Requires:	binutils
Requires:	e2fsprogs
Requires:	rpm
Requires:	wget

%description -n vserver-distro-fedora
VServer build templates for Fedora Core 1,2,3,4,5,6 and Fedora 7.

%description -n vserver-distro-fedora -l pl.UTF-8
Szablony do tworzenia VServerów dla dystrybucji Fedora Core
1,2,3,4,5,6 oraz Fedora 7.

%package -n vserver-distro-gentoo
Summary:	VServer build template for Gentoo
Summary(pl.UTF-8):	Szablon budowania VServerów dla Gentoo
Group:		Applications/System
Requires:	%{name}-build = %{version}-%{release}

%description -n vserver-distro-gentoo
VServer build template for Gentoo.

%description -n vserver-distro-gentoo -l pl.UTF-8
Szablon budowania VServerów dla Gentoo.

%package -n vserver-distro-redhat
Summary:	VServer build template for Red Hat Linux 9
Summary(pl.UTF-8):	Szablon do tworzenia VServerów dla dystrybucji Red Hat Linux 9
Group:		Applications/System
Requires:	%{name}-build = %{version}-%{release}
Requires:	binutils
Requires:	e2fsprogs
Requires:	rpm
Requires:	wget

%description -n vserver-distro-redhat
VServer build template for RedHat Linux 9.

%description -n vserver-distro-redhat -l pl.UTF-8
Szablon do tworzenia VServerów dla dystrybucji Red Hat Linux 9.

%package -n vserver-distro-suse
Summary:	VServer build template for SuSE 9.1
Summary(pl.UTF-8):	Szablon do tworzenia VServerów dla dystrybucji SuSE 9.1
Group:		Applications/System
Requires:	%{name}-build = %{version}-%{release}
Requires:	binutils
Requires:	e2fsprogs
Requires:	rpm
Requires:	wget

%description -n vserver-distro-suse
VServer build template for SuSE Linux 9.1.

%description -n vserver-distro-suse -l pl.UTF-8
Szablon do tworzenia VServerów dla dystrybucji SuSE 9.1.

%package -n vserver-distro-ubuntu
Summary:	VServer build templates for Ubuntu
Summary(pl):	Szablony do tworzenia VServerów dla dystrybucji Ubuntu
Group:		Applications/System
Requires:	%{name}-build = %{version}-%{release}
Requires:	dpkg

%description -n vserver-distro-ubuntu
VServer build templates for Ubuntu.

%description -n vserver-distro-ubuntu -l pl
Szablony do tworzenia VServerów dla dystrybucji Ubuntu.

%prep
%setup -q -a11
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%{?with_no_dynamic_context:%patch10 -p1}
%patch11 -p1
%patch12 -p1
%patch13 -p1

install %{SOURCE9} package-management.txt

cp -a compat.h vserver-compat.h

%build
unset LD_SYMBOLIC_FUNCTIONS || :

%if %{with dietlibc}
CFLAGS="%{rpmcflags} -D__GLIBC__ -D__KERNEL_STRICT_NAMES=1 -U__STRICT_ANSI__"
%endif
%{__aclocal} -I m4
%{__automake}
%{__autoconf}
%configure \
	--with-initrddir=/etc/rc.d/init.d \
	--enable-release \
	--enable-apis=NOLEGACY \
	--with-initscripts=sysv \
	--%{?with_dietlibc:en}%{!?with_dietlibc:dis}able-dietlibc \
	MKTEMP=/bin/mktemp \
	MOUNT=/bin/mount \
	PS=/bin/ps \
	UMOUNT=/bin/umount \
	IP=/sbin/ip \
	IPTABLES=%{_usrsbin}/iptables \
	MODPROBE=/sbin/modprobe \
	NAMEIF=/sbin/nameif \
	RMMOD=/sbin/rmmod \
	VCONFIG=/sbin/vconfig \
	WGET=%{_usrbin}/wget \

%{__make} all
%{?with_doc:%{__make} doc}

%{__make} -C vproc-%{_vproc_version} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/vservers,/etc/{sysconfig,rc.d/init.d,cron.d},/dev/pts} \
	$RPM_BUILD_ROOT{%{_sysconfdir}/vservices,/vservers/.pkg}

%{__make} -j1 install install-distribution \
	DESTDIR=$RPM_BUILD_ROOT

cp -a vserver-compat.h $RPM_BUILD_ROOT%{_includedir}

chmod -R +rX $RPM_BUILD_ROOT%{_libdir}/%{name}/distributions/*

for i in $RPM_BUILD_ROOT/etc/rc.d/init.d/v_* ; do
	s=`basename $i | sed s/v_//`
	cat >$RPM_BUILD_ROOT%{_sysconfdir}/vservices/$s << EOF
# IP addresses/interfaces to bound $s service to
#IP=10.0.0.1
#IP=eth0
EOF
done

sed 's|%{_usrlib}/util-vserver|%{_libdir}/%{name}|g' %{SOURCE1} > \
	$RPM_BUILD_ROOT/etc/rc.d/init.d/vprocunhide
sed 's|%{_usrlib}/util-vserver|%{_libdir}/%{name}|g' %{SOURCE2} > \
	$RPM_BUILD_ROOT/etc/rc.d/init.d/vservers
sed 's|%{_usrlib}/util-vserver|%{_libdir}/%{name}|g' %{SOURCE3} > \
	$RPM_BUILD_ROOT/etc/rc.d/init.d/vservers-legacy
sed 's|%{_usrlib}/util-vserver|%{_libdir}/%{name}|g' %{SOURCE4} > \
	$RPM_BUILD_ROOT/etc/rc.d/init.d/rebootmgr
sed 's|%{_usrlib}/util-vserver|%{_libdir}/%{name}|g' %{SOURCE5} > \
	$RPM_BUILD_ROOT/etc/sysconfig/vservers

install %{SOURCE6} $RPM_BUILD_ROOT/etc/sysconfig/vservers-legacy

install %{SOURCE7} $RPM_BUILD_ROOT/etc/rc.d/init.d/vrootdevices
install %{SOURCE8} $RPM_BUILD_ROOT/etc/sysconfig/vrootdevices
install %{SOURCE10} $RPM_BUILD_ROOT%{_libdir}/%{name}/distributions/pld-ac/initpost
install %{SOURCE10} $RPM_BUILD_ROOT%{_libdir}/%{name}/distributions/pld-th/initpost
install vproc-%{_vproc_version}/vproc $RPM_BUILD_ROOT%{_sbindir}
install %{SOURCE12} $RPM_BUILD_ROOT%{_libdir}/%{name}/vhashify.cron

cat > $RPM_BUILD_ROOT/etc/cron.d/vservers << EOF
02 2 * * 0      root    %{_libdir}/%{name}/vhashify.cron
EOF

ln -sf null $RPM_BUILD_ROOT/dev/initctl

%ifarch %{x8664}
# ac i686
cp -a $RPM_BUILD_ROOT%{_libdir}/%{name}/distributions/pld-ac \
	$RPM_BUILD_ROOT%{_libdir}/%{name}/distributions/pld-ac-i686
echo "%{_target_cpu}-%{_target_vendor}-linux" > $RPM_BUILD_ROOT%{_libdir}/%{name}/distributions/pld-ac/rpm/platform
echo "i686-%{_target_vendor}-linux" > $RPM_BUILD_ROOT%{_libdir}/%{name}/distributions/pld-ac-i686/rpm/platform
cp -a $RPM_BUILD_ROOT%{_sysconfdir}/vservers/.distributions/pld-ac \
        $RPM_BUILD_ROOT%{_sysconfdir}/vservers/.distributions/pld-ac-i686
sed -i 's/x86_64/i686/g' $RPM_BUILD_ROOT%{_sysconfdir}/vservers/.distributions/pld-ac-i686/poldek/*.conf

# th i686
cp -a $RPM_BUILD_ROOT%{_libdir}/%{name}/distributions/pld-th \
        $RPM_BUILD_ROOT%{_libdir}/%{name}/distributions/pld-th-i686
echo "%{_target_cpu}-%{_target_vendor}-linux" > $RPM_BUILD_ROOT%{_libdir}/%{name}/distributions/pld-th/rpm/platform
echo "i686-%{_target_vendor}-linux" > $RPM_BUILD_ROOT%{_libdir}/%{name}/distributions/pld-th-i686/rpm/platform
cp -a $RPM_BUILD_ROOT%{_sysconfdir}/vservers/.distributions/pld-th \
	$RPM_BUILD_ROOT%{_sysconfdir}/vservers/.distributions/pld-th-i686
sed -i 's/x86_64/i686/g' $RPM_BUILD_ROOT%{_sysconfdir}/vservers/.distributions/pld-th-i686/poldek/*.conf

# ac x86_64
sed -i 's/^glibc$/glibc64/' $RPM_BUILD_ROOT%{_libdir}/%{name}/distributions/pld-ac/pkgs/01
sed -i 's/glibc\-\[0\-9\]\*\.rpm/glibc64\-\[0\-9\]\*\.rpm/' $RPM_BUILD_ROOT%{_libdir}/%{name}/distributions/pld-ac/rpmlist.d/00.lst
sed -i 's/x86_64/amd64/g' $RPM_BUILD_ROOT%{_sysconfdir}/vservers/.distributions/pld-ac/poldek/*.conf
%endif
%ifarch i486
sed -i 's/i486/i386/g' $RPM_BUILD_ROOT%{_sysconfdir}/vservers/.distributions/pld-ac/poldek/*.conf
%endif

# XXX baggins check this: needed but seems unused
install -d $RPM_BUILD_ROOT/var/cache/vservers

# we have our own initscript which does the same
rm -f $RPM_BUILD_ROOT/etc/rc.d/init.d/vservers-default
rm -f $RPM_BUILD_ROOT%{_libdir}/util-vserver/vserver-wrapper
# probaly the part of them
rm -f $RPM_BUILD_ROOT%{_sysconfdir}/vservers.conf

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_sbindir}/setattr --barrier /vservers || :

%post	lib -p /sbin/ldconfig
%postun	lib -p /sbin/ldconfig

%triggerpostun build -- %{name}-build < 0.30.210-5.2
if [ -f /etc/vservers/.distributions/pld2.0/poldek/poldek.conf.rpmsave ]; then
	mv -f /etc/vservers/.distributions/{pld2.0,pld-ac}/poldek/poldek.conf.rpmsave
fi

# kill old vserver specific package ignores which are no longer needed
l=`egrep '^ignore.*(basesystem|SysVinit|rc-scripts)' /etc/vservers/*/apps/pkgmgmt/base/poldek/etc/poldek.conf -l 2>/dev/null`
if [ "$l" ]; then
	%{__sed} -i -e '/^ignore/s, \(basesystem\|SysVinit\|rc-scripts\),,g' $l
fi

%post init
/sbin/chkconfig --add vrootdevices
/sbin/chkconfig --add vprocunhide
/sbin/chkconfig --add vservers
if [ ! -f /var/lock/subsys/vrootdevices ]; then
	echo "Type \"/sbin/service vrootdevices start\" to assign virtual root devices" 1>&2
fi
if [ ! -f /var/lock/subsys/vprocunhide ]; then
	echo "Type \"/sbin/service vprocunhide start\" to set /proc visibility for vservers" 1>&2
fi
if [ ! -f /var/lock/subsys/vservers ]; then
	echo "Type \"/sbin/service vservers start\" to start vservers" 1>&2
fi

%preun init
if [ "$1" = "0" ]; then
	%service vservers stop
	%service vprocunhide stop
	%service vrootdevices stop
	/sbin/chkconfig --del vservers
	/sbin/chkconfig --del vprocunhide
	/sbin/chkconfig --del vrootdevices
fi

%post legacy
/sbin/chkconfig --add rebootmgr
/sbin/chkconfig --add vservers-legacy
if [ ! -f /var/lock/subsys/rebootmgr ] ; then
	echo "Type \"/sbin/service rebootmgr start\" to start reboot manager for legacy vservers" 1>&2
fi
if [ ! -f /var/lock/subsys/vservers-legacy ] ; then
	echo "Type \"/sbin/service vservers-legacy start\" to start legacy vservers" 1>&2
fi

%preun legacy
if [ "$1" = "0" ]; then
	%service rebootmgr stop
	%service vservers-legacy stop
	/sbin/chkconfig --del rebootmgr
	/sbin/chkconfig --del vservers-legacy
fi

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS THANKS doc/intro.txt
%{?with_doc:%doc doc/*.html}
%dir %{_sysconfdir}/vservers
%dir %{_sysconfdir}/vservers/.defaults
%dir %{_sysconfdir}/vservers/.defaults/apps
%dir %{_sysconfdir}/vservers/.defaults/files
%{_sysconfdir}/vservers/.defaults/vdirbase
%{_sysconfdir}/vservers/.defaults/run.rev
/sbin/vshelper
%attr(755,root,root) %{_sbindir}/chbind
%attr(755,root,root) %{_sbindir}/chcontext
%attr(755,root,root) %{_sbindir}/chxid
%attr(755,root,root) %{_sbindir}/exec-cd
%attr(755,root,root) %{_sbindir}/lsxid
%attr(755,root,root) %{_sbindir}/naddress
%attr(755,root,root) %{_sbindir}/nattribute
%attr(755,root,root) %{_sbindir}/ncontext
%attr(755,root,root) %{_sbindir}/reducecap
%attr(755,root,root) %{_sbindir}/setattr
%attr(755,root,root) %{_sbindir}/showattr
%attr(755,root,root) %{_sbindir}/vattribute
%attr(755,root,root) %{_sbindir}/vcontext
%attr(755,root,root) %{_sbindir}/vdlimit
%attr(755,root,root) %{_sbindir}/vnamespace
%attr(755,root,root) %{_sbindir}/vkill
%attr(755,root,root) %{_sbindir}/vlimit
%attr(755,root,root) %{_sbindir}/vdevmap
%attr(755,root,root) %{_sbindir}/vdu
%attr(755,root,root) %{_sbindir}/vproc
%attr(755,root,root) %{_sbindir}/vps
%attr(755,root,root) %{_sbindir}/vpstree
%attr(755,root,root) %{_sbindir}/vrsetup
%attr(755,root,root) %{_sbindir}/vsched
%attr(755,root,root) %{_sbindir}/vserver
%attr(755,root,root) %{_sbindir}/vserver-info
%attr(755,root,root) %{_sbindir}/vserver-stat
%attr(755,root,root) %{_sbindir}/vsomething
%attr(755,root,root) %{_sbindir}/vtag
%attr(755,root,root) %{_sbindir}/vtop
%attr(755,root,root) %{_sbindir}/vuname
%attr(755,root,root) %{_sbindir}/vwait
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/defaults
%{_libdir}/%{name}/FEATURES.txt
%{_libdir}/%{name}/util-vserver-vars
%{_libdir}/%{name}/defaults/*
%attr(755,root,root) %{_libdir}/%{name}/capchroot
%attr(755,root,root) %{_libdir}/%{name}/chain-echo
%attr(755,root,root) %{_libdir}/%{name}/chbind-compat
%attr(755,root,root) %{_libdir}/%{name}/check-unixfile
%attr(755,root,root) %{_libdir}/%{name}/chcontext-compat
%attr(755,root,root) %{_libdir}/%{name}/chroot-sh
%attr(755,root,root) %{_libdir}/%{name}/exec-ulimit
%attr(755,root,root) %{_libdir}/%{name}/fakerunlevel
%attr(755,root,root) %{_libdir}/%{name}/filetime
%{_libdir}/%{name}/functions
%attr(755,root,root) %{_libdir}/%{name}/h2ext
%attr(755,root,root) %{_libdir}/%{name}/h2ext-worker
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
%{_libdir}/%{name}/vserver-setup.*
%attr(755,root,root) %{_libdir}/%{name}/vserver-build
%{_libdir}/%{name}/vserver-build.*
%attr(755,root,root) %{_libdir}/%{name}/vservers.grabinfo.sh
%attr(755,root,root) %{_libdir}/%{name}/vhashify
%attr(755,root,root) %{_libdir}/%{name}/vhashify.cron
%attr(755,root,root) %{_libdir}/%{name}/vshelper
%attr(755,root,root) %{_libdir}/%{name}/vshelper-sync
%attr(755,root,root) %{_libdir}/%{name}/vsysctl
%{_mandir}/man8/chbind.8*
%{_mandir}/man8/chcontext.8*
%{_mandir}/man8/reducecap.8*
%{_mandir}/man8/vps.8*
%{_mandir}/man8/vpstree.8*
%{_mandir}/man8/vserver-stat.8*
%{_mandir}/man8/vserver.8*
%{_mandir}/man8/vtop.8*
%attr(000,root,root) %dir /vservers
%dir /vservers/.pkg
%dir %{_localstatedir}/run/vservers
%dir %{_localstatedir}/run/vservers.rev
%dir %{_localstatedir}/run/vshelper
%dir /var/cache/vservers

%files lib
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%{?with_doc:%doc lib/apidoc/latex/refman.pdf lib/apidoc/html}
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/vserver*.h
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libvserver.a

%files build
%defattr(644,root,root,755)
%doc contrib/yum*.patch package-management.txt
%dir %{_sysconfdir}/vservers/.defaults/apps/vunify
%dir %{_sysconfdir}/vservers/.defaults/apps/vunify/hash
%dir %{_sysconfdir}/vservers/.distributions
%dir %{_sysconfdir}/vservers/.distributions/.common
%dir %{_sysconfdir}/vservers/.distributions/.common/pubkeys
%dir %{_sysconfdir}/vservers/.distributions/pld-ac
%dir %{_sysconfdir}/vservers/.distributions/pld-ac/poldek
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/vservers/.distributions/pld-ac/poldek/*.conf
%ifarch %{x8664}
%dir %{_sysconfdir}/vservers/.distributions/pld-ac-i686
%dir %{_sysconfdir}/vservers/.distributions/pld-ac-i686/poldek
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/vservers/.distributions/pld-ac-i686/poldek/*.conf
%dir %{_sysconfdir}/vservers/.distributions/pld-th-i686
%dir %{_sysconfdir}/vservers/.distributions/pld-th-i686/poldek
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/vservers/.distributions/pld-th-i686/poldek/*.conf
%endif
%dir %{_sysconfdir}/vservers/.distributions/pld-th
%dir %{_sysconfdir}/vservers/.distributions/pld-th/poldek
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/vservers/.distributions/pld-th/poldek/*.conf
%attr(755,root,root) %{_libdir}/%{name}/rpm-fake*
%dir %{_libdir}/%{name}/distributions
%attr(-,root,root) %{_libdir}/%{name}/distributions/defaults
%attr(-,root,root) %{_libdir}/%{name}/distributions/pld*
%dir %{_libdir}/%{name}/distributions/template
%attr(755,root,root) %{_libdir}/%{name}/distributions/template/init*
%attr(-,root,root) %{_libdir}/%{name}/distributions/redhat
%{_libdir}/%{name}/vserver-build.*
%{_libdir}/%{name}/vserver-setup.functions
%{_libdir}/%{name}/defaults/fstab
%{_libdir}/%{name}/defaults/debootstrap.uri
%{_libdir}/%{name}/defaults/vunify-exclude
%attr(755,root,root) %{_libdir}/%{name}/pkgmgmt
%attr(755,root,root) %{_libdir}/%{name}/vapt-get-worker
%attr(755,root,root) %{_libdir}/%{name}/vclone
%attr(755,root,root) %{_libdir}/%{name}/vcopy
%attr(755,root,root) %{_libdir}/%{name}/vpkg
%attr(755,root,root) %{_libdir}/%{name}/vpoldek-worker
%attr(755,root,root) %{_libdir}/%{name}/vrpm-*
%attr(755,root,root) %{_libdir}/%{name}/vserver-build
%attr(755,root,root) %{_libdir}/%{name}/vunify
%attr(755,root,root) %{_libdir}/%{name}/vyum-worker
%attr(755,root,root) %{_sbindir}/vapt-get
%attr(755,root,root) %{_sbindir}/vpoldek
%attr(755,root,root) %{_sbindir}/vrpm
%attr(755,root,root) %{_sbindir}/vyum

%files init
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/vsysvwrapper
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/vrootdevices
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/vservers
%config(noreplace) %verify(not md5 mtime size) /etc/cron.d/vservers
%attr(754,root,root) /etc/rc.d/init.d/vprocunhide
%attr(754,root,root) /etc/rc.d/init.d/vrootdevices
%attr(754,root,root) /etc/rc.d/init.d/vservers

%files legacy
%defattr(644,root,root,755)
%dir %{_sysconfdir}/vservices
%{_sysconfdir}/vservices/*
%dir %{_libdir}/%{name}/legacy
%attr(755,root,root) %{_libdir}/%{name}/legacy/*
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/vservers-legacy
%attr(754,root,root) /etc/rc.d/init.d/v_*
%attr(754,root,root) /etc/rc.d/init.d/rebootmgr
%attr(754,root,root) /etc/rc.d/init.d/vservers-legacy
%attr(755,root,root) %{_sbindir}/vserver-copy
%{_mandir}/man8/distrib-info.8*
%{_mandir}/man8/rebootmgr.8*
%{_mandir}/man8/vserver-copy.8*

%files -n vserver-distro-centos
%defattr(644,root,root,755)
%{_libdir}/util-vserver/distributions/centos*

%files -n vserver-distro-debian
%defattr(644,root,root,755)
%dir %{_libdir}/%{name}/distributions/debian
%{_libdir}/%{name}/distributions/debian/debootstrap.script
%attr(755,root,root) %{_libdir}/%{name}/distributions/debian/initpost
%{_libdir}/%{name}/distributions/etch
%{_libdir}/%{name}/distributions/lenny
%{_libdir}/%{name}/distributions/sid

%files -n vserver-distro-fedora
%defattr(644,root,root,755)
%dir %{_sysconfdir}/vservers/.distributions/f7
%dir %{_sysconfdir}/vservers/.distributions/f7/apt
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/vservers/.distributions/f7/apt/sources.list
%dir %{_sysconfdir}/vservers/.distributions/fc*
%dir %{_sysconfdir}/vservers/.distributions/fc*/apt
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/vservers/.distributions/fc*/apt/sources.list
%{_libdir}/%{name}/distributions/f7
%{_libdir}/%{name}/distributions/fc*

%files -n vserver-distro-gentoo
%defattr(644,root,root,755)
%dir %{_libdir}/util-vserver/distributions/gentoo
%attr(755,root,root) %{_libdir}/util-vserver/distributions/gentoo/*
%attr(755,root,root) %{_sbindir}/vdispatch-conf
%attr(755,root,root) %{_sbindir}/vemerge
%attr(755,root,root) %{_sbindir}/vesync
%attr(755,root,root) %{_sbindir}/vupdateworld

%files -n vserver-distro-redhat
%defattr(644,root,root,755)
%dir %{_sysconfdir}/vservers/.distributions/rh*
%dir %{_sysconfdir}/vservers/.distributions/rh*/apt
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/vservers/.distributions/rh*/apt/sources.list
%{_libdir}/%{name}/distributions/rh*

%files -n vserver-distro-suse
%defattr(644,root,root,755)
%dir %{_sysconfdir}/vservers/.distributions/suse*
%dir %{_sysconfdir}/vservers/.distributions/suse*/apt
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/vservers/.distributions/suse*/apt/sources.list
%{_libdir}/%{name}/distributions/suse*

%files -n vserver-distro-ubuntu
%defattr(644,root,root,755)
%{_libdir}/%{name}/distributions/breezy
%{_libdir}/%{name}/distributions/dapper
%{_libdir}/%{name}/distributions/edgy
%{_libdir}/%{name}/distributions/feisty
%{_libdir}/%{name}/distributions/gutsy
%{_libdir}/%{name}/distributions/hoary
%{_libdir}/%{name}/distributions/warty
