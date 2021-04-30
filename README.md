# SAN bootability package

## Overview

Most Linux distributions now support the ability to install directly
to an iSCSI (or FCoE, or other SAN protocol) target disk.  You can use
the Linux distribution's own installer in conjunction with a
bootloader such as [iPXE][ipxe] to install the operating system onto
the iSCSI disk.  When you do this, the installer will automatically
configure the installed operating system to be able to boot from an
iSCSI target disk.

If you originally installed the operating system to a local disk
(rather than to an iSCSI target disk), then the installer will not set
up the configuration required to support booting via iSCSI.  You can
take an image of the local disk containing the installed operating
system and copy it to an iSCSI target disk, but the operating system
will not be able to boot successfully because it will be missing some
required configuration.

The `sanbootable` package solves this problem by providing the
configuration required to allow a Linux operating system to boot from
either a local disk or an iSCSI target.

## Installation

### Ubuntu

Download and install the latest version of
[`sanbootable.deb`][sanbootable.deb]:
```
curl -OL https://github.com/ipxe/sanbootable/releases/latest/download/sanbootable.deb
sudo apt install -y ./sanbootable.deb
```

## Usage

After installing the `sanbootable` package, you can freely transfer
your disk image from a local disk to an iSCSI target disk or vice
versa.

The `sanbootable` code will detect at boot time whether the operating
system is being booted from a local disk or from an iSCSI target, and
will automatically adjust the system configuration as needed.


[ipxe]: https://ipxe.org
[sanbootable.deb]: https://github.com/ipxe/sanbootable/releases/latest/download/sanbootable.deb
