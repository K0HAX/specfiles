Name: sipcalc
Version: 1.1.6
Release: 1
Summary: Routemeister Sipcalc
Source0: sipcalc-1.1.6.tar.gz
License: BSD
Group: Development/Tools
BuildArch: x86_64
BuildRoot: %{_tmppath}/%{name}-buildroot
%description
Sipcalc is an console based ip subnet calculator with IPv4 and IPv6 support.
%prep
%setup -q

%build
%configure
%make_build

%install
%make_install
#mkdir -p $RPM_BUILD_ROOT/usr/bin
#install -m 0755 sipcalc $RPM_BUILD_ROOT/usr/bin/sipcalc

%clean
rm -rf $RPM_BUILD_ROOT
%files
/usr/bin/sipcalc
%{_mandir}/man1/sipcalc.1.gz

