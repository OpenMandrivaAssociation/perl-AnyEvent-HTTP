%define upstream_name    AnyEvent-HTTP
%define upstream_version 2.15

%if %{_use_internal_dependency_generator}
%define __noautoreq 'perl\\(Exporter(.*)\\)'
%else
%define _requires_exceptions Exporter::
%endif

Name:		perl-%{upstream_name}
Version:	%perl_convert_version 2.15
Release:	1

Summary:	Simple but non-blocking HTTP/HTTPS client
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/AnyEvent/AnyEvent-HTTP-2.15.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(AnyEvent)
BuildRequires:	perl(common::sense)
BuildArch:	noarch

%description
This module is an AnyEvent user, you need to make sure that you
use and run a supported event loop.

This module implements a simple, stateless and non-blocking HTTP client. It
supports GET, POST and other request methods, cookies and more, all on a
very low level. It can follow redirects, supports proxies and automatically
limits the number of connections to the values specified in the RFC.

It should generally be a "good client" that is enough for most HTTP tasks.
Simple tasks should be simple, but complex tasks should still be possible
as the user retains control over request and response headers.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Wed Jun 15 2011 Guillaume Rousse <guillomovitch@mandriva.org> 2.120.0-1mdv2011.0
+ Revision: 685306
- update to new version 2.12

* Thu May 12 2011 Guillaume Rousse <guillomovitch@mandriva.org> 2.110.0-1
+ Revision: 673782
- update to new version 2.11

* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 2.100.0-2
+ Revision: 657381
- rebuild for updated spec-helper

* Wed Mar 02 2011 Guillaume Rousse <guillomovitch@mandriva.org> 2.100.0-1
+ Revision: 641314
- update to new version 2.1

* Mon Feb 28 2011 Funda Wang <fwang@mandriva.org> 2.40.0-2
+ Revision: 640752
- rebuild to obsolete old packages

* Sun Feb 20 2011 Guillaume Rousse <guillomovitch@mandriva.org> 2.40.0-1
+ Revision: 638892
- update to new version 2.04

* Sun Jan 30 2011 Guillaume Rousse <guillomovitch@mandriva.org> 2.30.0-1
+ Revision: 634187
- update to new version 2.03

* Wed Jan 05 2011 Guillaume Rousse <guillomovitch@mandriva.org> 2.0.0-1mdv2011.0
+ Revision: 628754
- update to new version 2.0

* Fri Dec 31 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.500.0-1mdv2011.0
+ Revision: 626816
- update to new version 1.5

* Sat Dec 25 2010 Shlomi Fish <shlomif@mandriva.org> 1.460.0-1mdv2011.0
+ Revision: 624763
- import perl-AnyEvent-HTTP


