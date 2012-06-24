#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Catalyst
%define	pnam	Action-RenderView
Summary:	Catalyst::Action::RenderView - Sensible default end action.
#Summary(pl):	
Name:		perl-Catalyst-Action-RenderView
Version:	0.04
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/M/MR/MRAMBERG/Catalyst-Action-RenderView-0.04.tar.gz
# Source0-md5:	95f0e438c073efa5e0930eda00304136
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Catalyst >= 5.7
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This action implements a sensible default end action, which will forward
to the first available view, unless status is set to 3xx, or there is a
response body. It also allows you to pass dump_info=1 to the url in
order to force a debug screen, while in debug mode.

If you have more than one view, you can specify which one to use with
the default_view config setting (see Catalyst/"$c-view($name)">.)

# %description -l pl
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Catalyst/Action/*.pm
%{_mandir}/man3/*
