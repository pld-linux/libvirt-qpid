# TODO: PLDify init script
Summary:	Interface with libvirt using QMF
Summary(pl.UTF-8):	Interfejs libvirt wykorzystujący QMF
Name:		libvirt-qpid
Version:	0.2.12
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	ftp://libvirt.org/libvirt-qpid/%{name}-%{version}.tar.gz
# Source0-md5:	f42d560c3380e393fa9fee9b5d91011c
Patch0:		%{name}-build.patch
URL:		http://libvirt.org/CIM/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	libvirt-devel
BuildRequires:	libxml2-devel
BuildRequires:	qpid-cpp-devel
BuildRequires:	qpid-cpp-qmfgen
Requires:	libvirt
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libvirt-qpid provides an interface with libvirt using QMF (qpid
modelling framework) which utilizes the AMQP protocol. The Advanced
Message Queuing Protocol (AMQP) is an open standard application layer
protocol providing reliable transport of messages.

QMF provides a modeling framework layer on top of qpid (which
implements AMQP). This interface allows you to manage hosts, domains,
pools etc. as a set of objects with properties and methods.

%description -l pl.UTF-8
libvirt-qpid udostępnia interfejs libvirt wykorzystujący QMF (qpid
modelling framework - szkielet modelujący qpid), który wykorzystuje
protokół AMQP. AMQF (Advanced Message Queuing Protocol - zaawansowany
protokół kolejkowania komunikatów) to otwarty standard protokołu
warstwy aplikacji zapewniający wiarygodny transport komunikatów.

QMF udostępnia warstwę szkieletu modelującego ponad qpidem (który
implementuje AMQP). Interfejs ten pozwala na zarządzanie hostami,
domenami, pulami itp. jako zbiorami obiektów z właściwościami i
metodami.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS README TODO doc/*.html
%attr(755,root,root) %{_sbindir}/libvirt-qpid
%attr(754,root,root) /etc/rc.d/init.d/libvirt-qpid
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/libvirt-qpid
%dir %{_datadir}/libvirt-qpid
%{_datadir}/libvirt-qpid/libvirt-schema.xml
