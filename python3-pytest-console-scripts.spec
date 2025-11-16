#
# Conditional build:
%bcond_without	tests	# unit tests

Summary:	Pytest plugin for testing console scripts
Summary(pl.UTF-8):	Wtyczka pytesta do testowania skryptów konsolowych
Name:		python3-pytest-console-scripts
Version:	1.4.1
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/pytest-console-scripts/
Source0:	https://files.pythonhosted.org/packages/source/p/pytest-console-scripts/pytest-console-scripts-%{version}.tar.gz
# Source0-md5:	f28617c5043f2cf39ad0cea40132032d
URL:		https://pypi.org/project/pytest-console-scripts/
BuildRequires:	python3-modules >= 1:3.8
BuildRequires:	python3-setuptools
BuildRequires:	python3-setuptools_scm
%if %{with tests}
%if "%{_ver_lt %{py3_ver} 3.10}" == "1"
BuildRequires:	python3-importlib_metadata >= 3.6
%endif
BuildRequires:	python3-pytest >= 4.0.0
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.750
Requires:	python3-modules >= 1:3.8
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pytest-console-scripts is a pytest plugin for testing Python scripts
installed via console_scripts entry point of setup.py. It can run the
scripts under test in a separate process or using the interpreter
that's running the test suite. The former mode ensures that the script
will run in an environment that is identical to normal execution
whereas the latter one allows much quicker test runs during
development while simulating the real runs as much as possible.

%description -l pl.UTF-8
pytest-console-scripts to wtyczka pytesta do testowania skryptów
Pythona instalowanych poprzez wpis console_scripts w setup.py. Może
uruchamiać testowane skrypty w osobnym procesie lub przy użyciu
interpretera uruchamiającego zestaw testów. Pierwszy tryb zapewnia, że
skrypt będzie działał w środowisku identycznym z normalnym trybem
wykonywania, natomiast drugi pozwala na szybsze uruchamianie testów w
czasie rozwijania oprogramowania, symulując w miarę rzeczywiste
uruchomienia.

%prep
%setup -q -n pytest-console-scripts-%{version}

%build
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTEST_PLUGINS=pytest_console_scripts \
PYTHONPATH=$(pwd) \
%{__python3} -m pytest tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md LICENSE README.md
%{py3_sitescriptdir}/pytest_console_scripts
%{py3_sitescriptdir}/pytest_console_scripts-%{version}-py*.egg-info
