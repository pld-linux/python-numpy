Summary:	Python numerical facilities 
Name:		python-numpy
Version:	1.8 
Release:	1
Copyright:	Distributable
Group:		Development/Languages/Python
Group(de):	Entwicklung/Sprachen/Python
Group(pl):	Programowanie/Jêzyki/Python
Source0:	LLNLPython.tgz
Source1:	Makefile.pre.in
Patch0:		LLNLPython8-fixbugs.patch
Patch1:		LLNLPython8-fixdirs.patch
URL:		http://www.python.org/topics/scicomp/numpy.html
Icon:		linux-python-numpy-icon.gif 
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	python >= 1.5

%description
NumPy is a collection of extension modules to provide high-performance
multidimensional numeric arrays to the Python programming language.

%package gist
Summary:	Xlib-based plotting for NumPy
Group:		Development/Languages/Python
Group(de):	Entwicklung/Sprachen/Python
Group(pl):	Programowanie/Jêzyki/Python
Requires:	yorick >= 1.4, python-numpy >= 1.5

%description gist
Gist is an extension of python that allows plotting of arbitrary NumPy
arrays. Both 2-D and 3-D plotting is available. You can get started
with online help from within python using
  >>> from gist import *
  >>> help("help.")
  >>> help("gist.")

%package RNG
Summary:	Random Number Generator Objects for NumPy
Group:		Development/Languages/Python
Group(de):	Entwicklung/Sprachen/Python
Group(pl):	Programowanie/Jêzyki/Python
Requires:	python-numpy >= 1.5

%description RNG
RNG provides a random number object to Numerical Python.

%prep
%setup -q -n LLNLPython8/
%patch0 -p1
%patch1 -p1

%build
cd Numerical
cp -f %{SOURCE1} .
%{__make} -f Makefile.pre.in boot
%{__make} OPT="%{rpmcflags}"

cd $RPM_BUILD_DIR/LLNLPython8/Graphics
cp -f %{SOURCE1} .
%{__make} -f Makefile.pre.in boot
%{__make} OPT="%{rpmcflags}"

cd $RPM_BUILD_DIR/LLNLPython8/RNG
cp -f %{SOURCE1} .
%{__make} -f Makefile.pre.in boot
%{__make} OPT="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
cd Numerical
install -d $RPM_BUILD_ROOT%{_includedir}/python1.5
install Include/* $RPM_BUILD_ROOT%{_includedir}/python1.5
install -d $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/NumPy
install *.so $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/NumPy
install Lib/* $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/NumPy
echo "NumPy" > $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/NumPy.pth

cd ../Graphics
install -d $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/Graphics
install *.so $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/Graphics
install Gist/Lib/*.py Gist/Lib/*.help $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/Graphics
install Gist/Demo/*.* Gist3D/Demo/*.* OOG/Demo/*.* $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/Graphics
install Gist3D/Lib/*.py $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/Graphics
install OOG/Lib/*.py $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/Graphics
install Arrayfcns/Lib/*.py $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/Graphics
echo "Graphics" > $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/Graphics.pth

cd ../RNG
install -d $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/RNG
install *.so $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/RNG
install Lib/*.py $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/RNG
echo "RNG" > $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/RNG.pth

%clean
rm -rf $RPM_BUILD_ROOT

%post
if ! grep "^%{_libdir}/python1.5/site-packages/NumPy\$" /etc/ld.so.conf > /dev/null; then
	echo "%{_libdir}/python1.5/site-packages/NumPy" >> /etc/ld.so.conf
fi
ldconfig -v

%files
%defattr(644,root,root,755)
%doc Numerical/Doc Numerical/Demo Numerical/Test  
%{_libdir}/python1.5/site-packages/NumPy.pth
%{_libdir}/python1.5/site-packages/NumPy
%{_includedir}/python1.5/arrayobject.h
%{_includedir}/python1.5/f2c.h
%{_includedir}/python1.5/fftpack.h
%{_includedir}/python1.5/ranlib.h
%{_includedir}/python1.5/ufuncobject.h

%files gist
%defattr(644,root,root,755)
%{_libdir}/python1.5/site-packages/Graphics.pth
%{_libdir}/python1.5/site-packages/Graphics

%files RNG
%defattr(644,root,root,755)
%doc RNG/Demo
%{_libdir}/python1.5/site-packages/RNG.pth
%{_libdir}/python1.5/site-packages/RNG
