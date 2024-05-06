%global upstream_name nvidia-vaapi-driver

Name:           libva-nvidia-driver
Epoch:          1
Version:        0.0.12
Release:        1%{?dist}
Summary:        VA-API user mode driver for Nvidia GPUs
License:        MIT
URL:            https://github.com/elFarto/%{upstream_name}

Source0:        %{url}/archive/v%{version}/%{upstream_name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  meson >= 0.58.0
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(ffnvcodec) >= 11.1.5.1
%if 0%{?fedora} || 0%{?rhel} >= 9
BuildRequires:  pkgconfig(gstreamer-codecparsers-1.0)
%endif
BuildRequires:  pkgconfig(libdrm) >= 2.4.60
BuildRequires:  pkgconfig(libva) >= 1.8.0

Conflicts:      libva-vdpau-driver%{?_isa}
Obsoletes:      %{upstream_name} < 0.0.10-3
Provides:       %{upstream_name} = %{version}-%{release}
# Alternative name that better describes the API involved
Provides:       nvdec-vaapi-driver = %{version}-%{release}

Requires:       mesa-filesystem

%description
This is a VA-API implementation that uses NVDEC as a backend. This
implementation is specifically designed to be used by Firefox for accelerated
decode of web content, and may not operate correctly in other applications.

%prep
%autosetup -n %{upstream_name}-%{version}

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files
%license COPYING
%doc README.md
%{_libdir}/dri/nvidia_drv_video.so

%changelog
* Mon May 06 2024 Simone Caronni <negativo17@gmail.com> - 1:0.0.12-1
- Update to 0.0.12.
- Trim changelog.
- Clean up SPEC file, allow it to build for EL8.

* Wed Nov 08 2023 Simone Caronni <negativo17@gmail.com> - 0.0.11-1
- Update to 0.0.11.
- Rename to libva-nvidia-driver, as in main Fedora repository.

* Wed Jun 28 2023 Simone Caronni <negativo17@gmail.com> - 0.0.10-1
- Update to 0.0.10.

* Mon Mar 20 2023 Simone Caronni <negativo17@gmail.com> - 0.0.9-1.20230319gitc0a7f54
- Update to latest snapshot.

* Mon Feb 06 2023 Simone Caronni <negativo17@gmail.com> - 0.0.8-2.20230205git17c62b8
- Add latest fixes.

* Sat Feb 04 2023 Simone Caronni <negativo17@gmail.com> - 0.0.8-1.20230131git2bb71a5
- Rebase to latest snapshot.
