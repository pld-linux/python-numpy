
%define module numpy
%define mname Numeric

%define	python_ver	%(echo `python -c "import sys; print (sys.version[:3])"`)
%define	python_sitepkgsdir	%(echo `python -c "import sys; print (sys.prefix + '/lib/python' + sys.version[:3] + '/site-packages/')"`)
%define python_compile_opt python -O -c "import compileall; import sys; compileall.compile_dir(sys.argv[1])"
%define python_compile python -c "import compileall; import sys; compileall.compile_dir(sys.argv[1])"

Summary:	Python numerical facilities 
Summary(pl):	Modu³y do obliczeñ numerycznych dla jêzyka Python
Name:		python-%{module}
Version:	20.1.0a3
Release:	1
Copyright:	Distributable
Group:		Development/Languages/Python
Group(de):	Entwicklung/Sprachen/Python
Group(pl):	Programowanie/Jêzyki/Python
Source0:	http://prdownloads.sourceforge.net/numpy/%{mname}-%{version}.tar.gz
URL:		http://www.pfdubois.com/numpy/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	python >= 1.5
BuildRequires:	python-devel >= 1.5

%description
NumPy is a collection of extension modules to provide high-performance
multidimensional numeric arrays to the Python programming language.

%description -l pl
Pakiet zawiera wydajne modu³y dla jêzyka Python do obliczeñ numerycznych
na wielowymiarowych macierzach.

%package devel
Summary:	C header files for numerical modules
Summary(pl):	Pliki nag³ówkowe jêzyka C modu³ów numerycznych
Group:		Development/Languages/Python
Group(de):	Entwicklung/Sprachen/Python
Group(pl):	Programowanie/Jêzyki/Python
Requires:	%{name} = %{version}

%description devel
C header files for numerical modules.

%description devel -l pl
Pliki nag³ówkowe jêzyka C modu³ów numerycznych

%package FFT
Summary:	N/A
Group:		Development/Languages/Python
Group(de):	Entwicklung/Sprachen/Python
Group(pl):	Programowanie/Jêzyki/Python
Requires:	%{name} = %{version}

%description FFT
N/A

%package kinds
Summary:	N/A
Group:		Development/Languages/Python
Group(de):	Entwicklung/Sprachen/Python
Group(pl):	Programowanie/Jêzyki/Python
Requires:	%{name} = %{version}
Requires:	%{name}-kinds = %{version}

%description kinds
N/A

%package MA
Summary:	N/A
Group:		Development/Languages/Python
Group(de):	Entwicklung/Sprachen/Python
Group(pl):	Programowanie/Jêzyki/Python
Requires:	%{name} = %{version}

%description MA
N/A

%package Properties
Summary:	N/A
Group:		Development/Languages/Python
Group(de):	Entwicklung/Sprachen/Python
Group(pl):	Programowanie/Jêzyki/Python
Requires:	%{name} = %{version}

%description Properties
N/A

%package RNG
Summary:	Random Number Generator Objects for NumPy
Group:		Development/Languages/Python
Group(de):	Entwicklung/Sprachen/Python
Group(pl):	Programowanie/Jêzyki/Python
Requires:	%{name} = %{version}

%description RNG
RNG provides a random number object to Numerical Python.

%prep
%setup -q -n %{mname}-%{version}

%build
python setup_all.py build

%install
python setup_all.py install --root=$RPM_BUILD_ROOT
%python_compile_opt $RPM_BUILD_ROOT%{python_sitepkgsdir}
%python_compile $RPM_BUILD_ROOT%{python_sitepkgsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{python_sitepkgsdir}/%{mname}
%{python_sitepkgsdir}/%{mname}.pth
%attr(755,root,root) %{python_sitepkgsdir}/%{mname}/*.so
%{python_sitepkgsdir}/%{mname}/*.py?

%files devel
%defattr(644,root,root,755)
%{_includedir}/python%{python_ver}/%{mname}

%files FFT
%defattr(644,root,root,755)
%dir %{python_sitepkgsdir}/FFT
%attr(755,root,root) %{python_sitepkgsdir}/FFT/*.so
%{python_sitepkgsdir}/FFT/*.py?

%files kinds
%defattr(644,root,root,755)
%dir %{python_sitepkgsdir}/kinds
%attr(755,root,root) %{python_sitepkgsdir}/kinds/*.so
%{python_sitepkgsdir}/kinds/*.py?

%files MA
%defattr(644,root,root,755)
%dir %{python_sitepkgsdir}/MA
%{python_sitepkgsdir}/MA/*.py?

%files Properties
%defattr(644,root,root,755)
%{python_sitepkgsdir}/Properties.pyc
%{python_sitepkgsdir}/Properties.pyo

%files RNG
%defattr(644,root,root,755)
%dir %{python_sitepkgsdir}/RNG
%attr(755,root,root) %{python_sitepkgsdir}/RNG/*.so
%{python_sitepkgsdir}/RNG/*.py?
