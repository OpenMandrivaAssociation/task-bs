Summary:	Task package for the Mandriva build system nodes
Name:		task-bs
Version:	2012.0
Release:	3
License:	GPLv2+
Group:		System/Servers
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Url:		http://www.mandriva.com/
BuildArch:	noarch

%description
This task package installs the required components for the Mandriva
build system nodes.

%package common
Summary:	Task package for common tools on Mandriva build system nodes
Group:		System/Servers
Requires:	basesystem
Requires:	urpmi
Requires:	cfengine-cfagent
Requires:	openssh-server
Requires:	sshd-monitor
Requires:	openldap-clients
Requires:	nss_ldap
Requires:	pam_ldap
Requires:	nscd
Requires:	sudo
Requires:	zsh
Requires:	nail
Requires:	ntp
Requires:	smartmontools
# rpmctl (through mkcd deps)
Requires:	perl-Image-Size

%description common
This task package installs the required common components for the
Mandriva build system nodes.

%package cluster-base
Summary:	Task package for base system of the Mandriva cluster nodes
Group:		System/Servers
Requires:	task-bs-common
Requires:	nfs-utils
Requires:	kernel-server-latest
Requires:	net-snmp
Requires:	ganglia-core

%description cluster-base
This task package installs the required components for the base system
of the Mandriva cluster nodes.

%package cluster-chroot
Summary:	Task package for chroot system of the Mandriva cluster nodes
Group:		System/Servers
Requires:	task-bs-common
Requires:	autofs
Requires:	nfs-utils-clients
Requires:	mdv-youri-submit
# iurt requirements
Requires:	mdv-distrib-tools
Requires:	mkcd
Requires:	perl-File-NCopy
Requires:	perl-Filesys-Df
Requires:	perl-MIME-tools
Requires:	perl-RPM
Requires:	rpmmon
Requires:	rsync
Requires:	repsys
Requires:	mdvsys
Requires:	postfix
Requires:	squid
# urpmi requirements for migrating rpmdb db version to one compatible with chrooted rpm
#Requires:	db42-utils
Requires:	db4-utils >= 4.6
Requires:	rpmlint
Requires:	rpmlint-mandriva-policy

%description cluster-chroot
This task package installs the required components for the chroot system
of the Mandriva cluster nodes, running cooker.

%package cluster-main
Summary:	Task package for the main node of the Mandriva cluster
Group:		System/Servers
Requires:	task-bs-common
Requires:	autofs
Requires:	nfs-utils
Requires:	repsys
Requires:	smartmontools
Requires:	kernel-server-latest
Requires:	mdv-youri-submit
Requires:	net-snmp
Requires:	postfix
# for the web interface:
Requires:	apache-mpm-prefork
Requires:	apache-mod_userdir
Requires:	apache-mod_authnz_external
Requires:	apache-mod_ssl
Requires:	apache-mod_php
Requires:	php-suhosin
Requires:	php-ssh2

%description cluster-main
This task package installs the required components for the main node
of the Mandriva cluster (currently kenobi).

%package mirror-upload
Summary:	Task package for mirror upload node in Mandriva build system
Group:		System/Servers
Requires:	task-bs-common
Requires:	nfs-utils
Requires:	mdv-youri-submit
Requires:	mkcd
Requires:	rsync
Requires:	lftp
Requires:	dhcp-server
Requires:	pxe
Requires:	tftp-server
Requires:	apache-mpm-prefork
Requires:	postfix
Requires:	kernel-server-latest
Requires:	make
# for soft/build_system/mirror/mirrorlist called by generatelist.sh:
Requires:	libxslt-proc

%description mirror-upload
This task package installs the required components for the mirror upload
node of the Mandriva build system (currently raoh).

%prep
%setup -q -T -c

%build

%install

%clean
rm -rf %{buildroot}

%triggerin cluster-chroot -- glibc, gcc, binutils

%files common
%files cluster-base
%files cluster-chroot
%files cluster-main
%files mirror-upload


%changelog
* Fri Nov 18 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 2012.0-2
+ Revision: 731666
- rebuild

  + Bogdano Arendartchuk <bogdano@mandriva.com>
    - icecream is not being used anymore

* Sat Apr 09 2011 Bogdano Arendartchuk <bogdano@mandriva.com> 2011.0-1
+ Revision: 652040
- Bump version

* Tue Jan 25 2011 Bogdano Arendartchuk <bogdano@mandriva.com> 2010.1-6
+ Revision: 632516
- now nodes use squid to cache packages
- rpm5: s/perl-RPM4/perl-RPM/

  + Per Øyvind Karlsen <peroyvind@mandriva.org>
    - drop dependency on db42-utils to prevent urpmi trying to migrate to ancient bdb
    - bump release

* Tue Dec 28 2010 Thierry Vignaud <tv@mandriva.org> 2010.1-5mdv2011.0
+ Revision: 625583
- make task-bs-common conflicts with msec

* Sun Oct 31 2010 Olivier Blin <blino@mandriva.org> 2010.1-4mdv2011.0
+ Revision: 591158
- add back sshd-monitor, this could save some big trouble
- don't conflict with msec, the proper way is to configure it not to be evil

* Wed Sep 01 2010 Thierry Vignaud <tv@mandriva.org> 2010.1-3mdv2011.0
+ Revision: 575063
- make task-bs-common conflicts with msec

* Mon Aug 30 2010 Thierry Vignaud <tv@mandriva.org> 2010.1-2mdv2011.0
+ Revision: 574266
- make task-bs-cluster-base conflicts with msec

  + Bogdano Arendartchuk <bogdano@mandriva.com>
    - get off my lawn X libs

  + Pascal Terjan <pterjan@mandriva.org>
    - Increase version

* Mon Apr 19 2010 Bogdano Arendartchuk <bogdano@mandriva.com> 2010.0-12mdv2010.1
+ Revision: 536876
- added packages used to recreate the environment on The New Kenobi

  + Olivier Blin <blino@mandriva.org>
    - require perl-Image-Size for rpmctl

* Sun Nov 22 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2009.0-10mdv2010.1
+ Revision: 468682
- perl-  has been renamed

* Tue Aug 04 2009 Michael Scherer <misc@mandriva.org> 2009.0-9mdv2010.0
+ Revision: 408682
- update license
- update requires on rpmlint

* Mon Jul 13 2009 Gustavo De Nardin <gustavodn@mandriva.com> 2009.0-8mdv2010.0
+ Revision: 395603
- perl-Filesys-Statvfs_Statfs_Df got renamed to perl-Filesys-Df

* Tue Jan 06 2009 Pixel <pixel@mandriva.com> 2009.0-7mdv2009.1
+ Revision: 326118
- urpmi requires a recent db_dump, but either db47-utils or db46-utils will do

* Tue Sep 09 2008 Pixel <pixel@mandriva.com> 2009.0-6mdv2009.0
+ Revision: 283116
- task-bs-cluster-chroot: add some requires to allow urpmi to migrate rpmdb db
  version to one compatible with chrooted rpm

* Sun Aug 10 2008 Olivier Blin <blino@mandriva.org> 2009.0-4mdv2009.0
+ Revision: 270205
- require openldap-clients everywhere
  (ldapsearch is used by scripts like all_ssh)

* Tue Jul 22 2008 Olivier Blin <blino@mandriva.org> 2009.0-3mdv2009.0
+ Revision: 240093
- require rpmmon (for iurt)

* Tue Jun 24 2008 Frederic Crozat <fcrozat@mandriva.com> 2009.0-2mdv2009.0
+ Revision: 228518
- add trigger to automatically update icecream environment when gcc / glibc / binutils are updated

* Wed May 14 2008 Thierry Vignaud <tv@mandriva.org> 2009.0-1mdv2009.0
+ Revision: 206902
- bump version

* Thu May 08 2008 Olivier Blin <blino@mandriva.org> 2008.1-12mdv2009.0
+ Revision: 204606
- require postfix in kenobi and cluster chroots (not to lose cron error messages)

* Fri Mar 07 2008 Olivier Blin <blino@mandriva.org> 2008.1-11mdv2008.1
+ Revision: 181261
- require nail (to get alerts when cron jobs fail)

  + Pixel <pixel@mandriva.com>
    - add libxslt-proc for soft/build_system/mirror/mirrorlist called by generatelist.sh

  + Marcelo Ricardo Leitner <mrl@mandriva.com>
    - Added net-snmp requires to task-bs-base and task-bs-main: we will monitor them
      from outside.
    - Added icecream requires to tasb-bs-base and task-bs-main: icecream daemons
      should be executed from outside, while task-bs-main is the scheduler.

  + Thierry Vignaud <tv@mandriva.org>
    - fix no-buildroot-tag

* Fri Feb 08 2008 Olivier Blin <blino@mandriva.org> 2008.1-10mdv2008.1
+ Revision: 164274
- kenobi also needs mdv-youri-submit

* Fri Feb 08 2008 Olivier Blin <blino@mandriva.org> 2008.1-9mdv2008.1
+ Revision: 164184
- iurt requires rsync for log files
- require make on raoh
- require apache and kernel-server on kenobi

* Tue Jan 29 2008 Olivier Blin <blino@mandriva.org> 2008.1-8mdv2008.1
+ Revision: 159684
- require lftp on mirror upload node

* Fri Jan 25 2008 Olivier Blin <blino@mandriva.org> 2008.1-7mdv2008.1
+ Revision: 158095
- require nscd everywhere

* Tue Jan 22 2008 Olivier Blin <blino@mandriva.org> 2008.1-6mdv2008.1
+ Revision: 156344
- require perl-MDV-Repsys in cluster chroots

* Tue Jan 22 2008 Olivier Blin <blino@mandriva.org> 2008.1-5mdv2008.1
+ Revision: 156043
- require kernel-server-latest as well for mirror upload host
- require apache and postfix for mirror upload
- require rsync for mirror upload
- require mkcd on mirror upload host

* Mon Jan 21 2008 Olivier Blin <blino@mandriva.org> 2008.1-4mdv2008.1
+ Revision: 155718
- add iurt requirements for cluster chroots (thanks to Anssi, #37001)

* Fri Jan 18 2008 Olivier Blin <blino@mandriva.org> 2008.1-3mdv2008.1
+ Revision: 154909
- add kernel-server-latest on cluster base systems
- make sure basesystem gets installed/reinstalled automatically on every cluster node

* Tue Jan 15 2008 Olivier Blin <blino@mandriva.org> 2008.1-2mdv2008.1
+ Revision: 152534
- install smartmontools
- install sshd-monitor everywhere
- require urpmi everywhere
- require ntp everywhere
- require nscd in cluster chroots
- require icecream in cluster chroots

* Fri Dec 21 2007 Olivier Blin <blino@mandriva.org> 2008.1-1mdv2008.1
+ Revision: 136483
- oops, require nfs-utils instead of nfs-server
- require dhcp/pxe/tftp on main mirror
- require autofs on main cluster node
- require repsys on public cluster nodes
- require mdv-youri-submit in cluster chroots and mirror upload systems
- require zsh so that zsh users can login
- require cfengine-cfagent
- require nfs-utils-clients for cluster chroots
- add current node main in descriptions
- require autofs on cluster chroots
- require nfs-server on cluster base nodes, cluster main node and mirror upload node
- require sudo on all nodes
- require nss_ldap and pam_ldap on all nodes
- require openssh-server on all nodes
- initial task-bs package
- create task-bs

