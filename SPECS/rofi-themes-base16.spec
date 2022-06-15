Name: rofi-themes-base16
Version: 0.1.0
Release: 2%{?dist}
Summary: Base16 themes for rofi
BuildArch: noarch

License: MIT
URL: https://github.com/jordiorlando/base16-rofi
Source0: %{URL}/archive/v%{version}/%{name}-%{version}.tar.gz

Requires: rofi
Requires: rofi-themes


%description
A collection of base16 themes for rofi


%prep
%setup -q -n base16-rofi-%{version}

# Remove executable bits from rasi and config files
# https://github.com/jordiorlando/base16-rofi/pull/16
chmod -x themes/*.rasi
chmod -x themes/*.config


%build


%install
mkdir -p %{buildroot}/%{_datadir}/rofi/themes
cp -rp themes/* %{buildroot}/%{_datadir}/rofi/themes


%files
%license LICENSE
%doc README.md
%{_datadir}/rofi/themes/base16-*


%changelog
* Thu Dec 30 2021 Jakub Kadlcik <jkadlcik@redhat.com> - 0.1.0-2
- Preserve timestamps when installing files
- Remove special characters from my name
- Depend on rofi-themes to prevent /usr/share/rofi/themes/ ownership conflicts

* Mon Nov 22 2021 Jakub Kadlcik <jkadlcik@redhat.com> - 0.1.0-1
- Upstream released first version

* Thu Nov 18 2021 Jakub Kadlcik <jkadlcik@redhat.com> - 0-2
- Rebuild from a7e7be0cb5812243f23cd4607eab11ce4cca7774

* Thu Nov 18 2021 Jakub Kadlcik <jkadlcik@redhat.com> - 0-1
- Initial package
