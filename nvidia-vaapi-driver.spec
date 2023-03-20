%global commit0 c0a7f54e3fa6b43a5a04e7bf147251dfca6897aa
%global date 20230319
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:           nvidia-vaapi-driver
Version:        0.0.9
Release:        1%{?shortcommit0:.%{date}git%{shortcommit0}}%{?dist}
Summary:        VA-API user mode driver for Nvidia GPUs
License:        MIT
URL:            https://github.com/elFarto/%{name}/

%if "%{?shortcommit0}"
Source0:        %{url}/archive/%{commit0}/%{name}-%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
%else
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
%endif

BuildRequires:  gcc
# gettid() available from glibc 2.30:
BuildRequires:  glibc-devel >= 2.30
BuildRequires:  meson >= 0.58.0
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(ffnvcodec) >= 11.1.5.1
BuildRequires:  pkgconfig(gstreamer-codecparsers-1.0)
BuildRequires:  pkgconfig(libdrm) >= 2.4.60
BuildRequires:  pkgconfig(libva) >= 1.8.0

Conflicts:      libva-vdpau-driver%{?_isa}

Requires:       mesa-filesystem

%description
This is a VA-API implementation that uses NVDEC as a backend. This
implementation is specifically designed to be used by Firefox for accelerated
decode of web content, and may not operate correctly in other applications.

%prep
%if "%{?shortcommit0}"
%autosetup -n %{name}-%{commit0}
%else
%autosetup
%endif

%build
%meson
%meson_build

%install
%meson_install

%files
%license COPYING
%doc README.md
%{_libdir}/dri/nvidia_drv_video.so

%changelog
* Mon Mar 20 2023 Simone Caronni <negativo17@gmail.com> - 0.0.9-1.20230319gitc0a7f54
- Update to latest snapshot.

* Mon Feb 06 2023 Simone Caronni <negativo17@gmail.com> - 0.0.8-2.20230205git17c62b8
- Add latest fixes.

* Sat Feb 04 2023 Simone Caronni <negativo17@gmail.com> - 0.0.8-1.20230131git2bb71a5
- Rebase to latest snapshot.

* Tue Oct 25 2022 Simone Caronni <negativo17@gmail.com> - 0.0.7-1.20221024git4992e29
- Update to latest 0.0.7 snapshot.

* Sun Sep 04 2022 Simone Caronni <negativo17@gmail.com> - 0.0.6-2.20220827gitdbf585a
- Update to latest snapshot.

* Thu May 26 2022 Simone Caronni <negativo17@gmail.com> - 0.0.6-1
- Same version has been promoted to 0.0.6 (no other change).

* Sun May 15 2022 Simone Caronni <negativo17@gmail.com> - 0.0.5-6.20220514git62a571c
- Updated to latest snapshot.

* Tue Apr 12 2022 Simone Caronni <negativo17@gmail.com> - 0.0.5-5.20220411git51aaf5e
- Update to latest snapshot.

* Tue Mar 29 2022 Simone Caronni <negativo17@gmail.com> - 0.0.5-4.20220327git10a9f6a
- Update to latest snapshot.

* Sat Mar 12 2022 Simone Caronni <negativo17@gmail.com> - 0.0.5-3
- Backport libva check.

* Sat Feb 12 2022 Simone Caronni <negativo17@gmail.com> - 0.0.5-2
- Drop environment variables.

* Sat Feb 12 2022 Simone Caronni <negativo17@gmail.com> - 0.0.5-1
- First build.
