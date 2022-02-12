Name:           nvidia-vaapi-driver
Version:        0.0.5
Release:        1%{?dist}
Summary:        VA-API user mode driver for Nvidia GPUs
License:        MIT
URL:            https://github.com/elFarto/%{name}/

Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        nvidia-vaapi.sh

BuildRequires:  gcc
BuildRequires:  meson >= 0.58.0
#BuildRequires:  mesa-libEGL-devel
BuildRequires:  nv-codec-headers >= 11.1.5.1
BuildRequires:  pkgconfig(gstreamer-codecparsers-1.0)

Conflicts:      libva-vdpau-driver%{?_isa}

Requires:       libva%{?_isa}

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

# Temporary until libva knows about the driver
install -m 0755 -p -D %{SOURCE1} %{buildroot}%{_sysconfdir}/profile.d/nvidia-vaapi.sh

%files
%license COPYING
%doc README.md
%{_libdir}/dri/nvidia_drv_video.so
%config(noreplace) %{_sysconfdir}/profile.d/nvidia-vaapi.sh

%changelog
* Sat Feb 12 2022 Simone Caronni <negativo17@gmail.com> - 0.0.5-1
- First build.
