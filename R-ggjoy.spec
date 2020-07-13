#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-ggjoy
Version  : 0.4.1
Release  : 28
URL      : https://cran.r-project.org/src/contrib/ggjoy_0.4.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/ggjoy_0.4.1.tar.gz
Summary  : Joyplots in 'ggplot2'
Group    : Development/Tools
License  : GPL-2.0
Requires: R-ggplot2
Requires: R-ggridges
BuildRequires : R-ggplot2
BuildRequires : R-ggridges
BuildRequires : buildreq-R

%description
ggjoy
=====
[![Build Status](https://travis-ci.org/clauswilke/ggjoy.svg?branch=master)](https://travis-ci.org/clauswilke/ggjoy) [![Coverage Status](https://img.shields.io/codecov/c/github/clauswilke/ggjoy/master.svg)](https://codecov.io/github/clauswilke/ggjoy?branch=master) [![CRAN\_Status\_Badge](http://www.r-pkg.org/badges/version/ggjoy)](https://CRAN.R-project.org/package=ggjoy) [![CRAN\_Downloads\_Badge](http://cranlogs.r-pkg.org/badges/ggjoy)](http://cranlogs.r-pkg.org/downloads/total/last-month/ggjoy)

%prep
%setup -q -c -n ggjoy
cd %{_builddir}/ggjoy

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1589768617

%install
export SOURCE_DATE_EPOCH=1589768617
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library ggjoy
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library ggjoy
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library ggjoy
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc ggjoy || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/ggjoy/DESCRIPTION
/usr/lib64/R/library/ggjoy/INDEX
/usr/lib64/R/library/ggjoy/LICENSE
/usr/lib64/R/library/ggjoy/Meta/Rd.rds
/usr/lib64/R/library/ggjoy/Meta/features.rds
/usr/lib64/R/library/ggjoy/Meta/hsearch.rds
/usr/lib64/R/library/ggjoy/Meta/links.rds
/usr/lib64/R/library/ggjoy/Meta/nsInfo.rds
/usr/lib64/R/library/ggjoy/Meta/package.rds
/usr/lib64/R/library/ggjoy/Meta/vignette.rds
/usr/lib64/R/library/ggjoy/NAMESPACE
/usr/lib64/R/library/ggjoy/NEWS
/usr/lib64/R/library/ggjoy/R/ggjoy
/usr/lib64/R/library/ggjoy/R/ggjoy.rdb
/usr/lib64/R/library/ggjoy/R/ggjoy.rdx
/usr/lib64/R/library/ggjoy/doc/index.html
/usr/lib64/R/library/ggjoy/doc/introduction.Rmd
/usr/lib64/R/library/ggjoy/doc/introduction.html
/usr/lib64/R/library/ggjoy/help/AnIndex
/usr/lib64/R/library/ggjoy/help/aliases.rds
/usr/lib64/R/library/ggjoy/help/ggjoy.rdb
/usr/lib64/R/library/ggjoy/help/ggjoy.rdx
/usr/lib64/R/library/ggjoy/help/paths.rds
/usr/lib64/R/library/ggjoy/html/00Index.html
/usr/lib64/R/library/ggjoy/html/R.css
