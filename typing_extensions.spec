#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : typing_extensions
Version  : 3.6.6
Release  : 3
URL      : https://files.pythonhosted.org/packages/fc/e6/3d2f306b12f01bde2861d67458d32c673e206d6fcc255537bf452db8f80c/typing_extensions-3.6.6.tar.gz
Source0  : https://files.pythonhosted.org/packages/fc/e6/3d2f306b12f01bde2861d67458d32c673e206d6fcc255537bf452db8f80c/typing_extensions-3.6.6.tar.gz
Summary  : Backported and Experimental Type Hints for Python 3.5+
Group    : Development/Tools
License  : Python-2.0
Requires: typing_extensions-license = %{version}-%{release}
Requires: typing_extensions-python = %{version}-%{release}
Requires: typing_extensions-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
The ``typing`` module was added to the standard library in Python 3.5 on
        a provisional basis and will no longer be provisional in Python 3.7. However,
        this means users of Python 3.5 - 3.6 who are unable to upgrade will not be
        able to take advantage of new types added to the ``typing`` module, such as
        ``typing.Text`` or ``typing.Coroutine``.
        
        The ``typing_extensions`` module contains both backports of these changes
        as well as experimental types that will eventually be added to the ``typing``
        module, such as ``Protocol``.
        
        Users of other Python versions should continue to install and use
        the ``typing`` module from PyPi instead of using this one unless specifically
        writing code that must be compatible with multiple Python versions or requires
        experimental types.

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

%description python3
python3 components for the typing_extensions package.


%prep
%setup -q -n typing_extensions-3.6.6

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1541544907
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/typing_extensions
cp LICENSE %{buildroot}/usr/share/package-licenses/typing_extensions/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/typing_extensions/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
