#
# m68k and mips are the only not supported archs
#
# Conditional build:
%bcond_without	dietlibc		# don't use dietlibc (ask for troubles)
%bcond_without	doc			# don't build documentation which needed LaTeX
%bcond_without	no_dynamic_context	# disable enforcement of disabled dynamic context
%bcond_with	xalan			# use the xalan xslt processor
#
%define	vproc_version 0.01
# diet compile fails with ccache in %{__cc}
%undefine	with_ccache
#
%define		pre	r2844
#
Summary:	Linux virtual server utilities
Summary(pl.UTF-8):	Narzędzia dla linuksowych serwerów wirtualnych
Name:		util-vserver
Version:	0.30.216
Release:	0.%{pre}.1
License:	GPL
Group:		Applications/System
Source0:	%{name}-%{version}-%{pre}.tar.bz2
# Source0-md5:	e7a0b28e935bfce9f6db1dc5d93dc7b5
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
Source11:	http://www.13thfloor.at/vserver/s_release/v1.2.10/vproc-%{vproc_version}.tar.bz2
# Source11-md5:	1d030717bdbc958ea4b35fd2410dad85
Source12:	%{name}-vhashify.cron
Source13:	ftp://ftp.pld-linux.org/dists/ac/PLD-2.0-Ac-GPG-key.asc
# Source13-md5:	8e7574d1de2fa95c2c54cd2ee03364c1
Source14:	ftp://ftp.pld-linux.org/dists/th/PLD-3.0-Th-GPG-key.asc
# Source14-md5:	08b29584dd349aac9caa7610131a0a88
Source15:	%{name}.init
Patch0:		%{name}-vsysvwrapper.patch
Patch1:		%{name}-pld.patch
Patch2:		%{name}-centos.patch
Patch4:		%{name}-m4-diet.patch
Patch5:		%{name}-yum-verb-nogpg.patch
Patch6:		%{name}-build-umask.patch
Patch7:		%{name}-utmpx.patch
Patch8:		%{name}-vprocunhide.patch
Patch9:		%{name}-dev.patch
Patch10:	%{name}-no-dynamic-ctx.patch
Patch11:	%{name}-more-ip.patch
Patch12:	%{name}-rpm-fake-resolver-badperm-errorlogging.patch
Patch13:	%{name}-tmpdir.patch
Patch14:	%{name}-rpmpath.patch
Patch15:	%{name}-interfaces-ignore-cvs-dir.patch
Patch16:	%{name}-personalitymachine.patch
Patch17:	%{name}-backupfiles.patch
Patch18:	%{name}-vprocunhide-net.patch
# http://glen.alkohol.ee/pld/util-vserver-dbrebuild-internalize4.patch
Patch19:	%{name}-dbrebuild-internalize4.patch
Patch20:	%{name}-dev-stdfd.patch
Patch21:	%{name}-bash-wrapper.patch
Patch22:	%{name}-pivot-root-ugly-hack.patch
Patch23:	%{name}-ac.patch
URL:		http://savannah.nongnu.org/projects/util-vserver/
BuildRequires:	autoconf
BuildRequires:	automake >= 1.9
BuildRequires:	beecrypt-devel
BuildRequires:	ctags
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
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	tetex-format-pdflatex
BuildRequires:	tetex-makeindex
# To be removed when tetex-format-pdflatex, tetex-pdftex...
# ...and graphviz packages get fixed
BuildRequires:	ghostscript
BuildRequires:	ghostscript-fonts-std
%if "%{pld_release}" == "ti"
BuildRequires:	tetex-fonts-jknappen
BuildRequires:	tetex-metafont
%else
BuildRequires:	texlive-fonts-type1-urw
BuildRequires:	texlive-format-pdflatex
BuildRequires:	texlive-makeindex
BuildRequires:	texlive-pdftex
BuildRequires:	texlive-xetex
%endif
%{?with_xalan:BuildRequires:	xalan-j}
%endif
Requires(post,preun):	/sbin/chkconfig
Requires:	%{name}-lib = %{version}-%{release}
Requires:	coreutils
Requires:	diffutils
Requires:	issue
Requires:	make
Requires:	mktemp >= 1.5-18
Requires:	rc-scripts
Requires:	tar
Requires:	util-linux
Requires:	vserver-distro-pld = %{version}-%{release}
Conflicts:	poldek < 0.18.8-10
Obsoletes:	util-vserver-build
Obsoletes:	util-vserver-core
Obsoletes:	util-vserver-init
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%if %{with dietlibc}
# binaries created with this option have broken segments when using dietlibc
%define	filterout_ld	-Wl,-z,relro
%endif

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
the Linux-Vserver enabled kernel, utilities which assist in building
Vservers and SysV initscripts which start and stop Vservers and related
tools.

%description -l pl.UTF-8
Ten pakiet dostarcza składniki i szkielet do tworzenia wirtualnych
serwerów. Wirtualny serwer działa wewnątrz serwera linuksowego, lecz
jest od niego w dużym stopniu niezależny. Jako taki może uruchamiać
różne usługi z normalną konfiguracją. Różne vserwery nie mogą wchodzić
w interakcję z innymi ani z usługami na głównym serwerze.

Wymaga to specjalnego jądra obsługującego nowe wywołania systemowe
new_s_context i set_ipv4root.

Ten pakiet zawiera narzędzia wymagane do komunikacji z jądrem z
włączonym mechanizmem Linux-Vserver, narzędzia pomagające przy
budowaniu Vserwerów i skrypty inicjalizujące SysV uruchamiające i
zatrzymujące Vserwery oraz powiązane narzędzia.

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

%package -n python-util-vserver
Summary:	Python interface to libutil-vserver library
Summary(pl.UTF-8):	Pythonowy interfejs do biblioteki libutil-vserver
License:	LGPL v2.1+
Group:		Libraries/Python

%description -n python-util-vserver
Python interface to libutil-vserver library.

%description -n python-util-vserver -l pl.UTF-8
Pythonowy interfejs do biblioteki libutil-vserver.

%package -n vserver-distro-alpine
Summary:	VServer build template for Alpine Linux
Summary(pl.UTF-8):	Szablon budowania VServerów dla dystrybucji Alpine Linux
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}

%description -n vserver-distro-alpine
VServer build template for Alpine Linux.

%description -n vserver-distro-alpine -l pl.UTF-8
Szablon budowania VServerów dla dystrybucji Alpine Linux.

%package -n vserver-distro-centos
Summary:	VServer build template for CentOS
Summary(pl.UTF-8):	Szablon budowania VServerów dla dystrybucji CentOS
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}
Requires:	vserver-distro-redhat = %{version}-%{release}
Requires:	yum

%description -n vserver-distro-centos
VServer build template for CentOS 4.2 and 5.

%description -n vserver-distro-centos -l pl.UTF-8
Szablon budowania VServerów dla dystrybucji CentOS 4.2 i 5.

%package -n vserver-distro-debian
Summary:	VServer build templates for Debian and Ubuntu
Summary(pl.UTF-8):	Szablony do tworzenia VServerów dla dystrybucji Debian i Ubuntu
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}
Requires:	debootstrap
Requires:	dpkg
Obsoletes:	vserver-distro-ubuntu

%description -n vserver-distro-debian
VServer build templates for Debian.

%description -n vserver-distro-debian -l pl.UTF-8
Szablony do tworzenia VServerów dla dystrybucji Debian.

%package -n vserver-distro-fedora
Summary:	VServer build templates for Fedora
Summary(pl.UTF-8):	Szablony do tworzenia VServerów dla dystrybucji Fedora
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}
Requires:	binutils
Requires:	e2fsprogs
Requires:	rpm
Requires:	wget
Requires:	vserver-distro-redhat = %{version}-%{release}
Requires:	yum

%description -n vserver-distro-fedora
VServer build templates for Fedora Core 1,2,3,4,5,6 and Fedora 7.

%description -n vserver-distro-fedora -l pl.UTF-8
Szablony do tworzenia VServerów dla dystrybucji Fedora Core
1,2,3,4,5,6 oraz Fedora 7.

%package -n vserver-distro-gentoo
Summary:	VServer build template for Gentoo
Summary(pl.UTF-8):	Szablon budowania VServerów dla Gentoo
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}

%description -n vserver-distro-gentoo
VServer build template for Gentoo.

%description -n vserver-distro-gentoo -l pl.UTF-8
Szablon budowania VServerów dla Gentoo.

%package -n vserver-distro-pld
Summary:	VServer build templates for PLD Linux
Summary(pl.UTF-8):	Szablony do tworzenia VServerów dla dystrybucji PLD Linux
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}
Requires:	/etc/pld-release
Requires:	poldek >= 0.30

%description -n vserver-distro-pld
VServer build templates for PLD Linux.

%description -n vserver-distro-pld -l pl.UTF-8
Szablony do tworzenia VServerów dla dystrybucji PLD Linux.

%package -n vserver-distro-redhat
Summary:	VServer build template for Red Hat Linux 9
Summary(pl.UTF-8):	Szablon do tworzenia VServerów dla dystrybucji Red Hat Linux 9
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}
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
Requires:	%{name} = %{version}-%{release}
Requires:	binutils
Requires:	e2fsprogs
Requires:	rpm
Requires:	wget

%description -n vserver-distro-suse
VServer build template for SuSE Linux 9.1.

%description -n vserver-distro-suse -l pl.UTF-8
Szablon do tworzenia VServerów dla dystrybucji SuSE 9.1.

%prep
%setup -q -n %{name}-%{version}-%{pre} -a11
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%{?with_no_dynamic_context:%patch10 -p1}
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p0

install %{SOURCE9} package-management.txt

%build
unset LD_SYMBOLIC_FUNCTIONS || :

%if %{with dietlibc}
CFLAGS="%{rpmcflags} -D__GLIBC__ -D__KERNEL_STRICT_NAMES=1 -U__STRICT_ANSI__"
%endif
%{__libtoolize}
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

%{__make} -C vproc-%{vproc_version} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/vservers/.pkg,/etc/{sysconfig,rc.d/init.d,cron.d}} \
	$RPM_BUILD_ROOT%{_sysconfdir}/vservices \
	$RPM_BUILD_ROOT%{_sysconfdir}/vservers/.defaults/apps/vdevmap

%{__make} -j1 install install-distribution \
	DESTDIR=$RPM_BUILD_ROOT

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
sed 's|%{_usrlib}/util-vserver|%{_libdir}/%{name}|g' %{SOURCE15} > \
	$RPM_BUILD_ROOT/etc/rc.d/init.d/util-vserver
sed 's|%{_usrlib}/util-vserver|%{_libdir}/%{name}|g' %{SOURCE5} > \
	$RPM_BUILD_ROOT/etc/sysconfig/vservers
sed 's|%{_usrlib}/util-vserver|%{_libdir}/%{name}|g' gentoo/bash-wrapper > \
	$RPM_BUILD_ROOT%{_libdir}/%{name}/bash-wrapper

install %{SOURCE6} $RPM_BUILD_ROOT/etc/sysconfig/vservers-legacy

install %{SOURCE7} $RPM_BUILD_ROOT/etc/rc.d/init.d/vrootdevices
install %{SOURCE8} $RPM_BUILD_ROOT/etc/sysconfig/vrootdevices
install -d $RPM_BUILD_ROOT%{_libdir}/%{name}/distributions/pld
install %{SOURCE10} $RPM_BUILD_ROOT%{_libdir}/%{name}/distributions/pld/initpost
ln -s ../pld/initpost $RPM_BUILD_ROOT%{_libdir}/%{name}/distributions/pld-ac/initpost
ln -s ../pld/initpost $RPM_BUILD_ROOT%{_libdir}/%{name}/distributions/pld-th/initpost
%ifarch i586 i686 %{x8664} athlon pentium2 pentium3 pentium4
ln -s ../pld/initpost $RPM_BUILD_ROOT%{_libdir}/%{name}/distributions/pld-ti/initpost
%endif
install vproc-%{vproc_version}/vproc $RPM_BUILD_ROOT%{_sbindir}
install %{SOURCE12} $RPM_BUILD_ROOT%{_libdir}/%{name}/vhashify.cron

cat > $RPM_BUILD_ROOT/etc/cron.d/vservers << EOF
02 2 * * 0      root    %{_libdir}/%{name}/vhashify.cron
EOF

install -d $RPM_BUILD_ROOT%{_libdir}/%{name}/distributions/pld-ac/pubkeys
cp -a %{SOURCE13} $RPM_BUILD_ROOT%{_libdir}/%{name}/distributions/pld-ac/pubkeys/pld-ac.asc

install -d $RPM_BUILD_ROOT%{_libdir}/%{name}/distributions/pld-th/pubkeys
cp -a %{SOURCE14} $RPM_BUILD_ROOT%{_libdir}/%{name}/distributions/pld-th/pubkeys/pld-th.asc

# set arch for pld-ac in pld.conf
%ifarch i586 i686 ppc sparc alpha athlon
%define		ftp_arch	%{_target_cpu}
%endif
%ifarch %{x8664}
%define		ftp_arch	amd64
%endif
%ifarch i486
%define		ftp_arch	i386
%endif
%ifarch pentium2 pentium3 pentium4
%define		ftp_arch	i686
%endif
%ifarch sparcv9 sparc64
%define		ftp_arch	sparc
%endif
%{__sed} -i -e 's|%%ARCH%%|%{ftp_arch}|' $RPM_BUILD_ROOT%{_sysconfdir}/vservers/.distributions/pld-ac/poldek/repos.d/pld.conf

# set arch for pld-th in pld.conf
%ifarch i486 i686 ppc sparc alpha athlon
%define		ftp_arch	%{_target_cpu}
%endif
%ifarch %{x8664}
%define		ftp_arch	x86_64
%endif
%ifarch i586
%define		ftp_arch	i486
%endif
%ifarch pentium2 pentium3 pentium4
%define		ftp_arch	i686
%endif
%ifarch sparcv9 sparc64
%define		ftp_arch	sparc
%endif
%{__sed} -i -e 's|%%ARCH%%|%{ftp_arch}|' $RPM_BUILD_ROOT%{_sysconfdir}/vservers/.distributions/pld-th/poldek/repos.d/pld.conf

%ifarch i586 i686 %{x8664} athlon pentium2 pentium3 pentium4
# set arch for pld-ti in pld.conf
%ifarch i586 i686
%define		ftp_arch	%{_target_cpu}
%endif
%ifarch %{x8664}
%define		ftp_arch	x86_64
%endif
%ifarch athlon pentium2 pentium3 pentium4
%define		ftp_arch	i686
%endif
%{__sed} -i -e 's|%%ARCH%%|%{ftp_arch}|' $RPM_BUILD_ROOT%{_sysconfdir}/vservers/.distributions/pld-ti/poldek/repos.d/pld.conf
%endif

# current debootstrap link
echo "http://ftp.debian.org/debian/pool/main/d/debootstrap/debootstrap_1.0.10_all.deb" \
	> $RPM_BUILD_ROOT%{_libdir}/%{name}/defaults/debootstrap.uri

install -d $RPM_BUILD_ROOT/var/cache/vservers/poldek

# we have our own initscript which does the same
rm -rf $RPM_BUILD_ROOT/dev
rm -f $RPM_BUILD_ROOT%{_libdir}/util-vserver/vserver-wrapper
rm -f $RPM_BUILD_ROOT%{_libdir}/util-vserver/vserver-init.functions
rm -f $RPM_BUILD_ROOT/etc/rc.d/init.d/vservers-default
rm -f $RPM_BUILD_ROOT%{_sysconfdir}/vservers.conf

%clean
rm -rf $RPM_BUILD_ROOT

%triggerun -- util-vserver-init
# Prevent preun from util-vserver-init from working
chmod a-x /etc/rc.d/init.d/vprocunhide
chmod a-x /etc/rc.d/init.d/vrootdevices
chmod a-x /etc/rc.d/init.d/vservers

%triggerpostun -- util-vserver-init
# Restore what triggerun removed
chmod ug+x /etc/rc.d/init.d/vprocunhide
chmod ug+x /etc/rc.d/init.d/vrootdevices
chmod ug+x /etc/rc.d/init.d/vservers
/sbin/chkconfig --add vrootdevices
/sbin/chkconfig --add vprocunhide
/sbin/chkconfig --add vservers
if [ -f /etc/sysconfig/vrootdevices.rpmsave ]; then
	cp -f /etc/sysconfig/vrootdevices{,.rpmnew}
	mv -f /etc/sysconfig/vrootdevices{.rpmsave,}
fi
if [ -f /etc/sysconfig/vservers.rpmsave ]; then
	cp -f /etc/sysconfig/vservers{,.rpmnew}
	mv -f /etc/sysconfig/vservers{.rpmsave,}
fi

%post
%{_sbindir}/setattr --barrier /vservers || :
/sbin/chkconfig --add util-vserver
/sbin/chkconfig --add vrootdevices
/sbin/chkconfig --add vprocunhide
/sbin/chkconfig --add vservers
if [ ! -f /var/lock/subsys/util-vserver ]; then
	echo "Type \"/sbin/service util-vserver start\" to set up vshelper path" 1>&2
fi
if [ ! -f /var/lock/subsys/vrootdevices ]; then
	echo "Type \"/sbin/service vrootdevices start\" to assign virtual root devices" 1>&2
fi
if [ ! -f /var/lock/subsys/vprocunhide ]; then
	echo "Type \"/sbin/service vprocunhide start\" to set /proc visibility for vservers" 1>&2
fi
if [ ! -f /var/lock/subsys/vservers ]; then
	echo "Type \"/sbin/service vservers start\" to start vservers" 1>&2
fi

%preun
if [ "$1" = "0" ]; then
	%service util-vserver stop
	%service vservers stop
	%service vprocunhide stop
	%service vrootdevices stop
	/sbin/chkconfig --del util-vserver
	/sbin/chkconfig --del vservers
	/sbin/chkconfig --del vprocunhide
	/sbin/chkconfig --del vrootdevices
fi

%post	lib -p /sbin/ldconfig
%postun	lib -p /sbin/ldconfig

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

%triggerpostun -n vserver-distro-pld -- util-vserver-build < 0.30.215-1.1
for D in ac th ti; do
	P=%{_sysconfdir}/vservers/.distributions/pld-$D/poldek

	if [ -f $P/pld-source.conf.rpmsave ]; then
		cp -f $P/repos.d/pld.conf{,.rpmnew}
		mv -f $P/pld-source.conf.rpmsave $P/repos.d/pld.conf
	fi
done
exit 0

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS THANKS doc/intro.txt
%doc contrib/yum*.patch package-management.txt
%{?with_doc:%doc doc/*.html}
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/vrootdevices
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/vservers
%config(noreplace) %verify(not md5 mtime size) /etc/cron.d/vservers
%attr(754,root,root) /etc/rc.d/init.d/vprocunhide
%attr(754,root,root) /etc/rc.d/init.d/vrootdevices
%attr(754,root,root) /etc/rc.d/init.d/util-vserver
%attr(754,root,root) /etc/rc.d/init.d/vservers
%dir %{_sysconfdir}/vservers
%dir %{_sysconfdir}/vservers/.defaults
%dir %{_sysconfdir}/vservers/.defaults/apps
%dir %{_sysconfdir}/vservers/.defaults/apps/vdevmap
%dir %{_sysconfdir}/vservers/.defaults/apps/vunify
%dir %{_sysconfdir}/vservers/.defaults/apps/vunify/hash
%dir %{_sysconfdir}/vservers/.defaults/files
%{_sysconfdir}/vservers/.defaults/vdirbase
%{_sysconfdir}/vservers/.defaults/cachebase
%{_sysconfdir}/vservers/.defaults/run.rev
%dir %{_sysconfdir}/vservers/.distributions
%dir %{_sysconfdir}/vservers/.distributions/.common
%dir %{_sysconfdir}/vservers/.distributions/.common/pubkeys
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
%attr(755,root,root) %{_sbindir}/vapt-get
%attr(755,root,root) %{_sbindir}/vattribute
%attr(755,root,root) %{_sbindir}/vcontext
%attr(755,root,root) %{_sbindir}/vdevmap
%attr(755,root,root) %{_sbindir}/vdlimit
%attr(755,root,root) %{_sbindir}/vdu
%attr(755,root,root) %{_sbindir}/vkill
%attr(755,root,root) %{_sbindir}/vlimit
%attr(755,root,root) %{_sbindir}/vmemctrl
%attr(755,root,root) %{_sbindir}/vmount
%attr(755,root,root) %{_sbindir}/vnamespace
%attr(755,root,root) %{_sbindir}/vpoldek
%attr(755,root,root) %{_sbindir}/vproc
%attr(755,root,root) %{_sbindir}/vps
%attr(755,root,root) %{_sbindir}/vpstree
%attr(755,root,root) %{_sbindir}/vrpm
%attr(755,root,root) %{_sbindir}/vrsetup
%attr(755,root,root) %{_sbindir}/vsched
%attr(755,root,root) %{_sbindir}/vserver
%attr(755,root,root) %{_sbindir}/vserver-info
%attr(755,root,root) %{_sbindir}/vserver-stat
%attr(755,root,root) %{_sbindir}/vsomething
%attr(755,root,root) %{_sbindir}/vspace
%attr(755,root,root) %{_sbindir}/vtag
%attr(755,root,root) %{_sbindir}/vtop
%attr(755,root,root) %{_sbindir}/vuname
%attr(755,root,root) %{_sbindir}/vwait
%attr(755,root,root) %{_sbindir}/vyum
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/defaults
%{_libdir}/%{name}/defaults/fstab
%{_libdir}/%{name}/defaults/debootstrap.*
%{_libdir}/%{name}/defaults/vunify-exclude
%{_libdir}/%{name}/defaults/context.start
%{_libdir}/%{name}/defaults/environment
%{_libdir}/%{name}/defaults/h2ext.desc
%{_libdir}/%{name}/defaults/mtab
%{_libdir}/%{name}/defaults/vprocunhide-files
%dir %{_libdir}/%{name}/distributions
%{_libdir}/%{name}/distributions/defaults
%dir %{_libdir}/%{name}/distributions/template
%attr(755,root,root) %{_libdir}/%{name}/distributions/template/initpost
%attr(755,root,root) %{_libdir}/%{name}/distributions/template/initpre
%dir %{_libdir}/%{name}/distributions/redhat
%attr(755,root,root) %{_libdir}/%{name}/distributions/redhat/initpost
%attr(755,root,root) %{_libdir}/%{name}/distributions/redhat/initpre
%attr(755,root,root) %{_libdir}/%{name}/distributions/redhat/rc.sysinit
%{_libdir}/%{name}/FEATURES.txt
%{_libdir}/%{name}/util-vserver-vars
%attr(755,root,root) %{_libdir}/%{name}/bash-wrapper
%attr(755,root,root) %{_libdir}/%{name}/capchroot
%attr(755,root,root) %{_libdir}/%{name}/chain-echo
%attr(755,root,root) %{_libdir}/%{name}/chbind-compat
%attr(755,root,root) %{_libdir}/%{name}/chcontext-compat
%attr(755,root,root) %{_libdir}/%{name}/check-unixfile
%attr(755,root,root) %{_libdir}/%{name}/chroot-sh
%attr(755,root,root) %{_libdir}/%{name}/exec-remount
%attr(755,root,root) %{_libdir}/%{name}/exec-ulimit
%attr(755,root,root) %{_libdir}/%{name}/fakerunlevel
%attr(755,root,root) %{_libdir}/%{name}/filetime
%{_libdir}/%{name}/functions
%attr(755,root,root) %{_libdir}/%{name}/h2ext
%attr(755,root,root) %{_libdir}/%{name}/h2ext-worker
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
%attr(755,root,root) %{_libdir}/%{name}/tunctl
%attr(755,root,root) %{_libdir}/%{name}/vapt-get-worker
%attr(755,root,root) %{_libdir}/%{name}/vclone
%attr(755,root,root) %{_libdir}/%{name}/vcopy
%attr(755,root,root) %{_libdir}/%{name}/vhashify
%attr(755,root,root) %{_libdir}/%{name}/vhashify.cron
%attr(755,root,root) %{_libdir}/%{name}/vpkg
%attr(755,root,root) %{_libdir}/%{name}/vpoldek-worker
%attr(755,root,root) %{_libdir}/%{name}/vprocunhide
%attr(755,root,root) %{_libdir}/%{name}/vrpm-*
%attr(755,root,root) %{_libdir}/%{name}/vserver-build
%{_libdir}/%{name}/vserver-build.*
%{_libdir}/%{name}/vserver-setup.functions
%{_libdir}/%{name}/vserver.*
%attr(755,root,root) %{_libdir}/%{name}/vservers.grabinfo.sh
%attr(755,root,root) %{_libdir}/%{name}/vshelper
%attr(755,root,root) %{_libdir}/%{name}/vshelper-sync
%attr(755,root,root) %{_libdir}/%{name}/vsysctl
%attr(755,root,root) %{_libdir}/%{name}/vsysvwrapper
%attr(755,root,root) %{_libdir}/%{name}/vunify
%attr(755,root,root) %{_libdir}/%{name}/vyum-worker
%{_mandir}/man8/chbind.8*
%{_mandir}/man8/chcontext.8*
%{_mandir}/man8/reducecap.8*
%{_mandir}/man8/vps.8*
%{_mandir}/man8/vpstree.8*
%{_mandir}/man8/vserver-build.8*
%{_mandir}/man8/vserver-stat.8*
%{_mandir}/man8/vserver.8*
%{_mandir}/man8/vtop.8*
%attr(000,root,root) %dir /vservers
%dir /vservers/.pkg
%dir %{_localstatedir}/run/vservers
%dir %{_localstatedir}/run/vservers.rev
%dir %{_localstatedir}/run/vshelper
%dir /var/cache/vservers
%dir /var/cache/vservers/poldek

%files lib
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libvserver.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libvserver.so.0

%files devel
%defattr(644,root,root,755)
%{?with_doc:%doc lib/apidoc/latex/refman.pdf lib/apidoc/html}
%attr(755,root,root) %{_libdir}/libvserver.so
%{_libdir}/lib*.la
%{_includedir}/vserver*.h
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libvserver.a

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

%files -n python-util-vserver
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/_libvserver.so

%files -n vserver-distro-alpine
%defattr(644,root,root,755)
%dir %{_libdir}/%{name}/distributions/alpine
%attr(755,root,root) %{_libdir}/%{name}/distributions/alpine/initpost
%attr(755,root,root) %{_libdir}/%{name}/distributions/alpine/initpre

%files -n vserver-distro-centos
%defattr(644,root,root,755)
%{_libdir}/util-vserver/distributions/centos*

%files -n vserver-distro-debian
%defattr(644,root,root,755)
%dir %{_libdir}/%{name}/distributions/debian
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
%{_libdir}/%{name}/distributions/f8
%{_libdir}/%{name}/distributions/f9
%{_libdir}/%{name}/distributions/f10
%{_libdir}/%{name}/distributions/f11
%{_libdir}/%{name}/distributions/fc*

%files -n vserver-distro-gentoo
%defattr(644,root,root,755)
%dir %{_libdir}/util-vserver/distributions/gentoo
%attr(755,root,root) %{_libdir}/util-vserver/distributions/gentoo/*
%attr(755,root,root) %{_sbindir}/vdispatch-conf
%attr(755,root,root) %{_sbindir}/vemerge
%attr(755,root,root) %{_sbindir}/vesync
%attr(755,root,root) %{_sbindir}/vupdateworld

%files -n vserver-distro-pld
%defattr(644,root,root,755)
%dir %{_libdir}/%{name}/distributions/pld
%attr(755,root,root) %{_libdir}/%{name}/distributions/pld/initpost
%dir %{_libdir}/%{name}/distributions/pld-*
%{_libdir}/%{name}/distributions/pld-*/pkgs
%{_libdir}/%{name}/distributions/pld-*/pubkeys
%{_libdir}/%{name}/distributions/pld-*/rpm
%attr(755,root,root) %{_libdir}/%{name}/distributions/pld-*/initpost
%dir %{_sysconfdir}/vservers/.distributions/pld-ac
%dir %{_sysconfdir}/vservers/.distributions/pld-ac/poldek
%dir %{_sysconfdir}/vservers/.distributions/pld-ac/poldek/repos.d
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/vservers/.distributions/pld-ac/poldek/repos.d/*.conf
%dir %{_sysconfdir}/vservers/.distributions/pld-th
%dir %{_sysconfdir}/vservers/.distributions/pld-th/poldek
%dir %{_sysconfdir}/vservers/.distributions/pld-th/poldek/repos.d
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/vservers/.distributions/pld-th/poldek/repos.d/*.conf
%ifarch i586 i686 %{x8664} athlon pentium2 pentium3 pentium4
%dir %{_sysconfdir}/vservers/.distributions/pld-ti
%dir %{_sysconfdir}/vservers/.distributions/pld-ti/poldek
%dir %{_sysconfdir}/vservers/.distributions/pld-ti/poldek/repos.d
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/vservers/.distributions/pld-ti/poldek/repos.d/*.conf
%endif

%files -n vserver-distro-redhat
%defattr(644,root,root,755)
%dir %{_sysconfdir}/vservers/.distributions/rh9
%dir %{_sysconfdir}/vservers/.distributions/rh9/apt
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/vservers/.distributions/rh*/apt/sources.list
%{_libdir}/%{name}/distributions/rh9
%dir %{_libdir}/%{name}/distributions/redhat
%attr(755,root,root) %{_libdir}/%{name}/distributions/redhat/initctl
%attr(755,root,root) %{_libdir}/%{name}/distributions/redhat/initpost
%attr(755,root,root) %{_libdir}/%{name}/distributions/redhat/initpre
%attr(755,root,root) %{_libdir}/%{name}/distributions/redhat/rc.sysinit

%files -n vserver-distro-suse
%defattr(644,root,root,755)
%dir %{_sysconfdir}/vservers/.distributions/suse*
%dir %{_sysconfdir}/vservers/.distributions/suse*/apt
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/vservers/.distributions/suse*/apt/sources.list
%{_libdir}/%{name}/distributions/suse*
