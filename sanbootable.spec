%define dracutlibdir %{_prefix}/lib/dracut

Name:		sanbootable
Version:	0.2
Release:	1%{?dist}
Summary:	SAN bootability package

License:	GPLv2+
URL:		https://github.com/ipxe/sanbootable
Source0:	https://github.com/ipxe/sanbootable/releases/download/v%{version}/%{name}-%{version}.tar.gz

BuildArch:	noarch
BuildRequires:	make
Requires:	dracut-network
Requires:	iscsi-initiator-utils

%description
Allow operating system to be booted from a SAN (e.g. iSCSI) disk.

%prep
%autosetup

%build
%configure --enable-redhat
%make_build

%install
%make_install

%post
dracut -v -f --regenerate-all

%files
%license LICENSE
%doc README.md
%{dracutlibdir}/dracut.conf.d/50-sanbootable.conf
%dir %{dracutlibdir}/modules.d/95sanbootable
%{dracutlibdir}/modules.d/95sanbootable/module-setup.sh
%{dracutlibdir}/modules.d/95sanbootable/sanbootable-cmdline.sh

%changelog
* Thu Jul  1 2021 Michael Brown <mbrown@fensystems.co.uk> - 0.2-1
- Initial release
