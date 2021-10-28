#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : typing_extensions
Version  : 3.10.0.2
Release  : 32
URL      : https://files.pythonhosted.org/packages/ed/12/c5079a15cf5c01d7f4252b473b00f7e68ee711be605b9f001528f0298b98/typing_extensions-3.10.0.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/ed/12/c5079a15cf5c01d7f4252b473b00f7e68ee711be605b9f001528f0298b98/typing_extensions-3.10.0.2.tar.gz
Summary  : Backported and Experimental Type Hints for Python 3.5+
Group    : Development/Tools
License  : Python-2.0
Requires: typing_extensions-license = %{version}-%{release}
Requires: typing_extensions-python = %{version}-%{release}
Requires: typing_extensions-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
=================
Typing Extensions
=================
.. image:: https://badges.gitter.im/python/typing.svg
:alt: Chat at https://gitter.im/python/typing
:target: https://gitter.im/python/typing?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge

%package license
Summary: license components for the typing_extensions package.
Group: Default

%description license
license components for the typing_extensions package.


%package python
Summary: python components for the typing_extensions package.
Group: Default
Requires: typing_extensions-python3 = %{version}-%{release}

%description python
python components for the typing_extensions package.


%package python3
Summary: python3 components for the typing_extensions package.
Group: Default
Requires: python3-core
Provides: pypi(typing_extensions)

%description python3
python3 components for the typing_extensions package.


%prep
%setup -q -n typing_extensions-3.10.0.2
cd %{_builddir}/typing_extensions-3.10.0.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1630363292
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/typing_extensions
cp %{_builddir}/typing_extensions-3.10.0.2/LICENSE %{buildroot}/usr/share/package-licenses/typing_extensions/7ad627868f90ad068bd06801aab97ec1ca34b890
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/typing_extensions/7ad627868f90ad068bd06801aab97ec1ca34b890

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
