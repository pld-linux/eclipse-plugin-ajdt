Summary:	AJDT - aspectJ development tools
Name:		eclipse-plugin-ajdt
Version:	1.1.12
Release:	1
License:	CPL v0.5
Group:		Development/Languages
Source0:	http://download.eclipse.org/technology/ajdt/30/update/ajdt_%{version}_archive.zip
# Source0-md5:	80a9fcbdb18d5ca46340c011cf28f45a
URL:		http://www.eclipse.org/ajdt/
Requires:	eclipse >= 3.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_eclipsedir  	%{_datadir}/eclipse

%description
The AspectJ Development Tools (AJDT) project provides Eclipse platform based
tool support for AOSD (Aspect Oriented Software Development)  with AspectJ.

%prep
%setup -q -c

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_eclipsedir}/{features,plugins}

cp -r plugins features $RPM_BUILD_ROOT%{_eclipsedir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_eclipsedir}/features/*
%{_eclipsedir}/plugins/*