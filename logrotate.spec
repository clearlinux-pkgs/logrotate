#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x873DB37572A37B36 (kdudka@redhat.com)
#
Name     : logrotate
Version  : 3.15.1
Release  : 5
URL      : https://github.com/logrotate/logrotate/releases/download/3.15.1/logrotate-3.15.1.tar.xz
Source0  : https://github.com/logrotate/logrotate/releases/download/3.15.1/logrotate-3.15.1.tar.xz
Source1  : logrotate.service
Source2  : logrotate.timer
Source3 : https://github.com/logrotate/logrotate/releases/download/3.15.1/logrotate-3.15.1.tar.xz.asc
Summary  : Rotates, compresses, removes and mails system log files
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+
Requires: logrotate-bin = %{version}-%{release}
Requires: logrotate-license = %{version}-%{release}
Requires: logrotate-man = %{version}-%{release}
Requires: logrotate-services = %{version}-%{release}
BuildRequires : acl-dev
BuildRequires : popt-dev

%description
The logrotate utility is designed to simplify the administration of
log files on a system which generates a lot of log files.  Logrotate
allows for the automatic rotation compression, removal and mailing of
log files.  Logrotate can be set to handle a log file daily, weekly,
monthly or when the log file gets to a certain size.  Normally,
logrotate runs as a daily cron job.

Install the logrotate package if you need a utility to deal with the
log files on your system.

%package bin
Summary: bin components for the logrotate package.
Group: Binaries
Requires: logrotate-license = %{version}-%{release}
Requires: logrotate-services = %{version}-%{release}

%description bin
bin components for the logrotate package.


%package license
Summary: license components for the logrotate package.
Group: Default

%description license
license components for the logrotate package.


%package man
Summary: man components for the logrotate package.
Group: Default

%description man
man components for the logrotate package.


%package services
Summary: services components for the logrotate package.
Group: Systemd services

%description services
services components for the logrotate package.


%prep
%setup -q -n logrotate-3.15.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1567182206
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1567182206
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/logrotate
cp COPYING %{buildroot}/usr/share/package-licenses/logrotate/COPYING
%make_install
mkdir -p %{buildroot}/usr/lib/systemd/system
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/systemd/system/logrotate.service
install -m 0644 %{SOURCE2} %{buildroot}/usr/lib/systemd/system/logrotate.timer

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/logrotate

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/logrotate/COPYING

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man5/logrotate.conf.5
/usr/share/man/man8/logrotate.8

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/logrotate.service
/usr/lib/systemd/system/logrotate.timer
