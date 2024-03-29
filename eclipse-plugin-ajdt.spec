Summary:	AJDT - aspectJ development tools
Summary(pl.UTF-8):	AJDT - narzędzia programistyczne aspectJ
Name:		eclipse-plugin-ajdt
Version:	1.5.2
Release:	1
License:	CPL v0.5
Group:		Development/Languages
Source0:	http://download.eclipse.org/tools/ajdt/33/update/ajdt_%{version}_for_eclipse_3.3.zip
# Source0-md5:	e1b6b84cf4e885ff4395460ace0173e8
URL:		http://www.eclipse.org/ajdt/
BuildRequires:	unzip
Requires:	aspectj >= 1.6.0
Requires:	eclipse >= 3.3
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
