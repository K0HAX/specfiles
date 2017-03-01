Name: netpipes
Version: 4.2
Release: 3
Summary: BSD Netpipes
Source0: netpipes-4.2.tar.gz
License: BSD
Group: Development/Tools
BuildArch: x86_64
BuildRoot: %{_tmppath}/%{name}-buildroot
%description
A package to manipulate BSD TCP/IP stream sockets
%prep
%setup -q
%build
make
%install
mkdir -p $RPM_BUILD_ROOT/usr/bin
install -m 0755 encapsulate $RPM_BUILD_ROOT/usr/bin/encapsulate
install -m 0755 faucet $RPM_BUILD_ROOT/usr/bin/faucet
install -m 0755 getpeername $RPM_BUILD_ROOT/usr/bin/getpeername
install -m 0755 hose $RPM_BUILD_ROOT/usr/bin/hose
install -m 0755 sockdown $RPM_BUILD_ROOT/usr/bin/sockdown
install -m 0755 timelimit $RPM_BUILD_ROOT/usr/bin/timelimit
%clean
rm -rf $RPM_BUILD_ROOT
%files
/usr/bin/encapsulate
/usr/bin/faucet
/usr/bin/getpeername
/usr/bin/hose
/usr/bin/sockdown
/usr/bin/timelimit
