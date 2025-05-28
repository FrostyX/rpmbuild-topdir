Name:           python-dbus-fast
Version:        2.21.1
Release:        0.01%{?dist}
Summary:        A faster version of dbus-next

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/bluetooth-devices/dbus-fast
Source:         %{pypi_source dbus_fast}

BuildRequires:  python3-devel
BuildRequires:  gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'dbus-fast' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-dbus-fast
Summary:        %{summary}

%description -n python3-dbus-fast %_description


%prep
%autosetup -p1 -n dbus_fast-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python3-dbus-fast -f %{pyproject_files}


%changelog
* Mon Feb 5 2024 Brian J. Murrell <brian@interlinx.bc.ca> - 2.21.1-0.01
- Initial creation
