%define module sphinxcontrib-htmlhelp

Summary:	HTML help file support for the Sphinx documentation generator
Name:		python-%{module}
Version:	2.1.0
Release:	2
Source0:	https://files.pythonhosted.org/packages/source/s/%{module}/sphinxcontrib_htmlhelp-%{version}.tar.gz
License:	ISC
Group:		Development/Python
Url:		https://sphinx-doc.org/
BuildArch:	noarch
BuildSystem:	python
BuildRequires:	python
BuildRequires:	gettext
BuildRequires:	python%{pyver}dist(pip)
Obsoletes:	python2-%{module} < 2.0.0

%description
HTML help file support for the Sphinx documentation generator.

%prep -a
find -name '*.mo' -delete

%build -p
for po in $(find -name '*.po'); do
  msgfmt --output-file=${po%.po}.mo ${po}
done

%install -a
# Move language files to /usr/share
cd %{buildroot}%{python_sitelib}
for lang in $(find sphinxcontrib/htmlhelp/locales -maxdepth 1 -mindepth 1 -type d -not -path '*/\.*' -printf "%f ");
do
  test $lang == __pycache__ && continue
  install -d %{buildroot}%{_datadir}/locale/$lang/LC_MESSAGES
  mv sphinxcontrib/htmlhelp/locales/$lang/LC_MESSAGES/*.mo %{buildroot}%{_datadir}/locale/$lang/LC_MESSAGES/
done
rm -rf sphinxcontrib/htmlhelp/locales
ln -s %{_datadir}/locale sphinxcontrib/htmlhelp/locales
cd -

%find_lang sphinxcontrib.htmlhelp

%files -f sphinxcontrib.htmlhelp.lang
%doc README.rst
%{python_sitelib}/sphinxcontrib/
%{python_sitelib}/sphinxcontrib_htmlhelp-%{version}.dist-info
