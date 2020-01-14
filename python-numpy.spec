# NOTE: 1.16.x is the last series with python 2.7 support; for newer versions see python3-numpy.spec
#
# Conditional build:
%bcond_without  python2 # CPython 2.x modules
%bcond_without  python3 # CPython 3.x modules

%define		module	numpy
Summary:	Python 2 numerical facilities
Summary(pl.UTF-8):	Moduły do obliczeń numerycznych dla języka Python 2
Name:		python-%{module}
# keep 1.16.x series here, see note above
Version:	1.16.6
Release:	1
Epoch:		1
License:	BSD
Group:		Libraries/Python
#Source0Download: https://github.com/numpy/numpy/releases/
Source0:	https://github.com/numpy/numpy/releases/download/v%{version}/%{module}-%{version}.tar.gz
# Source0-md5:	5e958c603605f3168b7b29f421f64cdd
URL:		http://sourceforge.net/projects/numpy/
BuildRequires:	gcc-fortran
BuildRequires:	lapack-devel >= 3.1.1-2
%if %{with python2}
BuildRequires:	python-devel >= 1:2.7
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-devel >= 1:3.5
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-libs >= 1:2.7
# -- dropped some time ago
Obsoletes:	python-numpy-Properties
# -- dropped some time ago, should have been released as separate package, but wasn't
Obsoletes:	python-numpy-kinds
# old subpackage, merged into main
Obsoletes:	python-numpy-FFT
# -- dropped during Numeric->numpy transition (ma in main now?)
Obsoletes:	python-numpy-MA
Obsoletes:	python-numpy-RNG
Obsoletes:	python-Numeric
Obsoletes:	python-Numeric-FFT
Obsoletes:	python-Numeric-MA
Obsoletes:	python-Numeric-RNG
Requires:	pydoc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
NumPy is a collection of extension modules to provide high-performance
multidimensional numeric arrays to the Python programming language.

This package contains Python 2 modules.

%description -l pl.UTF-8
NumPy to zbiór modułów rozszerzeń zapewniających wydajne obliczenia
numeryczne na macierzach wielowymiarowych w języku Python.

Ten pakiet zawiera moduły Pythona 2.

%package devel
Summary:	C header files for Python 2 numerical modules
Summary(pl.UTF-8):	Pliki nagłówkowe języka C modułów numerycznych Pythona 2
Group:		Development/Languages/Python
%pyrequires_eq	python-devel
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	python-Numeric-devel

%description devel
C header files for Python 2 numerical modules.

%description devel -l pl.UTF-8
Pliki nagłówkowe języka C modułów numerycznych Pythona 2.

%package -n f2py
Summary:	Fortran to Python 2 interface generator
Summary(pl.UTF-8):	Generator interfejsów z Fortranu do Pythona 2
Group:		Libraries/Python
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description -n f2py
Fortran to Python 2 interface generator.

%description -n f2py -l pl.UTF-8
Generator interfejsów z Fortranu do Pythona 2.

%package -n python3-%{module}
Summary:	Python 3.x numerical facilities
Summary(pl.UTF-8):	Moduły do obliczeń numerycznych dla języka Python 3.x
Group:		Libraries/Python
Requires:	python3-libs >= 1:3.5

%description -n python3-%{module}
NumPy is a collection of extension modules to provide high-performance
multidimensional numeric arrays to the Python programming language.

This package contains Python 3 modules.

%description -l pl.UTF-8 -n python3-%{module}
NumPy to zbiór modułów rozszerzeń zapewniających wydajne obliczenia
numeryczne na macierzach wielowymiarowych w języku Python.

Ten pakiet zawiera moduły Pythona 3.

%package -n python3-%{module}-devel
Summary:	C header files for Python 3 numerical modules
Summary(pl.UTF-8):	Pliki nagłówkowe języka C modułów numerycznych Pythona 3
Group:		Development/Languages/Python
%pyrequires_eq	python3-devel
Requires:	python3-%{module} = %{epoch}:%{version}-%{release}
Obsoletes:	python-Numeric-devel

%description -n python3-%{module}-devel
C header files for Python 3 numerical modules.

%description -n python3-%{module}-devel -l pl.UTF-8
Pliki nagłówkowe języka C modułów numerycznych Pythona 3.

%package -n f2py3
Summary:	Fortran to Python 3 interface generator
Summary(pl.UTF-8):	Generator interfejsów z Fortranu do Pythona 3
Group:		Libraries/Python
Requires:	python3-%{module} = %{epoch}:%{version}-%{release}

%description -n f2py3
Fortran to Python 3 interface generator.

%description -n f2py3 -l pl.UTF-8
Generator interfejsów z Fortranu do Pythona 3.

%prep
%setup -q -n %{module}-%{version}

%build
# numpy.distutils uses CFLAGS/LDFLAGS as its own flags replacements,
# instead of appending proper options (like -fPIC/-shared resp.)
CFLAGS="%{rpmcflags} -fPIC"
LDFLAGS="%{rpmldflags} -shared"

%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%{__rm} -r $RPM_BUILD_ROOT%{py_sitedir}/%{module}/doc
%{__rm} -r $RPM_BUILD_ROOT%{py_sitedir}/%{module}/tests
%{__rm} -r $RPM_BUILD_ROOT%{py_sitedir}/%{module}/*/tests
%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/%{module}/LICENSE.txt

%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/%{module}/distutils/mingw/gfortran_vs2003_hack.c
%endif

%if %{with python3}
%py3_install

%{__rm} -r $RPM_BUILD_ROOT%{py3_sitedir}/%{module}/doc
%{__rm} -r $RPM_BUILD_ROOT%{py3_sitedir}/%{module}/tests
%{__rm} -r $RPM_BUILD_ROOT%{py3_sitedir}/%{module}/*/tests
%{__rm} $RPM_BUILD_ROOT%{py3_sitedir}/%{module}/LICENSE.txt

%{__rm} $RPM_BUILD_ROOT%{py3_sitedir}/%{module}/distutils/mingw/gfortran_vs2003_hack.c
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE.txt THANKS.txt
%dir %{py_sitedir}/%{module}
%{py_sitedir}/%{module}/*.py
%{py_sitedir}/%{module}/*.py[co]
%dir %{py_sitedir}/%{module}/compat
%{py_sitedir}/%{module}/compat/*.py
%{py_sitedir}/%{module}/compat/*.py[co]
%dir %{py_sitedir}/%{module}/core
%{py_sitedir}/%{module}/core/*.py
%{py_sitedir}/%{module}/core/*.py[co]
%attr(755,root,root) %{py_sitedir}/%{module}/core/*.so
%dir %{py_sitedir}/%{module}/distutils
%{py_sitedir}/%{module}/distutils/*.py
%{py_sitedir}/%{module}/distutils/*.py[co]
%dir %{py_sitedir}/%{module}/distutils/command
%{py_sitedir}/%{module}/distutils/command/*.py
%{py_sitedir}/%{module}/distutils/command/*.py[co]
%dir %{py_sitedir}/%{module}/distutils/fcompiler
%{py_sitedir}/%{module}/distutils/fcompiler/*.py
%{py_sitedir}/%{module}/distutils/fcompiler/*.py[co]
%dir %{py_sitedir}/%{module}/fft
%{py_sitedir}/%{module}/fft/*.py
%{py_sitedir}/%{module}/fft/*.py[co]
%attr(755,root,root) %{py_sitedir}/%{module}/fft/fftpack_lite.so
%dir %{py_sitedir}/%{module}/lib
%{py_sitedir}/%{module}/lib/*.py
%{py_sitedir}/%{module}/lib/*.py[co]
%dir %{py_sitedir}/%{module}/linalg
%{py_sitedir}/%{module}/linalg/*.py
%{py_sitedir}/%{module}/linalg/*.py[co]
%attr(755,root,root) %{py_sitedir}/%{module}/linalg/_umath_linalg.so
%attr(755,root,root) %{py_sitedir}/%{module}/linalg/lapack_lite.so
%dir %{py_sitedir}/%{module}/ma
%{py_sitedir}/%{module}/ma/*.py
%{py_sitedir}/%{module}/ma/*.py[co]
%dir %{py_sitedir}/%{module}/matrixlib
%{py_sitedir}/%{module}/matrixlib/*.py
%{py_sitedir}/%{module}/matrixlib/*.py[co]
%dir %{py_sitedir}/%{module}/polynomial
%{py_sitedir}/%{module}/polynomial/*.py
%{py_sitedir}/%{module}/polynomial/*.py[co]
%dir %{py_sitedir}/%{module}/random
%{py_sitedir}/%{module}/random/*.py
%{py_sitedir}/%{module}/random/*.py[co]
%attr(755,root,root) %{py_sitedir}/%{module}/random/mtrand.so
%dir %{py_sitedir}/%{module}/testing
%{py_sitedir}/%{module}/testing/_private
%{py_sitedir}/%{module}/testing/*.py
%{py_sitedir}/%{module}/testing/*.py[co]
%{py_sitedir}/numpy-%{version}-py*.egg-info

%files devel
%defattr(644,root,root,755)
%{py_sitedir}/%{module}/core/include
%{py_sitedir}/%{module}/core/lib
%{py_sitedir}/%{module}/random/*.h

%files -n f2py
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/f2py2
%attr(755,root,root) %{_bindir}/f2py%{py_ver}
%dir %{py_sitedir}/%{module}/f2py
%{py_sitedir}/%{module}/f2py/*.py
%{py_sitedir}/%{module}/f2py/*.py[co]
%{py_sitedir}/%{module}/f2py/src
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc LICENSE.txt THANKS.txt
%dir %{py3_sitedir}/%{module}
%{py3_sitedir}/%{module}/*.py
%{py3_sitedir}/%{module}/__pycache__
%dir %{py3_sitedir}/%{module}/compat
%{py3_sitedir}/%{module}/compat/*.py
%{py3_sitedir}/%{module}/compat/__pycache__
%dir %{py3_sitedir}/%{module}/core
%{py3_sitedir}/%{module}/core/*.py
%{py3_sitedir}/%{module}/core/__pycache__
%attr(755,root,root) %{py3_sitedir}/%{module}/core/*.cpython-3*.so
%dir %{py3_sitedir}/%{module}/distutils
%{py3_sitedir}/%{module}/distutils/*.py
%{py3_sitedir}/%{module}/distutils/__pycache__
%dir %{py3_sitedir}/%{module}/distutils/command
%{py3_sitedir}/%{module}/distutils/command/*.py
%{py3_sitedir}/%{module}/distutils/command/__pycache__
%dir %{py3_sitedir}/%{module}/distutils/fcompiler
%{py3_sitedir}/%{module}/distutils/fcompiler/*.py
%{py3_sitedir}/%{module}/distutils/fcompiler/__pycache__
%dir %{py3_sitedir}/%{module}/fft
%{py3_sitedir}/%{module}/fft/*.py
%{py3_sitedir}/%{module}/fft/__pycache__
%attr(755,root,root) %{py3_sitedir}/%{module}/fft/fftpack_lite.cpython-3*.so
%dir %{py3_sitedir}/%{module}/lib
%{py3_sitedir}/%{module}/lib/*.py
%{py3_sitedir}/%{module}/lib/__pycache__
%dir %{py3_sitedir}/%{module}/linalg
%{py3_sitedir}/%{module}/linalg/*.py
%{py3_sitedir}/%{module}/linalg/__pycache__
%attr(755,root,root) %{py3_sitedir}/%{module}/linalg/_umath_linalg.cpython-3*.so
%attr(755,root,root) %{py3_sitedir}/%{module}/linalg/lapack_lite.cpython-3*.so
%dir %{py3_sitedir}/%{module}/ma
%{py3_sitedir}/%{module}/ma/*.py
%{py3_sitedir}/%{module}/ma/__pycache__
%dir %{py3_sitedir}/%{module}/matrixlib
%{py3_sitedir}/%{module}/matrixlib/*.py
%{py3_sitedir}/%{module}/matrixlib/__pycache__
%dir %{py3_sitedir}/%{module}/polynomial
%{py3_sitedir}/%{module}/polynomial/*.py
%{py3_sitedir}/%{module}/polynomial/__pycache__
%dir %{py3_sitedir}/%{module}/random
%{py3_sitedir}/%{module}/random/*.py
%{py3_sitedir}/%{module}/random/__pycache__
%attr(755,root,root) %{py3_sitedir}/%{module}/random/mtrand.cpython-3*.so
%dir %{py3_sitedir}/%{module}/testing
%{py3_sitedir}/%{module}/testing/_private
%{py3_sitedir}/%{module}/testing/*.py
%{py3_sitedir}/%{module}/testing/__pycache__
%{py3_sitedir}/numpy-%{version}-py*.egg-info

%files -n python3-%{module}-devel
%defattr(644,root,root,755)
%{py3_sitedir}/%{module}/core/include
%{py3_sitedir}/%{module}/core/lib
%{py3_sitedir}/%{module}/random/*.h

%files -n f2py3
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/f2py3
%attr(755,root,root) %{_bindir}/f2py%{py3_ver}
%dir %{py3_sitedir}/%{module}/f2py
%{py3_sitedir}/%{module}/f2py/*.py
%{py3_sitedir}/%{module}/f2py/__pycache__
%{py3_sitedir}/%{module}/f2py/src
%endif
