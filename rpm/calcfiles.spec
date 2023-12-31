Name:           calcfiles
Version:        1.0
Release:        1%{?dist}
Summary:        Простой скрипт для подсчета файлов в каталоге
Requires:       unzip
License:        MIT
URL:            https://github.com/HoustonNFD/oc
Source0:        https://github.com/HoustonNFD/oc/archive/main.zip
BuildArch:      noarch

%description
calc_files.sh - это простой скрипт, который подсчитывает количество файлов в каталоге.

%prep
%autosetup -n oc-main

%install
mkdir -p %{buildroot}/usr/bin
install -m 755 %{_builddir}/oc-main/calc_files.sh %{buildroot}/usr/bin/calc_files

%files
/usr/bin/calc_files

%changelog
* Wed Dec 28 2023 Pavlo Khomenko <pasha9op@gmail.com> - 1.0-1
- Первоначальная сборка
