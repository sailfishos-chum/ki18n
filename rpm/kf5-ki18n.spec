%global kf5_version 5.116.0

Name: opt-kf5-ki18n
Version: 5.116.0
Release: 1%{?dist}
Summary: KDE Frameworks 5 Tier 1 addon for localization

License: LGPLv2+
URL:     https://invent.kde.org/frameworks/ki18n

Source0: %{name}-%{version}.tar.bz2

## upstream patches

%{?opt_kf5_default_filter}

BuildRequires:  opt-extra-cmake-modules >= %{kf5_version}
BuildRequires:  gettext
BuildRequires:  opt-kf5-rpm-macros >= %{kf5_version}
BuildRequires:  perl
BuildRequires:  python3-base
BuildRequires:  opt-qt5-qtbase-devel
BuildRequires:  opt-qt5-qtbase-private-devel
BuildRequires:  opt-qt5-qtdeclarative-devel
#BuildRequires:  opt-qt5-qtscript-devel

%{?_opt_qt5:Requires: %{_opt_qt5}%{?_isa} = %{_opt_qt5_version}}

%description
KDE Frameworks 5 Tier 1 addon for localization.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       gettext
Requires:       python3-base
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n %{name}-%{version}/upstream -p1


%build
export QTDIR=%{_opt_qt5_prefix}
touch .git

mkdir -p build
pushd build

%_opt_cmake_kf5 ../ \
   -DPYTHON_EXECUTABLE:PATH=%__python3
%make_build

popd

%install
pushd build
make DESTDIR=%{buildroot} install
popd

%find_lang %{name} --all-name


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%doc README.md
%license LICENSES/*.txt
%{_opt_kf5_libdir}/libKF5I18n.so.*
%{_opt_kf5_libdir}/libKF5I18nLocaleData.so.*
%{_opt_kf5_datadir}/qlogging-categories5/*ki18n*
%{_opt_kf5_qmldir}/org/kde/i18n/localeData/
%{_opt_kf5_qtplugindir}/kf5/ktranscript.so
%{_opt_kf5_datadir}/locale/
#lang(ca) %{_datadir}/locale/ca/LC_SCRIPTS/ki18n5/
#lang(ca@valencia) %{_datadir}/locale/ca@valencia/LC_SCRIPTS/ki18n5/
#lang(fi) %{_datadir}/locale/fi/LC_SCRIPTS/ki18n5/
#lang(gd) %{_datadir}/locale/gd/LC_SCRIPTS/ki18n5/
#lang(ja) %{_datadir}/locale/ja/LC_SCRIPTS/ki18n5/
#lang(ko) %{_datadir}/locale/ko/LC_SCRIPTS/ki18n5/
#lang(nb) %{_datadir}/locale/nb/LC_SCRIPTS/ki18n5/
#lang(nn) %{_datadir}/locale/nn/LC_SCRIPTS/ki18n5/
#lang(ru) %{_datadir}/locale/ru/LC_SCRIPTS/ki18n5/
#lang(sr) %{_datadir}/locale/sr/LC_SCRIPTS/ki18n5/
#lang(sr@ijekavian) %{_datadir}/locale/sr@ijekavian/LC_SCRIPTS/ki18n5/
#lang(sr@ijekavianlatin) %{_datadir}/locale/sr@ijekavianlatin/LC_SCRIPTS/ki18n5/
#lang(sr@latin) %{_datadir}/locale/sr@latin/LC_SCRIPTS/ki18n5/
#lang(sr) %{_datadir}/locale/uk/LC_SCRIPTS/ki18n5/

%files devel

%{_opt_kf5_includedir}/KF5/KI18n/
%{_opt_kf5_includedir}/KF5/KI18nLocaleData/
%{_opt_kf5_libdir}/libKF5I18n.so
%{_opt_kf5_libdir}/libKF5I18nLocaleData.so
%{_opt_kf5_libdir}/cmake/KF5I18n/
%{_opt_kf5_archdatadir}/mkspecs/modules/qt_KI18n.pri
