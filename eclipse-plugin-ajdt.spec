Summary:	AJDT - aspectJ development tools
Summary(pl):	AJDT - narzêdzia programistyczne aspectJ
Name:		eclipse-plugin-ajdt
Version:	1.3.0
Release:	1
License:	CPL v0.5
Group:		Development/Languages
Source0:	http://download.eclipse.org/technology/ajdt/31/dev/update/ajdt_%{version}.20050823115355_archive.zip
# Source0-md5:	ae776fad1db899469c8a1aee9a5de752
URL:		http://www.eclipse.org/ajdt/
BuildRequires:	unzip
Requires:	eclipse >= 3.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_eclipsedir  	%{_libdir}/eclipse

%description
The AspectJ Development Tools (AJDT) project provides Eclipse platform
based tool support for AOSD (Aspect Oriented Software Development)
with AspectJ.

%description -l pl
Projekt AJDT (AspectJ Development Tools) dodaje obs³ugê AOSD (Aspect
Oriented Software Development - tworzenia oprogramowania
zorientowanego aspektowo) do narzêdzi opartych na platformie Eclipse.

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
