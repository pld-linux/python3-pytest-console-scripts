#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_with	python3 # CPython 3.x module (built from python3-pytest-console-scripts.spec)

Summary:	Pytest plugin for testing console scripts
Summary(pl.UTF-8):	Wtyczka pytesta do testowania skryptów konsolowych
Name:		python-pytest-console-scripts
# keep 0.x here for python2 support
Version:	0.2.0
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/pytest-console-scripts/
Source0:	https://files.pythonhosted.org/packages/source/p/pytest-console-scripts/pytest-console-scripts-%{version}.tar.gz
# Source0-md5:	7bad9c8536a741c9af0542827da07eca
URL:		https://pypi.org/project/pytest-console-scripts/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-mock >= 2.0.0
BuildRequires:	python-pytest >= 4.0.0
#BuildRequires:	python-virtualenv < 20
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.3
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-mock >= 2.0.0
BuildRequires:	python3-pytest >= 4.0.0
#BuildRequires:	python3-virtualenv < 20
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
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

%package -n python3-pytest-console-scripts
Summary:	Pytest plugin for testing console scripts
Summary(pl.UTF-8):	Wtyczka pytesta do testowania skryptów konsolowych
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.3

%description -n python3-pytest-console-scripts
Pytest-console-scripts is a pytest plugin for testing python scripts
installed via console_scripts entry point of setup.py. It can run the
scripts under test in a separate process or using the interpreter
that's running the test suite. The former mode ensures that the script
will run in an environment that is identical to normal execution
whereas the latter one allows much quicker test runs during
development while simulating the real runs as much as possible.

%description -n python3-pytest-console-scripts -l pl.UTF-8
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
%if %{with python2}
%py_build

%if %{with tests}
# test_run_scripts relies on API removed in virtualenv 20
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTEST_PLUGINS=pytest_console_scripts \
%{__python} -m pytest tests --ignore=tests/test_run_scripts.py
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTEST_PLUGINS=pytest_console_scripts \
%{__python3} -m pytest tests --ignore=tests/test_run_scripts.py
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py_sitescriptdir}/pytest_console_scripts.py[co]
%{py_sitescriptdir}/pytest_console_scripts-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-pytest-console-scripts
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py3_sitescriptdir}/pytest_console_scripts.py
%{py3_sitescriptdir}/__pycache__/pytest_console_scripts.cpython-*.py[co]
%{py3_sitescriptdir}/pytest_console_scripts-%{version}-py*.egg-info
%endif
