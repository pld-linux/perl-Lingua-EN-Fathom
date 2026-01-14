#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Lingua
%define		pnam	EN-Fathom
Summary:	Lingua::EN::Fathom - Measure readability of English text
Summary(pl.UTF-8):	Lingua::EN::Fathom - określanie czytelności tekstu angielskiego
Name:		perl-Lingua-EN-Fathom
Version:	1.15
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Lingua/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	94bd7ecf1f9b460fb090f478a39acdfd
URL:		http://search.cpan.org/dist/Lingua-EN-Fathom/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Lingua-EN-Syllable
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module analyses English text in either a string or file. Totals
are then calculated for the number of characters, words, sentences,
blank and non blank (text) lines and paragraphs.

Three common readability statistics are also derived, the Fog, Flesch
and Kincaid indices.

All of these properties can be accessed through individual methods, or
by generating a text report.

A hash of all unique words and the number of times they occur is
generated.

%description -l pl.UTF-8
Ten moduł analizuje tekst angielski pochodzący z łańcucha znaków lub
pliku. Następnie wylicza podsumowanie liczby znaków, słów, zdań oraz
pustych i niepustych (zawierających tekst) wierszy oraz akapitów.

Liczone są także trzy popularne statystyki czytelności: Foga, Flescha
oraz Kincaida.

Wszystkie te właściwości można odczytywać poprzez osobne metody lub
generując raport tekstowy.

Generowany jest także hasz wszystkich unikalnych słów oraz liczby ich
wystąpień.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%{__perl} -pi -e 's,/usr/local/bin/perl,/usr/bin/perl,' examples/*.pl

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/*.pl $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Lingua/EN/Fathom.pm
%{_mandir}/man3/Lingua::EN::Fathom.3pm*
%dir %{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/*.pl
