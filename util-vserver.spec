Summary:	Linux virtual server utilities
Summary(pl):	Narzêdzia dla linuksowych serwerów wirtualnych
Name:		util-vserver
Version:	0.24
Release:	1
Epoch:		0
License:	GPL
Group:		Base
Source0:	http://savannah.nongnu.org/download/util-vserver/stable.pkg/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	625d6c9bc5a4d2e44eafdf0f619c2153
URL:		http://savannah.nongnu.org/projects/util-vserver/
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

%prep
%setup -q

%build
%configure \
	--with-kerneldir=%{_kernelsrcdir}
%{__make}


%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%define v_services	httpd named portmap sendmail smb sshd xinetd
%post
/sbin/chkconfig --add vservers
/sbin/chkconfig --add rebootmgr

for i in %{v_services}; do
	/sbin/chkconfig --add v_$i
done

%preun
test "$1" != 0 || for i in %{v_services}; do
	/sbin/chkconfig --del v_$i
done

test "$1" != 0 || %{_initrddir}/rebootmgr stop >&2 || :
test "$1" != 0 || /sbin/chkconfig --del rebootmgr
test "$1" != 0 || /sbin/chkconfig --del vservers

%postun
test "$1" = 0  || %{_initrddir}/rebootmgr condrestart >&2 || :

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README THANKS
%doc doc/FAQ.txt
%attr(755,root,root) %{_sbindir}/*
%{_libdir}/%{name}
%{_includedir}/vserver.h
%{_libdir}/libvserver.a
%{_mandir}/man8/*
%attr(754,root,root) /etc/rc.d/init.d/*
%config(noreplace) %{_sysconfdir}/vservers.conf
%attr(0,root,root) %dir /vservers
%exclude %{_sbindir}/newvserver
%exclude %{_mandir}/man8/newvserver*
