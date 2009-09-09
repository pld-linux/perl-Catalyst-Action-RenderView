#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Catalyst
%define	pnam	Action-RenderView
Summary:	Catalyst::Action::RenderView - sensible default end action
Summary(pl.UTF-8):	Catalyst::Action::RenderView - sensowna domyślna akcja końcowa
Name:		perl-Catalyst-Action-RenderView
Version:	0.11
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Catalyst/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	6231f873a1ad77dc22815eacf1b88976
URL:		http://search.cpan.org/dist/Catalyst-Action-RenderView/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Catalyst >= 5.7
BuildRequires:	perl-Data-Visitor >= 0.08
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This action implements a sensible default end action, which will
forward to the first available view, unless status is set to 3xx, or
there is a response body. It also allows you to pass dump_info=1 to
the URL in order to force a debug screen, while in debug mode.

If you have more than one view, you can specify which one to use with
the default_view config setting.

%description -l pl.UTF-8
Ta akcja implementuje sensowną domyślną akcję końcową, przekazującą
pierwszy dostępny widok, chyba że status jest ustawiony na 3xx lub
nie ma ciała odpowiedzi. Pozwala także przekazać dump_info=1 do
URL-a, aby wymusić ekran śledzenia w przypadku trybu śledzenia.

Jeśli jest więcej niż jeden widok, można podać który ma być
wykorzystany przy użyciu ustawienia konfiguracyjnego default_view.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} -MExtUtils::MakeMaker -we 'WriteMakefile(NAME=>"Catalyst::Action::RenderView")' \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Catalyst/Action/*.pm
%{_mandir}/man3/*
