Name:           python-xkbcommon
Version:        0.8
Release:        2%{?dist}
Summary:        Bindings for libxkbcommon using cffi

License:        MIT
URL:            https://github.com/sde1000/python-xkbcommon
Source:         %{pypi_source xkbcommon}

BuildRequires:  python3-devel
BuildRequires:  gcc
BuildRequires:  libxkbcommon-devel

Requires:  libxkbcommon


%global _description %{expand:
Python bindings for libxkbcommon using cffi.}


%description %_description

%package -n     python3-xkbcommon
Summary:        %{summary}

%description -n python3-xkbcommon %_description


%prep
%autosetup -p1 -n xkbcommon-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files xkbcommon


%check
%pyproject_check_import -t


%files -n python3-xkbcommon -f %{pyproject_files}


%changelog
* Sat Jul 22 2023 Jakub Kadlcik <frostyx@email.cz> - 0.8-2
- Remove wildcard from pyproject_save_files

* Sat Jul 22 2023 Jakub Kadlcik <frostyx@email.cz> - 0.8-1
- Update to a new upstream version

* Tue Jun 14 2022 Jakub Kadlcik <frostyx@email.cz> - 0.4-1
- Initial package
