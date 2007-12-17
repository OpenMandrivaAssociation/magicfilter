Summary:	Printer filters
Summary(pl):	Filtry dla drukarek
Name:		magicfilter
Version:	1.2
Release:	%mkrel 4
Group:		System/Configuration/Printing
License:	GPL
Source0:	ftp://sunsite.unc.edu/pub/Linux/system/printing/%{name}-%{version}.tar.gz
Patch0:		%{name}_1.2-28.diff.gz
Patch1:		%{name}-DESTDIR.patch
Patch2:		%{name}-hpdj.patch
BuildRequires:	a2ps
BuildRequires:	ghostscript
BuildRequires:	groff
BuildRequires:	gzip
BuildRequires:	libjpeg-progs
BuildRequires:	libtiff-progs
BuildRequires:	netpbm
BuildRequires:	tetex-dvips
BuildRequires:	transfig
BuildRequires:	sendmail-command
Requires:	a2ps
Requires:	ghostscript
Requires:	groff
Requires:	gzip
Requires:	libjpeg-progs
Requires:	libtiff-progs
Requires:	netpbm
Requires:	tetex-dvips
Requires:	transfig
Requires:	lpddaemon
Requires:	sendmail-command
Obsoletes:	apsfilter

%description
Magicfilter is a customizable, extensible automatic printer filter.

%description -l pl
Magicfilter jest konfigurowalnym i rozszerzalnym zbiorem filtrów dla
drukarek.

%prep
%setup -q
%patch0 -p1
%patch1 -p0
%patch2 -p1

%build
%configure

%make bindir=%{_sbindir}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8,%{_sysconfdir}/%{name}}

%makeinstall_std bindir=%{_sbindir} mandir=%_mandir/man8

install magicfilterconfig $RPM_BUILD_ROOT%{_sbindir}
install filters/*-filter $RPM_BUILD_ROOT%{_sysconfdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc QuickInst ChangeLog TODO
%dir %{_sysconfdir}/%{name}

%attr(755,root,root) %{_sbindir}/*
%attr(755,root,root) %config(noreplace) %{_sysconfdir}/%{name}/*
%{_mandir}/man*/*

