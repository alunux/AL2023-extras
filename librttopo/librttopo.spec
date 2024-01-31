Name:           librttopo
Version:        1.1.0
Release:        12%{?dist}
Summary:        Create and manage SQL/MM topologies

License:        GPL-2.0-or-later
URL:            https://git.osgeo.org/gitea/rttopo/librttopo
Source0:        https://git.osgeo.org/gitea/rttopo/librttopo/archive/%{name}-%{version}.tar.gz
# Use pkgconfig to find geos
Patch0:        librttopo_geos.patch

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: gcc
BuildRequires: geos-devel
BuildRequires: libtool
BuildRequires: make

BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-gcc
BuildRequires: mingw32-geos

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-gcc
BuildRequires: mingw64-geos


%description
The RT Topology Library exposes an API to create and manage standard
(ISO 13249 aka SQL/MM) topologies using user-provided data stores.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package -n mingw32-%{name}
Summary:       MinGW Windows Leptonica library
BuildArch:     noarch

%description -n mingw32-%{name}
MinGW Windows %{name} library.


%package -n mingw64-%{name}
Summary:       MinGW Windows %{name} library
BuildArch:     noarch

%description -n mingw64-%{name}
MinGW Windows %{name} library.


%{?mingw_debug_package}


%prep
%autosetup -p1 -n %{name}


%build
autoreconf -ifv

# Native build
mkdir build_native
pushd build_native
%global _configure ../configure
%configure --disable-static
%make_build
popd

# MinGW build
MINGW32_CONFIGURE_ARGS="PKGCONFIG=%{mingw32_target}-pkg-config" \
MINGW64_CONFIGURE_ARGS="PKGCONFIG=%{mingw64_target}-pkg-config" \
%mingw_configure  --disable-static
%mingw_make_build


%install
%make_install -C build_native
%mingw_make_install

find %{buildroot} -name '*.la' -exec rm -f {} ';'


%mingw_debug_install_post


%files
%license COPYING
%doc CREDITS NEWS.md README.md TODO
%{_libdir}/%{name}.so.*

%files devel
%{_includedir}/%{name}.h
%{_includedir}/%{name}_geom.h
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/rttopo.pc

%files -n mingw32-%{name}
%license COPYING
%{mingw32_bindir}/%{name}-1.dll
%{mingw32_includedir}/%{name}.h
%{mingw32_includedir}/%{name}_geom.h
%{mingw32_libdir}/%{name}.dll.a
%{mingw32_libdir}/pkgconfig/rttopo.pc

%files -n mingw64-%{name}
%license COPYING
%{mingw64_bindir}/%{name}-1.dll
%{mingw64_includedir}/%{name}.h
%{mingw64_includedir}/%{name}_geom.h
%{mingw64_libdir}/%{name}.dll.a
%{mingw64_libdir}/pkgconfig/rttopo.pc

%changelog
* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 1.1.0-9
- Rebuild with mingw-gcc-12

* Thu Feb 24 2022 Sandro Mani <manisandro@gmail.com> - 1.1.0-8
- Make mingw subpackages noarch

* Sun Feb 20 2022 Sandro Mani <manisandro@gmail.com> - 1.1.0-7
- Add mingw subpackege

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Oct 21 2021 Sandro Mani <manisandro@gmail.com> - 1.1.0-5
- Rebuild (geos)

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Feb 13 2021 Sandro Mani <manisandro@gmail.com> - 1.1.0-3
- Rebuild (geos)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Nov 13 2020 Sandro Mani <manisandro@gmail.com> 1.1.0-1
- Initial package
