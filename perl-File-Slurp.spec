Name: 		perl-File-Slurp
Version: 	9999.13
Release: 	7%{?dist}
Summary: 	Efficient Reading/Writing of Complete Files
License: 	GPL+ or Artistic
Group: 		Development/Libraries
URL: 		http://search.cpan.org/dist/File-Slurp/
Source0: 	http://www.cpan.org/modules/by-module/File/File-Slurp-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:  perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
BuildArch: noarch

BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Test::Pod::Coverage) >= 1.04
BuildRequires:	perl(Test::Pod) >= 1.14

%description
This module provides subs that allow you to read or write entire files with
one simple call. They are designed to be simple to use, have flexible ways
to pass in or get the file contents and to be very efficient. There is also
a sub to read in all the files in a directory other than . and ..

These slurp/spew subs work for files, pipes and sockets, and stdio, 
pseudo-files, and DATA.

%prep
%setup -q -n File-Slurp-%{version}
chmod 0644 lib/File/Slurp.pm extras/slurp_bench.pl
%{__perl} -pi -e 's|^#!/usr/local/bin/perl\b|#!%{__perl}|' extras/slurp_bench.pl

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*

%clean
rm -rf $RPM_BUILD_ROOT

%check
make test

%files
%defattr(-,root,root,-)
# For license text(s), see the perl package.
%doc Changes README extras/
%{perl_vendorlib}/File
%{_mandir}/man3/*

%changelog
* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 9999.13-7
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9999.13-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9999.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jul 09 2008 Ralf Corsépius <rc040203@freenet.de> - 9999.13-4
- Re-activate tests.

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 9999.13-3
- Rebuild for perl 5.10 (again)

* Thu Jan 24 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 9999.13-2
- disable tests, due to wacky Fedora builders

* Thu Jan 24 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 9999.13-1
- go to 9999.13 to fix build failures against perl 5.10.0

* Sun Jan 20 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 9999.12-4
- rebuild for new perl

* Sun Sep 02 2007 Ralf Corsépius <rc040203@freenet.de> - 9999.12-3
- Update license tag.
- BR: perl(ExtUtils::MakeMaker).

* Tue Sep 05 2006 Ralf Corsépius <rc040203@freenet.de> - 9999.12-2
- Mass rebuild.

* Sat Mar 18 2006 Ralf Corsépius <rc040203@freenet.de> - 9999.12-1
- Upstream update.

* Wed Mar 01 2006 Ralf Corsépius <rc040203@freenet.de> - 9999.11-2
- Rebuild for perl-5.8.8.

* Wed Feb 01 2006 Ralf Corsépius <rc040203@freenet.de> - 9999.11-1
- Upstream update.
- BR perl(Test::Pod), perl(Test::Pod::Coverage).
