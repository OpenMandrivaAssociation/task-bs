%define name task-bs
%define version 2010.1
%define release %mkrel 3

Summary: Task package for the Mandriva build system nodes
Name: %{name}
Version: %{version}
Release: %{release}
License: GPLv2+
Group: System/Servers
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Url: http://www.mandriva.com/
BuildArch: noarch

%description
This task package installs the required components for the Mandriva
build system nodes.

%package common
Summary: Task package for common tools on Mandriva build system nodes
Group: System/Servers
Requires: basesystem
Requires: urpmi
Requires: cfengine-cfagent
Requires: openssh-server
Requires: openldap-clients
Requires: nss_ldap pam_ldap nscd
Requires: sudo
Requires: zsh
Requires: nail
Requires: ntp
Requires: smartmontools
# rpmctl (through mkcd deps)
Requires: perl-Image-Size

%description common
This task package installs the required common components for the
Mandriva build system nodes.

%package cluster-base
Summary: Task package for base system of the Mandriva cluster nodes
Group: System/Servers
Requires: task-bs-common
Requires: nfs-utils
Requires: kernel-server-latest
Requires: net-snmp
Requires: icecream

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
# iurt requirements
Requires: mdv-distrib-tools mkcd perl-File-NCopy perl-Filesys-Df perl-MIME-tools perl-RPM4 rpmmon rsync
Requires: repsys
Requires: mdvsys
Requires: icecream
Requires: postfix
# urpmi requirements for migrating rpmdb db version to one compatible with chrooted rpm
Requires: db42-utils
Requires: db4-utils >= 4.6
Requires: rpmlint  rpmlint-mandriva-policy
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
Requires: smartmontools
Requires: kernel-server-latest
Requires: mdv-youri-submit
Requires: net-snmp
Requires: icecream-scheduler
Requires: postfix
# for the web interface:
Requires: apache-mpm-prefork
Requires: apache-mod_userdir
Requires: apache-mod_authnz_external
Requires: apache-mod_ssl
Requires: apache-mod_php
Requires: php-suhosin
Requires: php-ssh2

%description cluster-main
This task package installs the required components for the main node
of the Mandriva cluster (currently kenobi).

%package mirror-upload
Summary: Task package for mirror upload node in Mandriva build system
Group: System/Servers
Requires: task-bs-common
Requires: nfs-utils
Requires: mdv-youri-submit mkcd rsync lftp
Requires: dhcp-server pxe tftp-server
Requires: apache-mpm-prefork
Requires: postfix
Requires: kernel-server-latest
Requires: make
# for soft/build_system/mirror/mirrorlist called by generatelist.sh:
Requires: libxslt-proc

%description mirror-upload
This task package installs the required components for the mirror upload
node of the Mandriva build system (currently raoh).

%prep
%setup -q -T -c

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_var}/cache/icecream-local-environment

%clean
rm -rf %{buildroot}

%triggerin cluster-chroot -- glibc, gcc, binutils
rm -f %{_var}/cache/icecream-local-environment/*.tar.gz
cd %{_var}/cache/icecream-local-environment
ICECC_NEWVERSION=`%{_bindir}/create-env | grep creating | sed -e 's/creating //'`
umask 0022
echo "ICECC_VERSION=\"$PWD/$ICECC_NEWVERSION\" ; export ICECC_VERSION" > %{_sysconfdir}/profile.d/icecream-local-environment.sh
echo "setenv ICECC_VERSION \"${PWD}/$ICECC_NEWVERSION\"" > %{_sysconfdir}/profile.d/icecream-local-environment.csh

%files common
%files cluster-base
%files cluster-chroot
%dir %{_var}/cache/icecream-local-environment
%files cluster-main
%files mirror-upload
