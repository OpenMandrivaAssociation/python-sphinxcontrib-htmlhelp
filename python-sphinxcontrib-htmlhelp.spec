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
BuildRequires:	gettext
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
for po in $(find -name '*.po'); do
  msgfmt --output-file=${po%.po}.mo ${po}
done
%py3_build

%install
%py3_install

# Move language files to /usr/share
pushd %{buildroot}%{python_sitelib}
for lang in $(find sphinxcontrib/htmlhelp/locales -maxdepth 1 -mindepth 1 -type d -not -path '*/\.*' -printf "%f ");
do
  test $lang == __pycache__ && continue
  install -d %{buildroot}%{_datadir}/locale/$lang/LC_MESSAGES
  mv sphinxcontrib/htmlhelp/locales/$lang/LC_MESSAGES/*.mo %{buildroot}%{_datadir}/locale/$lang/LC_MESSAGES/
done
rm -rf sphinxcontrib/htmlhelp/locales
ln -s %{_datadir}/locale sphinxcontrib/htmlhelp/locales
popd

%find_lang sphinxcontrib.htmlhelp

%files -f sphinxcontrib.htmlhelp.lang
%license LICENSE
%doc README.rst
%{python_sitelib}/sphinxcontrib/
%{python_sitelib}/sphinxcontrib_htmlhelp-%{version}-py%{python3_version}-*.pth
%{python_sitelib}/sphinxcontrib_htmlhelp-%{version}-py%{python3_version}.egg-info/
