%include	/usr/lib/rpm/macros.python

%define module numpy
%define mname Numeric

Summary:	Python numerical facilities 
Summary(pl):	Modu³y do obliczeñ numerycznych dla jêzyka Python
Name:		python-%{module}
Version:	20.3
Release:	2
License:	distributable
Group:		Development/Languages/Python
Source0:	http://prdownloads.sourceforge.net/numpy/%{mname}-%{version}.tar.gz
URL:		http://www.pfdubois.com/numpy/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	python-devel >= 2.2
%requires_eq	python
BuildRequires:	rpm-pythonprov

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
%requires_eq	python
Requires:	%{name} = %{version}

%description devel
C header files for numerical modules.

%description devel -l pl
Pliki nag³ówkowe jêzyka C modu³ów numerycznych.

%package FFT
Summary:	Interface to the FFTPACK FORTRAN library
Summary(pl):	Interfejs do biblioteki FFTPACK jêzyka Fortran
Group:		Development/Languages/Python
%requires_eq	python
Requires:	%{name} = %{version}

%description FFT
The FFT.py module provides a simple interface to the FFTPACK FORTRAN
library, which is a powerful standard library for doing fast Fourier
transforms of real and complex data sets.

%description FFT -l pl
Modu³ FFT zawiera prosty interfejs do biblioteki FFTPACK jêzyka
Fortran. Ta biblioteka o wysokich mo¿liwo¶ciach jest standardowo
u¿ywana do prowadzenia obliczeñ za pomoc± dyskretnej transformaty
Fouriera na liczba rzeczywistych i zespolonych.

%package kinds
Summary:	Implementation of PEP 0242 - precision and range control of numeric computations
Summary(pl):	Implementacja propozycji PEP 0242 - mo¿liwo¶æ kontrolowania precyzji i zakresu obliczeñ numerycznych
Group:		Development/Languages/Python
%requires_eq	python
Requires:	%{name} = %{version}

%description kinds
This is implementation of PEP 0242. PEP's abstract follows:

This proposal gives the user optional control over the precision and
range of numeric computations so that a computation can be written
once and run anywhere with at least the desired precision and range.
It is backward compatible with existing code.

%description kinds -l pl
Modu³ zawiera implementacjê propozycji PEP 0242. Oto jej streszczenie.

Propozycja ta umo¿liwia u¿ytkownikowi, opcjonalnie, kontrolê nad
precyzj± i zakresem obliczeñ numerycznych. Dziêki temu raz napisane
obliczenia mog± byæ uruchamiane na dowolnej maszynie. Mechanizm jest
kompatybilny wstecz z istniej±cymi programami.

%package MA
Summary:	MA - a facility for dealing with masked arrays
Summary(pl):	Modu³ do obs³ugi macierzy niepe³nych
Group:		Development/Languages/Python
%requires_eq	python
Requires:	%{name} = %{version}

%description MA
Masked arrays are arrays that may have missing or invalid entries.
Module MA provides a work-alike replacement for Numeric that supports
data arrays with masks.

%description MA -l pl
Macierze niepe³ne s± to macierze, którym mo¿e brakowaæ lub mog±
zawieraæ niepoprawne warto¶ci. Modu³ MA zawiera odpowiednie narzêdzia
do operowania na tego typu macierzach.

%package Properties
Summary:	Property class implementation for Python
Summary(pl):	Implementacja klasy z w³a¶ciwo¶ciami dla jêzyka Python
Group:		Development/Languages/Python
%requires_eq	python
Requires:	%{name} = %{version}

%description Properties
PropertiedClass is a mixin class that can be used to emulate
properties in a Python class. A property is an attribute whose read,
write, or deleting requires special handling. It is also possible to
use this facility to prevent the writing or deleting of a property.

%description Properties -l pl
PropertiedClass jest klas±, która mo¿e byæ u¿yta do emulacji
w³a¶ciwo¶ci w klasach jêzyka Python. W³a¶ciwo¶æ klasy jest atrybutem,
którego czytanie, przypisywanie mu warto¶ci, czy te¿ jego usuwanie
powinno byæ traktowane w sposób specjalny. Mechanizm ten mo¿e byæ te¿
u¿ywany w celu ustalenia jakiego¶ atrybutu jako tylko do odczytu.

%package RNG
Summary:	Random Number Generator Object for NumPy
Summary:	Obiekt generatora liczb losowych dla modu³u NumPy
Group:		Development/Languages/Python
%requires_eq	python
Requires:	%{name} = %{version}

%description RNG
RNG provides a random number object to Numerical Python.

%description RNG -l pl
Modu³ ten zawiera implementacjê obiektu generatora liczb losowych dla
jêzyka Python.

%prep
%setup -q -n %{mname}-%{version}

%build
CC="%{__cc}"; export CC
CFLAGS="%{rpmcflags}"; export CFLAGS
python setup_all.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup_all.py install \
	--root=$RPM_BUILD_ROOT

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{py_sitedir}/%{mname}
%{py_sitedir}/%{mname}.pth
%attr(755,root,root) %{py_sitedir}/%{mname}/*.so
%{py_sitedir}/%{mname}/*.py[co]

%files devel
%defattr(644,root,root,755)
%{py_incdir}/%{mname}

%files FFT
%defattr(644,root,root,755)
%dir %{py_sitedir}/FFT
%attr(755,root,root) %{py_sitedir}/FFT/*.so
%{py_sitedir}/FFT/*.py[co]

%files kinds
%defattr(644,root,root,755)
%dir %{py_sitedir}/kinds
%attr(755,root,root) %{py_sitedir}/kinds/*.so
%{py_sitedir}/kinds/*.py[co]

%files MA
%defattr(644,root,root,755)
%dir %{py_sitedir}/MA
%{py_sitedir}/MA/*.py[co]

%files Properties
%defattr(644,root,root,755)
%dir %{py_sitedir}/PropertiedClasses
%{py_sitedir}/PropertiedClasses/*.py[co]

%files RNG
%defattr(644,root,root,755)
%dir %{py_sitedir}/RNG
%attr(755,root,root) %{py_sitedir}/RNG/*.so
%{py_sitedir}/RNG/*.py[co]
