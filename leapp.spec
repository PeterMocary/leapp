Name:       leapp
Version:    0.0.1
Release:    1%{?dist}
Summary:    leapp tool rpm

Group:      Unspecified
License:    GPLv2+
URL:        https://github.com/leapp-to/prototype
Source0:    https://github.com/leapp-to/prototype/archive/master.tar.gz
BuildArch:  noarch

BuildRequires:   python2-devel
BuildRequires:   python2-setuptools
BuildRequires:   libvirt-python
BuildRequires:   libvirt-devel
BuildRequires:   python-enum34
BuildRequires:   python2
BuildRequires:   python2-nmap
BuildRequires:   python2-paramiko

%description
LeApp is a "Minimum Viable Migration" utility that aims to decouple virtualized
applications from the operating system kernel included in their VM image by
migrating them into macro-containers that include all of the traditional
components of a stateful VM (operating system user space, application run-time,
management tools, configuration files, etc), but use the kernel of the
container host rather than providing their own.

%package    tool
Summary:    LeApp is a "Minimum Viable Migration" utility
Requires:   python2-%{name} = %{version}-%{release}

%description tool
LeApp is a "Minimum Viable Migration" utility that aims to decouple virtualized
applications from the operating system kernel included in their VM image by
migrating them into macro-containers that include all of the traditional
components of a stateful VM (operating system user space, application run-time,
management tools, configuration files, etc), but use the kernel of the
container host rather than providing their own.

%package -n python2-%{name}
Summary:    Python libraries of LeApp
Requires:   libguestfs-tools-c
Requires:   libvirt-python
Requires:   python-enum34
Requires:   python2
Requires:   python2-nmap
Requires:   python2-paramiko

%description -n python2-%{name}
LeApp is a "Minimum Viable Migration" utility that aims to decouple virtualized
applications from the operating system kernel included in their VM image by
migrating them into macro-containers that include all of the traditional
components of a stateful VM (operating system user space, application run-time,
management tools, configuration files, etc), but use the kernel of the
container host rather than providing their own.

%package cockpit
Summary:  Cockpit plugin for LeApp
Requires: cockpit
Requires: %{name}-tool = %{version}-%{release}

%description cockpit
LeApp is a "Minimum Viable Migration" utility that aims to decouple virtualized
applications from the operating system kernel included in their VM image by
migrating them into macro-containers that include all of the traditional
components of a stateful VM (operating system user space, application run-time,
management tools, configuration files, etc), but use the kernel of the
container host rather than providing their own.

%prep
%setup -qn prototype-master
sed -i "s/install_requires=/install_requires=[],__fake=/g" src/setup.py
[ -f AUTHORS ] || touch AUTHORS
[ -f COPYING ] || touch COPYING

%build
pushd src
%py2_build_egg
popd

%install
/bin/mkdir -p %{buildroot}/%{_datadir}/cockpit/leapp
/bin/cp -a cockpit/* %{buildroot}/%{_datadir}/cockpit/leapp/

pushd src
%py2_install_egg
popd

%files tool
%doc README.md AUTHORS COPYING
%attr(755, root, root) %{_bindir}/%{name}-tool

%files -n python2-%{name}
%doc README.md AUTHORS COPYING
%{python2_sitelib}/*

%files cockpit
%doc README.md AUTHORS COPYING
%dir %attr (755,root,root) %{_datadir}/cockpit/%{name}
%attr(644, root, root) %{_datadir}/cockpit/%{name}/*


%changelog
* Thu May 04 2017 Vinzenz Feenstra <evilissimo@redhat.com> - 0.0.1-1
- Initial
