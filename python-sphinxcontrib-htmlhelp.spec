%define	module	sphinxcontrib-htmlhelp

Summary:	HTML help file support for the Sphinx documentation generator
Name:		python-%{module}
Version:	1.0.3
Release:	1
Source0:	https://github.com/sphinx-doc/%{module}/archive/%{version}.tar.gz
License:	ISC
Group:		Development/Python
Url:		http://sphinx-doc.org/
BuildArch:	noarch
BuildRequires:	pkgconfig(python2)
BuildRequires:	pkgconfig(python3)
BuildRequires:	python-setuptools
BuildRequires:	python2-setuptools

%description
HTML help file support for the Sphinx documentation generator

%package -n python2-%{module}
Summary:	HTML help file support for the Sphinx documentation generator
Group:		Development/Python

%description -n python2-%{module}
HTML help file support for the Sphinx documentation generator

%prep
%setup -qc
cp -a %{module}-%{version} py2

%install
cd py2
PYTHONDONTWRITEBYTECODE=1 %__python2 setup.py install --root=%{buildroot}

cd ../%{module}-%{version}
PYTHONDONTWRITEBYTECODE=1 %__python setup.py install --root=%{buildroot}

%files
%{py_puresitedir}/sphinxcontrib*

%files -n python2-%{module}
%{py2_puresitedir}/sphinxcontrib*
