Name:           update-desktop-files
Version:        12.1
Release:        0
Summary:        A Build Tool to Update Desktop Files
License:        GPL-2.0+
Group:          Development/Tools/Building
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source:         tizen_update_desktop_file.sh
Source1:        map-desktop-category.sh
Source2:        macro
Source4:        brp-trim-desktop.sh
# This is not true technically, but we do that to make the rpm macros from
# desktop-file-utils available to most packages that ship a .desktop file
# (since they already have a update-desktop-files BuildRequires).
Requires:       desktop-file-utils
BuildArch:      noarch

%description
This package provides further translations and a shell script to update
desktop files. It is used by the %%tizen_update_desktop_file rpm macro.

%package -n brp-trim-desktopfiles
Summary:        Trim translations from .deskop files
Group:          Development/Tools/Building

%description -n brp-trim-desktopfiles
Trim translations from all .deskop files found in build root

%prep
%setup -q -n . -D -T 0
mkdir %name
cd %name

%build

%install
mkdir -p $RPM_BUILD_ROOT%_rpmconfigdir
install -m0755 %SOURCE0 %SOURCE1 $RPM_BUILD_ROOT%_rpmconfigdir
install -m0644 -D %SOURCE2 $RPM_BUILD_ROOT/etc/rpm/macros.%name
install -m0755 -D %SOURCE4 $RPM_BUILD_ROOT/usr/lib/rpm/brp-tizen.d/brp-70-trim-desktopfiles

%files
%defattr(-,root,root)
%_rpmconfigdir/*
%exclude %_rpmconfigdir/brp-tizen.d
/etc/rpm/*

%files -n brp-trim-desktopfiles
%defattr(-,root,root)
%_rpmconfigdir/brp-tizen.d

%changelog
