# Conditional build:
%bcond_without  python2 # CPython 2.x module
%bcond_without  python3 # CPython 3.x module

%define		module	numpy
Summary:	Python numerical facilities
Summary(pl.UTF-8):	Moduły do obliczeń numerycznych dla języka Python
Name:		python-%{module}
Version:	1.7.1
Release:	2
Epoch:		1
License:	BSD
Group:		Libraries/Python
Source0:	http://downloads.sourceforge.net/numpy/%{module}-%{version}.tar.gz
# Source0-md5:	0ab72b3b83528a7ae79c6df9042d61c6
Patch0:		%{name}-fortran-version.patch
URL:		http://sourceforge.net/projects/numpy/
%if %{with python2}
BuildRequires:	python-devel
%pyrequires_eq	python-libs
%endif
%if %{with python3}
BuildRequires:	python3-devel >= 1:3.3
BuildRequires:	python3-2to3
%endif
BuildRequires:	gcc-fortran
BuildRequires:	lapack-devel >= 3.1.1-2
BuildRequires:	rpm-pythonprov
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

%description -l pl.UTF-8
Pakiet umożliwia wydajne obliczenia numeryczne na macierzach
wielowymiarowych.

%package -n python3-%{module}
Summary:	Python 3.x numerical facilities
Summary(pl.UTF-8):	Moduły do obliczeń numerycznych dla języka Python 3.x
Group:		Libraries/Python

%description -n python3-%{module}
NumPy is a collection of extension modules to provide high-performance
multidimensional numeric arrays to the Python programming language.

%description -l pl.UTF-8 -n python3-%{module}
Pakiet umożliwia wydajne obliczenia numeryczne na macierzach
wielowymiarowych.

%package devel
Summary:	C header files for numerical modules
Summary(pl.UTF-8):	Pliki nagłówkowe języka C modułów numerycznych
Group:		Development/Languages/Python
%pyrequires_eq	python-devel
Obsoletes:	python-Numeric-devel
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
C header files for numerical modules.

%description devel -l pl.UTF-8
Pliki nagłówkowe języka C modułów numerycznych.

%package -n python3-%{module}-devel
Summary:	C header files for numerical modules
Summary(pl.UTF-8):	Pliki nagłówkowe języka C modułów numerycznych
Group:		Development/Languages/Python
%pyrequires_eq	python-devel
Obsoletes:	python-Numeric-devel
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description -n python3-%{module}-devel
C header files for numerical modules.

%description -n python3-%{module}-devel -l pl.UTF-8
Pliki nagłówkowe języka C modułów numerycznych.

%package numarray
Summary:	Array manipulation and computations for python
Summary(pl.UTF-8):	Operacje i obliczenia na tablicach dla Pythona
Group:		Development/Languages/Python
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description numarray
Numarray provides array manipulation and computational capabilities
similar to those found in IDL, Matlab, or Octave. Using numarray, it
is possible to write many efficient numerical data processing
applications directly in Python without using any C, C++ or Fortran
code (as well as doing such analysis interactively within Python or
PyRAF). For algorithms that are not well suited for efficient
computation using array facilities it is possible to write C functions
(and eventually Fortran) that can read and write numarray arrays that
can be called from Python.

Numarray is a re-implementation of an older Python array module called
Numeric. In general its interface is very similar. It is mostly
backward compatible and will be becoming more so in future releases.

%description numarray -l pl.UTF-8
Numarray zapewnia narzędzia do operacji oraz obliczeń na tablicach
podobne do tych, jakie zapewniają IDL, Matlab czy Octave. Używając
numarray możliwe jest stworzenie bezpośrednio w Pythonie, nie używając
wstawek C, C++ czy fortranowych, wielu wydajnych aplikacji do
przetwarzania danych numerycznych. Dla algorytmów, które nie pracują
wydajnie z tablicami, możliwe jest napisanie funkcji C, które mogą
czytać i zapisywać tablice numarray, i które mogą być wywoływane z
poziomu Pythona.

Numarray jest ponowną implementacją starszego modułu Pythona -
Numeric. Interfejsy tych modułów są do siebie bardzo podobne. Numarray
jest w większości przypadków kompatybilny wstecz, a sytuacja poprawi
się w nowszych wersjach.

%package -n python3-%{module}-numarray
Summary:	Array manipulation and computations for python
Summary(pl.UTF-8):	Operacje i obliczenia na tablicach dla Pythona
Group:		Development/Languages/Python
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description -n python3-%{module}-numarray
Numarray provides array manipulation and computational capabilities
similar to those found in IDL, Matlab, or Octave. Using numarray, it
is possible to write many efficient numerical data processing
applications directly in Python without using any C, C++ or Fortran
code (as well as doing such analysis interactively within Python or
PyRAF). For algorithms that are not well suited for efficient
computation using array facilities it is possible to write C functions
(and eventually Fortran) that can read and write numarray arrays that
can be called from Python.

Numarray is a re-implementation of an older Python array module called
Numeric. In general its interface is very similar. It is mostly
backward compatible and will be becoming more so in future releases.

%description -n python3-%{module}-numarray -l pl.UTF-8
Numarray zapewnia narzędzia do operacji oraz obliczeń na tablicach
podobne do tych, jakie zapewniają IDL, Matlab czy Octave. Używając
numarray możliwe jest stworzenie bezpośrednio w Pythonie, nie używając
wstawek C, C++ czy fortranowych, wielu wydajnych aplikacji do
przetwarzania danych numerycznych. Dla algorytmów, które nie pracują
wydajnie z tablicami, możliwe jest napisanie funkcji C, które mogą
czytać i zapisywać tablice numarray, i które mogą być wywoływane z
poziomu Pythona.

Numarray jest ponowną implementacją starszego modułu Pythona -
Numeric. Interfejsy tych modułów są do siebie bardzo podobne. Numarray
jest w większości przypadków kompatybilny wstecz, a sytuacja poprawi
się w nowszych wersjach.

%package numarray-devel
Summary:	Header files for python-numarray
Summary(pl.UTF-8):	Pliki nagłówkowe dla python-numarray
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}
Requires:	%{name}-numarray = %{epoch}:%{version}-%{release}

%description numarray-devel
Header files for python-numarray.

%description numarray-devel -l pl.UTF-8
Pliki nagłówkowe dla python-numarray.

%package -n python3-%{module}-numarray-devel
Summary:	Header files for python-numarray
Summary(pl.UTF-8):	Pliki nagłówkowe dla python-numarray
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}
Requires:	%{name}-numarray = %{epoch}:%{version}-%{release}

%description -n python3-%{module}-numarray-devel
Header files for python-numarray.

%description -n python3-%{module}-numarray-devel -l pl.UTF-8
Pliki nagłówkowe dla python-numarray.

%package oldnumeric
Summary:	Modules providing backward compatibility with old Numeric packages
Summary(pl.UTF-8):	Moduły zapewniające wsteczną kompatybilność ze starymi pakietami Numeric
Group:		Libraries/Python
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description oldnumeric
Modules providing backward compatibility with old Numeric packages.

%description oldnumeric -l pl.UTF-8
Moduły zapewniające wsteczną kompatybilność ze starymi pakietami
Numeric.

%package -n python3-%{module}-oldnumeric
Summary:	Modules providing backward compatibility with old Numeric packages
Summary(pl.UTF-8):	Moduły zapewniające wsteczną kompatybilność ze starymi pakietami Numeric
Group:		Libraries/Python
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description -n python3-%{module}-oldnumeric
Modules providing backward compatibility with old Numeric packages.

%description -n python3-%{module}-oldnumeric -l pl.UTF-8
Moduły zapewniające wsteczną kompatybilność ze starymi pakietami
Numeric.

%package -n f2py
Summary:	Fortran to Python interface generator
Summary(pl.UTF-8):	Generator interfejsów z Fortranu do Pythona
Group:		Libraries/Python
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description -n f2py
Fortran to Python interface generator.

%description -n f2py -l pl.UTF-8
Generator interfejsów z Fortranu do Pythona.

%package -n f2py3
Summary:	Fortran to Python 3 interface generator
Summary(pl.UTF-8):	Generator interfejsów z Fortranu do Pythona 3
Group:		Libraries/Python
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description -n f2py3
Fortran to Python 3 interface generator.

%description -n f2py3 -l pl.UTF-8
Generator interfejsów z Fortranu do Pythona 3.

%prep
%setup -q -n %{module}-%{version}
%patch0 -p1

%build
CC="%{__cc}"; export CC
CFLAGS="%{rpmcflags}"; export CFLAGS

%if %{with python2}
%{__python} setup.py build
%endif

%if %{with python3}
%{__python3} setup.py build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%{__python} setup.py install \
	--root=$RPM_BUILD_ROOT

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}

%{__rm} -r $RPM_BUILD_ROOT%{py_sitedir}/%{module}/doc
%{__rm} -r $RPM_BUILD_ROOT%{py_sitedir}/%{module}/*/{benchmarks,tests,docs}
# already in f2py package
%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/%{module}/f2py/f2py.1

%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/%{module}/distutils/mingw/gfortran_vs2003_hack.c
%endif

%if %{with python3}
%{__python3} setup.py install \
	--root=$RPM_BUILD_ROOT

%py3_ocomp $RPM_BUILD_ROOT%{py3_sitedir}
%py3_comp $RPM_BUILD_ROOT%{py3_sitedir}

%{__rm} -r $RPM_BUILD_ROOT%{py3_sitedir}/%{module}/doc
%{__rm} -r $RPM_BUILD_ROOT%{py3_sitedir}/%{module}/*/{tests,docs}
# already in f2py package
%{__rm} $RPM_BUILD_ROOT%{py3_sitedir}/%{module}/f2py/f2py.1

%{__rm} $RPM_BUILD_ROOT%{py3_sitedir}/%{module}/distutils/mingw/gfortran_vs2003_hack.c
%endif


%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
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
%attr(755,root,root) %{py_sitedir}/%{module}/lib/_compiled_base.so
%dir %{py_sitedir}/%{module}/linalg
%{py_sitedir}/%{module}/linalg/*.py
%{py_sitedir}/%{module}/linalg/*.py[co]
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
%{py_sitedir}/%{module}/testing/*.py
%{py_sitedir}/%{module}/testing/*.py[co]
%dir %{py_sitedir}/%{module}/tests
%{py_sitedir}/%{module}/tests/*.py
%{py_sitedir}/%{module}/tests/*.py[co]
%if "%{py_ver}" > "2.4"
%{py_sitedir}/numpy-%{version}-py*.egg-info
%endif
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
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
%attr(755,root,root) %{py3_sitedir}/%{module}/lib/_compiled_base.cpython-3*.so
%dir %{py3_sitedir}/%{module}/linalg
%{py3_sitedir}/%{module}/linalg/*.py
%{py3_sitedir}/%{module}/linalg/__pycache__
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
%{py3_sitedir}/%{module}/testing/*.py
%{py3_sitedir}/%{module}/testing/__pycache__
%dir %{py3_sitedir}/%{module}/tests
%{py3_sitedir}/%{module}/tests/*.py
%{py3_sitedir}/%{module}/tests/__pycache__
%{py3_sitedir}/numpy-%{version}-py*.egg-info
%endif

%if %{with python2}
%files devel
%defattr(644,root,root,755)
%{py_sitedir}/%{module}/core/include
%{py_sitedir}/%{module}/core/lib
%{py_sitedir}/%{module}/random/*.h
%endif

%if %{with python3}
%files -n python3-%{module}-devel
%defattr(644,root,root,755)
%{py3_sitedir}/%{module}/core/include
%{py3_sitedir}/%{module}/core/lib
%{py3_sitedir}/%{module}/random/*.h
%endif

%if %{with python2}
%files numarray
%defattr(644,root,root,755)
%dir %{py_sitedir}/%{module}/numarray
%{py_sitedir}/%{module}/numarray/*.py
%{py_sitedir}/%{module}/numarray/*.py[co]
%attr(755,root,root) %{py_sitedir}/%{module}/numarray/_capi.so
%endif

%if %{with python3}
%files -n python3-%{module}-numarray
%defattr(644,root,root,755)
%dir %{py3_sitedir}/%{module}/numarray
%{py3_sitedir}/%{module}/numarray/*.py
%{py3_sitedir}/%{module}/numarray/__pycache__
%attr(755,root,root) %{py3_sitedir}/%{module}/numarray/_capi.cpython-3*.so
%endif

%if %{with python2}
%files numarray-devel
%defattr(644,root,root,755)
%{py_sitedir}/%{module}/numarray/include
%endif

%if %{with python3}
%files -n python3-%{module}-numarray-devel
%defattr(644,root,root,755)
%{py3_sitedir}/%{module}/numarray/include
%endif

%if %{with python2}
%files oldnumeric
%defattr(644,root,root,755)
%dir %{py_sitedir}/%{module}/oldnumeric
%{py_sitedir}/%{module}/oldnumeric/*.py
%{py_sitedir}/%{module}/oldnumeric/*.py[co]
%endif

%if %{with python3}
%files -n python3-%{module}-oldnumeric
%defattr(644,root,root,755)
%dir %{py3_sitedir}/%{module}/oldnumeric
%{py3_sitedir}/%{module}/oldnumeric/*.py
%{py3_sitedir}/%{module}/oldnumeric/__pycache__
%endif

%if %{with python2}
%files -n f2py
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/f2py
%dir %{py_sitedir}/%{module}/f2py
%{py_sitedir}/%{module}/f2py/*.py
%{py_sitedir}/%{module}/f2py/*.py[co]
%{py_sitedir}/%{module}/f2py/src
%endif

%if %{with python3}
%files -n f2py3
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/f2py3
%dir %{py3_sitedir}/%{module}/f2py
%{py3_sitedir}/%{module}/f2py/*.py
%{py3_sitedir}/%{module}/f2py/__pycache__
%{py3_sitedir}/%{module}/f2py/src
%endif
