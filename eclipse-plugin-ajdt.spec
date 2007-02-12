Summary:	AJDT - aspectJ development tools
Summary(pl.UTF-8):	AJDT - narzędzia programistyczne aspectJ
Name:		eclipse-plugin-ajdt
Version:	1.4
Release:	1
License:	CPL v0.5
Group:		Development/Languages
Source0:	http://download.eclipse.org/tools/ajdt/32/update/ajdt_%{version}_for_eclipse_3.2.zip
# Source0-md5:	a535a91f7aaac3a23e44e17a40431b43
URL:		http://www.eclipse.org/ajdt/
BuildRequires:	unzip
Requires:	aspectj >= 1.5.2
Requires:	eclipse >= 3.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_eclipsedir  	%{_libdir}/eclipse

%description
The AspectJ Development Tools (AJDT) project provides Eclipse platform
based tool support for AOSD (Aspect Oriented Software Development)
with AspectJ.

%description -l pl.UTF-8
Projekt AJDT (AspectJ Development Tools) dodaje obsługę AOSD (Aspect
Oriented Software Development - tworzenia oprogramowania
zorientowanego aspektowo) do narzędzi opartych na platformie Eclipse.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_eclipsedir}/{features,plugins}

cp -r plugins features $RPM_BUILD_ROOT%{_eclipsedir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_libdir}/eclipse/features/*
%{_libdir}/eclipse/plugins/*
