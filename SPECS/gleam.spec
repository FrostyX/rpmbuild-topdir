%global debug_package %{nil}

Name: gleam
Version: 1.11.1
Release: 1%{?dist}
Summary: A friendly language for building type-safe, scalable systems!

License: Apache-2.0
URL: https://github.com/gleam-lang/gleam
Source: %{URL}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: cargo
BuildRequires: clippy
Requires: erlang


%description
Gleam is a general-purpose, concurrent, functional high-level programming
language that compiles to Erlang or JavaScript source code. Gleam is
a statically-typed language, which is different from the most popular languages
that run on Erlang’s virtual machine BEAM, Erlang and Elixir.


%prep
%autosetup


%build
%make_build


%install
%make_install
mkdir -p %{buildroot}/%{_bindir}/
cp -a target/release/%{name} %{buildroot}/%{_bindir}/


%check
# The `deno` tool is not packaged in Fedora so we are not running
# the tests for now
# make test


%files
%license LICENCE
%doc README.md
%doc CHANGELOG.md
%{_bindir}/%{name}


%changelog
* Thu Jun 05 2025 Jakub Kadlcik <frostyx@email.cz> - 1.11.1-1
- New upstream version

* Mon Jun 02 2025 Jakub Kadlcik <frostyx@email.cz> - 1.11.0-1
- New upstream version

* Tue Apr 15 2025 Jakub Kadlcik <frostyx@email.cz> - 1.10.0-1
- New upstream version

* Fri Mar 14 2025 Jakub Kadlcik <frostyx@email.cz> - 1.9.1-1
- New upstream version

* Mon Mar 10 2025 Jakub Kadlcik <frostyx@email.cz> - 1.9.0-1
- New upstream version

* Tue Feb 11 2025 Jakub Kadlcik <frostyx@email.cz> - 1.8.1-1
- New upstream version

* Sun Feb 09 2025 Jakub Kadlcik <frostyx@email.cz> - 1.8.0-1
- New upstream version

* Sun Jan 05 2025 Jakub Kadlcik <frostyx@email.cz> - 1.7.0-1
- New upstream version

* Tue Dec 03 2024 Jakub Kadlcik <frostyx@email.cz> - 1.6.3-1
- New upstream version

* Sat Nov 23 2024 Jakub Kadlcik <frostyx@email.cz> - 1.6.2-1
- New upstream version

* Tue Nov 19 2024 Jakub Kadlcik <frostyx@email.cz> - 1.6.1-1
- New upstream version

* Mon Nov 18 2024 Jakub Kadlcik <frostyx@email.cz> - 1.6.0-1
- New upstream version

* Fri Sep 27 2024 Jakub Kadlcik <frostyx@email.cz> - 1.5.1-1
- New upstream version

* Thu Sep 19 2024 Jakub Kadlcik <frostyx@email.cz> - 1.5.0-1
- New upstream version

* Sun Aug 04 2024 Jakub Kadlcik <frostyx@email.cz> - 1.4.1-1
- New upstream version

* Fri Aug 02 2024 Jakub Kadlcik <frostyx@email.cz> - 1.4.0-1
- New upstream version

* Fri Jul 12 2024 Jakub Kadlcik <frostyx@email.cz> - 1.3.2-1
- New upstream version

* Fri May 31 2024 Jakub Kadlcik <frostyx@email.cz> - 1.2.1-1
- New upstream version

* Mon May 27 2024 Jakub Kadlcik <frostyx@email.cz> - 1.2.0-1
- New upstream version

* Wed Apr 17 2024 Jakub Kadlcik <frostyx@email.cz> - 1.1.0-1
- New upstream version

* Sat Apr 13 2024 Jakub Kadlcik <frostyx@email.cz> 1.0.0-1
- Initial package
