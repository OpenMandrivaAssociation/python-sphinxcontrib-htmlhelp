%define module sphinxcontrib-htmlhelp

Summary:	HTML help file support for the Sphinx documentation generator
Name:		python-%{module}
Version:	2.0.0
Release:	1
Source0:	https://github.com/sphinx-doc/%{module}/archive/%{module}-%{version}.tar.gz
License:	ISC
Group:		Development/Python
Url:		http://sphinx-doc.org/
BuildArch:	noarch
BuildRequires:	pkgconfig(python3)
BuildRequires:	python-setuptools
Obsoletes:	python2-%{module} < 2.0.0

%description
HTML help file support for the Sphinx documentation generator.

%prep
%autosetup -n %{module}-%{version}

# drop bundled egg-info
rm -rf *.egg-info/

find -name '*.mo' -delete

%build
%py3_build

%install
%py3_install

%files
%license LICENSE
%doc README.rst
%{python_sitelib}/sphinxcontrib/
%{python_sitelib}/sphinxcontrib_htmlhelp-%{version}-py%{python3_version}-*.pth
%{python_sitelib}/sphinxcontrib_htmlhelp-%{version}-py%{python3_version}.egg-info/
