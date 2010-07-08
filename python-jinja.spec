
%define module jinja
Summary:	Template engine
Name:		python-%{module}
Version:	1.2
Release:	2
License:	BSD
Group:		Development/Languages/Python
Source0:	http://pypi.python.org/packages/source/J/Jinja/Jinja-%{version}.tar.gz
# Source0-md5:	1235a005ade00b213800ff1e798c0241
URL:		http://jinja.pocoo.org/1/
Requires:	python-docutils >= 0.5
BuildRequires:	python-devel
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Jinja is a sandboxed  template engine written in pure Python  licensed
under the BSD license. It provides a Django-like non-XML syntax and
compiles templates into executable python code. It's basically a
combination of Django templates and python code.

%prep
%setup -q -n Jinja-%{version}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
		--optimize=2 \
		--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc PKG-INFO TODO AUTHORS
%{py_sitedir}/%{module}
%{py_sitedir}/*Jinja*.egg*
