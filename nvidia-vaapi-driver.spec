#global commit0 62a571c6c8ac3c07c13c1f73c4a8adcd3eb5710d
#global date 20220514
#global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:           nvidia-vaapi-driver
Version:        0.0.6
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
BuildRequires:  mesa-libEGL-devel
BuildRequires:  meson >= 0.58.0
BuildRequires:  nv-codec-headers >= 11.1.5.1
BuildRequires:  pkgconfig(gstreamer-codecparsers-1.0)
BuildRequires:  pkgconfig(libva) >= 1.8.0

Conflicts:      libva-vdpau-driver%{?_isa}

Requires:       libva%{?_isa}
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
