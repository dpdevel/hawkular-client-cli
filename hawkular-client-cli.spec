%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}

Name:           hawkular-client-cli
Version:        0.18.4
Release:        1%{?dist}
Summary:        Read/Write data to and from a Hawkular metric server.

License:        Apache License 2.0
URL:            https://github.com/dpdevel/%{name}
Source0:        https://github.com/dpdevel/%{name}/archive/v%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python-devel
BuildRequires:  python-setuptools

Requires:       python-hawkular-client
Requires:       python-future
Requires:       PyYAML

%description
Utility script for accessing Hawkular metrics server remotely.


%prep
%setup -q


%build
%{__python} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT


%files
%doc README.md COPYING
%{_bindir}/hawkular-cli
%{python_sitelib}/*


%changelog
