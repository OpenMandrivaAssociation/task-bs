%define name task-bs
%define version 2008.1
%define release %mkrel 1

Summary: Task package for the Mandriva build system nodes
Name: %{name}
Version: %{version}
Release: %{release}
License: GPL
Group: System/Servers
Url: http://www.mandriva.com/
BuildArch: noarch

%description
This task package installs the required components for the Mandriva
build system nodes.

%package common
Summary: Task package for common tools on Mandriva build system nodes
Group: System/Servers
Requires: cfengine-cfagent
Requires: openssh-server
Requires: nss_ldap pam_ldap
Requires: sudo
Requires: zsh

%description common
This task package installs the required common components for the
Mandriva build system nodes.

%package cluster-base
Summary: Task package for base system of the Mandriva cluster nodes
Group: System/Servers
Requires: task-bs-common
Requires: nfs-utils

%description cluster-base
This task package installs the required components for the base system
of the Mandriva cluster nodes.

%package cluster-chroot
Summary: Task package for chroot system of the Mandriva cluster nodes
Group: System/Servers
Requires: task-bs-common
Requires: autofs
Requires: nfs-utils-clients
Requires: mdv-youri-submit
Requires: repsys
Requires: icecream

%description cluster-chroot
This task package installs the required components for the chroot system
of the Mandriva cluster nodes, running cooker.

%package cluster-main
Summary: Task package for the main node of the Mandriva cluster
Group: System/Servers
Requires: task-bs-common
Requires: autofs
Requires: nfs-utils
Requires: repsys

%description cluster-main
This task package installs the required components for the main node
of the Mandriva cluster (currently kenobi).

%package mirror-upload
Summary: Task package for mirror upload node in Mandriva build system
Group: System/Servers
Requires: task-bs-common
Requires: nfs-utils
Requires: mdv-youri-submit
Requires: dhcp-server pxe tftp-server

%description mirror-upload
This task package installs the required components for the mirror upload
node of the Mandriva build system (currently raoh).

%prep
%setup -q -T -c

%build

%install
rm -rf %{buildroot}

%clean
rm -rf %{buildroot}

%files common
%files cluster-base
%files cluster-chroot
%files cluster-main
%files mirror-upload
