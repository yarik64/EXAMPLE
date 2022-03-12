%define _unpackaged_files_terminate_build 1

Name: example
Version: 0.1.0
Release: alt1

Summary: Example application
License: GPLv2+
Group: Other
Url: https://github.com/

BuildRequires: cmake cmake-modules rpm-macros-cmake gcc-c++ qt5-base-devel qt5-declarative-devel qt5-tools-devel qt5-base-common doxygen
BuildRequires: desktop-file-utils ImageMagick-tools

Source0: %name-%version.tar

%description
Example of qt widget application.

%prep
%setup -q

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

cd %_cmake__builddir
desktop-file-install --dir=%buildroot%_desktopdir \
                     --set-key Exec --set-value %_bindir/example-main \
                     ../setup/example.desktop

for size in 48 64 128 256 512; do
    mkdir -p %buildroot%_datadir/icons/hicolor/''${size}x''${size}/apps/
    convert ../setup/logo_1024_1024.png -resize ''${size}x''${size} \
    %buildroot%_datadir/icons/hicolor/''${size}x''${size}/apps/example.png
done

%files
%doc README.md
%doc INSTALL.md
%_bindir/example-main

%_libdir/libexample-gui.so

%_datadir/icons/hicolor/48x48/apps/example.png
%_datadir/icons/hicolor/64x64/apps/example.png
%_datadir/icons/hicolor/128x128/apps/example.png
%_datadir/icons/hicolor/256x256/apps/example.png
%_datadir/icons/hicolor/512x512/apps/example.png

%_desktopdir/example.desktop

%changelog
* Mon Jul 05 2021 Evgeny Sinelnikov <sin@altlinux.org> 0.1.0-alt1
- Initial build
