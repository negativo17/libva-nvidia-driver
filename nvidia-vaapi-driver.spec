Name:           nvidia-vaapi-driver
Version:        0.0.5
Release:        3%{?dist}
Summary:        VA-API user mode driver for Nvidia GPUs
License:        MIT
URL:            https://github.com/elFarto/%{name}/

Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         %{name}-libva-dep.patch

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
%autosetup -p1

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
* Sat Mar 12 2022 Simone Caronni <negativo17@gmail.com> - 0.0.5-3
- Backport libva check.

* Sat Feb 12 2022 Simone Caronni <negativo17@gmail.com> - 0.0.5-2
- Drop environment variables.

* Sat Feb 12 2022 Simone Caronni <negativo17@gmail.com> - 0.0.5-1
- First build.
