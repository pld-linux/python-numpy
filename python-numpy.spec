#
# TODO:
#	- description for oldnumeric
#
%define		module	numpy
%define		_rc1 rc1

Summary:	Python numerical facilities
Summary(pl):	Modu³y do obliczeñ numerycznych dla jêzyka Python
Name:		python-%{module}
Version:	1.0
Release:	0.%{_rc1}.1
Epoch:		1
License:	distributable
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/numpy/%{module}-%{version}%{_rc1}.tar.gz
# Source0-md5:	b8cd486ee334520047f9a35454dad94a
URL:		http://sourceforge.net/projects/numpy/
BuildRequires:	python-devel >= 1:2.3
%pyrequires_eq	python-libs
# -- dropped some time ago
Obsoletes:	python-numpy-Properties
# -- dropped some time ago, should have been released as separate package, but wasn't
Obsoletes:	python-numpy-kinds
# -- dropped during Numeric->numpy transition
Obsoletes:	python-numpy-MA
Obsoletes:	python-numpy-RNG
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
NumPy is a collection of extension modules to provide high-performance
multidimensional numeric arrays to the Python programming language.

%description -l pl
Pakiet umo¿liwia wydajne obliczenia numeryczne na macierzach
wielowymiarowych.

%package devel
Summary:	C header files for numerical modules
Summary(pl):	Pliki nag³ówkowe jêzyka C modu³ów numerycznych
Group:		Development/Languages/Python
%pyrequires_eq	python-devel
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
C header files for numerical modules.

%description devel -l pl
Pliki nag³ówkowe jêzyka C modu³ów numerycznych.

%package FFT
Summary:	Interface to the FFTPACK FORTRAN library
Summary(pl):	Interfejs do biblioteki FFTPACK jêzyka Fortran
Group:		Libraries/Python
%pyrequires_eq	python-libs
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description FFT
The FFT.py module provides a simple interface to the FFTPACK FORTRAN
library, which is a powerful standard library for doing fast Fourier
transforms of real and complex data sets.

%description FFT -l pl
Modu³ FFT zawiera prosty interfejs do biblioteki FFTPACK jêzyka
Fortran. Ta biblioteka o wysokich mo¿liwo¶ciach jest standardowo
u¿ywana do prowadzenia obliczeñ za pomoc± dyskretnej transformaty
Fouriera na liczba rzeczywistych i zespolonych.

%package numarray
Summary:        Array manipulation and computations for python
Summary(pl):    Operacje i obliczenia na tablicach dla Pythona
Group:          Development/Languages/Python
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

%description numarray -l pl
Numarray zapewnia narzêdzia do operacji oraz obliczeñ na tablicach
podobne do tych, jakie zapewniaj± IDL, Matlab czy Octabe. U¿ywaj±c
numarray mo¿liwe jest stworzenie bezpo¶rednio w Pythonie, nie u¿ywaj±c
wstawek C, C++ czy Fortranowych, wielu wydajnych aplikacji do
przetwarzania danych numerycznych. Dla algorytmów, które nie pracuj±
wydajnie z tablicami, mo¿liwe jest napisanie funkcji C, które mog±
czytaæ i zapisywaæ tablice numarray, i które mog± byæ wywo³ywane z
poziomu Pythona.

Numarray jest ponown± implementacj± starszego modu³u Pythona -
Numeric. Interfejsy tych modu³ów s± do siebie bardzo podobne. Numarray
jest w wiêkszo¶ci przypadków kompatybilny wstecz, a sytuacja poprawi
siê w nowszych wersjach.

%package numarray-devel
Summary:        Header files for python-numarray
Summary(pl):    Pliki nag³ówkowe dla python-numarray
Group:          Development/Libraries

%description numarray-devel
Header files for python-numarray.

%description numarray-devel -l pl
Pliki nag³ówkowe dla python-numarray.

%package oldnumeric
Summary:        Old numeric packages
Summary(pl):    Old numeric packages
Group:          Libraries/Python

%description oldnumeric
Old numeric packages.

%description oldnumeric -l pl
Old numeric packages.

%prep
%setup -q -n %{module}-%{version}%{_rc1}

%build
CC="%{__cc}"; export CC
CFLAGS="%{rpmcflags}"; export CFLAGS
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--root=$RPM_BUILD_ROOT

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

rm -rf $RPM_BUILD_ROOT%{py_sitedir}/%{module}/{*.txt,COMPATIBILITY,scipy_compatibility,doc}
rm -rf $RPM_BUILD_ROOT%{py_sitedir}/%{module}/*/{tests,docs}
# already in f2py package
rm -rf $RPM_BUILD_ROOT{%{_bindir}/f2py,%{py_sitedir}/%{module}/f2py/f2py.1}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{py_sitedir}/%{module}
%{py_sitedir}/%{module}/*.py[co]
%dir %{py_sitedir}/%{module}/core
%{py_sitedir}/%{module}/core/*.py[co]
%attr(755,root,root) %{py_sitedir}/%{module}/core/*.so
%dir %{py_sitedir}/%{module}/distutils
%{py_sitedir}/%{module}/distutils/*.py[co]
%{py_sitedir}/%{module}/distutils/site.cfg
%dir %{py_sitedir}/%{module}/distutils/command
%{py_sitedir}/%{module}/distutils/command/*.py[co]
%dir %{py_sitedir}/%{module}/distutils/fcompiler
%{py_sitedir}/%{module}/distutils/fcompiler/*.py[co]
%dir %{py_sitedir}/%{module}/f2py
%{py_sitedir}/%{module}/f2py/*.py[co]
%{py_sitedir}/%{module}/f2py/src
%dir %{py_sitedir}/%{module}/lib
%{py_sitedir}/%{module}/lib/*.py[co]
%attr(755,root,root) %{py_sitedir}/%{module}/lib/*.so
%dir %{py_sitedir}/%{module}/linalg
%{py_sitedir}/%{module}/linalg/*.py[co]
%attr(755,root,root) %{py_sitedir}/%{module}/linalg/*.so
%dir %{py_sitedir}/%{module}/random
%{py_sitedir}/%{module}/random/*.py[co]
%attr(755,root,root) %{py_sitedir}/%{module}/random/*.so
%dir %{py_sitedir}/%{module}/testing
%{py_sitedir}/%{module}/testing/*.py[co]

%files devel
%defattr(644,root,root,755)
%{py_sitedir}/%{module}/core/include
%{py_sitedir}/%{module}/random/*.h

%files FFT
%defattr(644,root,root,755)
%dir %{py_sitedir}/%{module}/fft
%attr(755,root,root) %{py_sitedir}/%{module}/fft/*.so
%{py_sitedir}/%{module}/fft/*.py[co]

%files numarray
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/%{module}/numarray/*.so
%dir %{py_sitedir}/%{module}/numarray
%{py_sitedir}/%{module}/numarray/*.py[co]

%files numarray-devel
%defattr(644,root,root,755)
%dir %{py_sitedir}/%{module}/numarray/numpy
%{py_sitedir}/%{module}/numarray/numpy/*

%files oldnumeric
%defattr(644,root,root,755)
%dir %{py_sitedir}/%{module}/oldnumeric
%{py_sitedir}/%{module}/oldnumeric/*
