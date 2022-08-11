#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-pkginfo
Version  : 1.8.3
Release  : 16
URL      : https://files.pythonhosted.org/packages/00/91/fe0806e3ebded8c4e52f93ab4d963eef34bb33595c7aa7b5591d32ab5b92/pkginfo-1.8.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/00/91/fe0806e3ebded8c4e52f93ab4d963eef34bb33595c7aa7b5591d32ab5b92/pkginfo-1.8.3.tar.gz
Summary  : Query metadatdata from sdists / bdists / installed packages.
Group    : Development/Tools
License  : MIT
Requires: pypi-pkginfo-bin = %{version}-%{release}
Requires: pypi-pkginfo-license = %{version}-%{release}
Requires: pypi-pkginfo-python = %{version}-%{release}
Requires: pypi-pkginfo-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(py)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv

%description
==================
This package provides an API for querying the distutils metadata written in
the ``PKG-INFO`` file inside a source distriubtion (an ``sdist``) or a
binary distribution (e.g., created by running ``bdist_egg``).  It can
also query the ``EGG-INFO`` directory of an installed distribution, and
the ``*.egg-info`` stored in a "development checkout"
(e.g, created by running ``setup.py develop``).

%package bin
Summary: bin components for the pypi-pkginfo package.
Group: Binaries
Requires: pypi-pkginfo-license = %{version}-%{release}

%description bin
bin components for the pypi-pkginfo package.


%package license
Summary: license components for the pypi-pkginfo package.
Group: Default

%description license
license components for the pypi-pkginfo package.


%package python
Summary: python components for the pypi-pkginfo package.
Group: Default
Requires: pypi-pkginfo-python3 = %{version}-%{release}

%description python
python components for the pypi-pkginfo package.


%package python3
Summary: python3 components for the pypi-pkginfo package.
Group: Default
Requires: python3-core
Provides: pypi(pkginfo)

%description python3
python3 components for the pypi-pkginfo package.


%prep
%setup -q -n pkginfo-1.8.3
cd %{_builddir}/pkginfo-1.8.3
pushd ..
cp -a pkginfo-1.8.3 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656394535
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

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test || :
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-pkginfo
cp %{_builddir}/pkginfo-1.8.3/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-pkginfo/03162d5b27cb1ca3f768d50b3ea24877f6543dbd
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/pkginfo

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-pkginfo/03162d5b27cb1ca3f768d50b3ea24877f6543dbd

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
