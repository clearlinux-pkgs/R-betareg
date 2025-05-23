#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v25
# autospec commit: 9594167
#
Name     : R-betareg
Version  : 3.2.3
Release  : 60
URL      : https://ftp.osuosl.org/pub/cran/src/contrib/betareg_3.2-3.tar.gz
Source0  : https://ftp.osuosl.org/pub/cran/src/contrib/betareg_3.2-3.tar.gz
Summary  : Beta Regression
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0
Requires: R-betareg-lib = %{version}-%{release}
Requires: R-Formula
Requires: R-flexmix
Requires: R-lmtest
Requires: R-modeltools
Requires: R-sandwich
BuildRequires : R-Formula
BuildRequires : R-flexmix
BuildRequires : R-lmtest
BuildRequires : R-modeltools
BuildRequires : R-partykit
BuildRequires : R-sandwich
BuildRequires : R-strucchange
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
<img src="https://topmodels.R-Forge.R-project.org/betareg/betareg.png" align="right" alt="countreg logo" width="100" />

%package lib
Summary: lib components for the R-betareg package.
Group: Libraries

%description lib
lib components for the R-betareg package.


%prep
%setup -q -n betareg
pushd ..
cp -a betareg buildavx2
popd
pushd ..
cp -a betareg buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1747066358

%install
export SOURCE_DATE_EPOCH=1747066358
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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
/usr/lib64/R/library/betareg/NEWS.md
/usr/lib64/R/library/betareg/R/betareg
/usr/lib64/R/library/betareg/R/betareg.rdb
/usr/lib64/R/library/betareg/R/betareg.rdx
/usr/lib64/R/library/betareg/data/CarTask.rda
/usr/lib64/R/library/betareg/data/FoodExpenditure.rda
/usr/lib64/R/library/betareg/data/GasolineYield.rda
/usr/lib64/R/library/betareg/data/ImpreciseTask.rda
/usr/lib64/R/library/betareg/data/LossAversion.rda
/usr/lib64/R/library/betareg/data/MockJurors.rda
/usr/lib64/R/library/betareg/data/ReadingSkills.rda
/usr/lib64/R/library/betareg/data/StressAnxiety.rda
/usr/lib64/R/library/betareg/data/WeatherTask.rda
/usr/lib64/R/library/betareg/demo/SmithsonVerkuilen2006.R
/usr/lib64/R/library/betareg/doc/betareg-ext.R
/usr/lib64/R/library/betareg/doc/betareg-ext.html
/usr/lib64/R/library/betareg/doc/betareg-ext.qmd
/usr/lib64/R/library/betareg/doc/betareg.R
/usr/lib64/R/library/betareg/doc/betareg.html
/usr/lib64/R/library/betareg/doc/betareg.qmd
/usr/lib64/R/library/betareg/doc/index.html
/usr/lib64/R/library/betareg/help/AnIndex
/usr/lib64/R/library/betareg/help/aliases.rds
/usr/lib64/R/library/betareg/help/betareg.rdb
/usr/lib64/R/library/betareg/help/betareg.rdx
/usr/lib64/R/library/betareg/help/figures/README-plot-1.png
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

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/R/library/betareg/libs/betareg.so
/V4/usr/lib64/R/library/betareg/libs/betareg.so
/usr/lib64/R/library/betareg/libs/betareg.so
