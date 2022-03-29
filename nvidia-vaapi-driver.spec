%global commit0 10a9f6a8b76367903b97ad430391f36ff6b1692b
%global date 20220327
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:           nvidia-vaapi-driver
Version:        0.0.5
Release:        4%{?shortcommit0:.%{date}git%{shortcommit0}}%{?dist}
Summary:        VA-API user mode driver for Nvidia GPUs
License:        MIT
URL:            https://github.com/elFarto/%{name}/

%if "%{?shortcommit0}"
Source0:        %{url}/archive/%{commit0}/%{name}-%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
%else
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
%endif

BuildRequires:  gcc
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
* Tue Mar 29 2022 Simone Caronni <negativo17@gmail.com> - 0.0.5-4.20220327git10a9f6a
- Update to latest snapshot.

* Sat Mar 12 2022 Simone Caronni <negativo17@gmail.com> - 0.0.5-3
- Backport libva check.

* Sat Feb 12 2022 Simone Caronni <negativo17@gmail.com> - 0.0.5-2
- Drop environment variables.

* Sat Feb 12 2022 Simone Caronni <negativo17@gmail.com> - 0.0.5-1
- First build.
