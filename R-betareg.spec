#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-betareg
Version  : 3.1.4
Release  : 37
URL      : https://cran.r-project.org/src/contrib/betareg_3.1-4.tar.gz
Source0  : https://cran.r-project.org/src/contrib/betareg_3.1-4.tar.gz
Summary  : Beta Regression
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0
Requires: R-Formula
Requires: R-flexmix
Requires: R-lmtest
Requires: R-modeltools
Requires: R-partykit
Requires: R-sandwich
Requires: R-strucchange
BuildRequires : R-Formula
BuildRequires : R-flexmix
BuildRequires : R-lmtest
BuildRequires : R-modeltools
BuildRequires : R-partykit
BuildRequires : R-sandwich
BuildRequires : R-strucchange
BuildRequires : buildreq-R

%description
In addition to maximum likelihood regression (for both mean and precision of a beta-distributed
  response), bias-corrected and bias-reduced estimation as well as finite mixture models and
  recursive partitioning for beta regressions are provided.

%prep
%setup -q -c -n betareg
cd %{_builddir}/betareg

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1612909784

%install
export SOURCE_DATE_EPOCH=1612909784
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
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library betareg
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library betareg
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library betareg
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc betareg || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/betareg/CITATION
/usr/lib64/R/library/betareg/DESCRIPTION
/usr/lib64/R/library/betareg/INDEX
/usr/lib64/R/library/betareg/Meta/Rd.rds
/usr/lib64/R/library/betareg/Meta/data.rds
/usr/lib64/R/library/betareg/Meta/demo.rds
/usr/lib64/R/library/betareg/Meta/features.rds
/usr/lib64/R/library/betareg/Meta/hsearch.rds
/usr/lib64/R/library/betareg/Meta/links.rds
/usr/lib64/R/library/betareg/Meta/nsInfo.rds
/usr/lib64/R/library/betareg/Meta/package.rds
/usr/lib64/R/library/betareg/Meta/vignette.rds
/usr/lib64/R/library/betareg/NAMESPACE
/usr/lib64/R/library/betareg/NEWS
/usr/lib64/R/library/betareg/R/betareg
/usr/lib64/R/library/betareg/R/betareg.rdb
/usr/lib64/R/library/betareg/R/betareg.rdx
/usr/lib64/R/library/betareg/data/CarTask.rda
/usr/lib64/R/library/betareg/data/FoodExpenditure.rda
/usr/lib64/R/library/betareg/data/GasolineYield.rda
/usr/lib64/R/library/betareg/data/ImpreciseTask.rda
/usr/lib64/R/library/betareg/data/MockJurors.rda
/usr/lib64/R/library/betareg/data/ReadingSkills.rda
/usr/lib64/R/library/betareg/data/StressAnxiety.rda
/usr/lib64/R/library/betareg/data/WeatherTask.rda
/usr/lib64/R/library/betareg/demo/SmithsonVerkuilen2006.R
/usr/lib64/R/library/betareg/doc/betareg-ext.R
/usr/lib64/R/library/betareg/doc/betareg-ext.Rnw
/usr/lib64/R/library/betareg/doc/betareg-ext.pdf
/usr/lib64/R/library/betareg/doc/betareg.R
/usr/lib64/R/library/betareg/doc/betareg.Rnw
/usr/lib64/R/library/betareg/doc/betareg.pdf
/usr/lib64/R/library/betareg/doc/index.html
/usr/lib64/R/library/betareg/help/AnIndex
/usr/lib64/R/library/betareg/help/aliases.rds
/usr/lib64/R/library/betareg/help/betareg.rdb
/usr/lib64/R/library/betareg/help/betareg.rdx
/usr/lib64/R/library/betareg/help/paths.rds
/usr/lib64/R/library/betareg/html/00Index.html
/usr/lib64/R/library/betareg/html/R.css
/usr/lib64/R/library/betareg/tests/Examples/betareg-Ex.Rout.save
/usr/lib64/R/library/betareg/tests/betamix.R
/usr/lib64/R/library/betareg/tests/betamix.Rout.save
/usr/lib64/R/library/betareg/tests/betatree.R
/usr/lib64/R/library/betareg/tests/betatree.Rout.save
/usr/lib64/R/library/betareg/tests/bias.R
/usr/lib64/R/library/betareg/tests/bias.Rout.save
