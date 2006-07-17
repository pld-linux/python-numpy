%define		module	numpy

Summary:	Python numerical facilities
Summary(pl):	Modu³y do obliczeñ numerycznych dla jêzyka Python
Name:		python-%{module}
Version:	0.9.8
Release:	1
Epoch:		1
License:	distributable
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/numpy/%{module}-%{version}.tar.gz
# Source0-md5:	ca528d2b460a6567d70bb6bdf0dc1805
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

%prep
%setup -q -n %{module}-%{version}

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
%dir %{py_sitedir}/%{module}/dft
%attr(755,root,root) %{py_sitedir}/%{module}/dft/*.so
%{py_sitedir}/%{module}/dft/*.py[co]
