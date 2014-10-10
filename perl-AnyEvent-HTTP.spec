%define upstream_name    AnyEvent-HTTP
%define upstream_version 2.21

%if %{_use_internal_dependency_generator}
%define __noautoreq 'perl\\(Exporter(.*)\\)'
%else
%define _requires_exceptions Exporter::
%endif

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Simple but non-blocking HTTP/HTTPS client
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/AnyEvent/%{upstream_name}-%{upstream_version}.tar.gz

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
