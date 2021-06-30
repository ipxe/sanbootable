# Configure autoconf
#
AC_INIT([sanbootable], [0.1], [mbrown@fensystems.co.uk])
AC_CONFIG_SRCDIR([src/initramfs/iscsi.initramfs])
AC_CONFIG_AUX_DIR([build-aux])
AM_INIT_AUTOMAKE([foreign subdir-objects tar-ustar])

# Define distribution selections
#
AC_ARG_ENABLE([ubuntu],
  AS_HELP_STRING([--enable-ubuntu],
		 [enable all Ubuntu features]))

# Define individual feature selections
#
AC_ARG_ENABLE([finalrd],
  AS_HELP_STRING([--disable-finalrd],
		 [disable finalrd hook]))
AC_ARG_ENABLE([grub-initrd-fallback],
  AS_HELP_STRING([--disable-grub-initrd-fallback],
		 [disable GRUB initrd fallback hook]))
AC_ARG_ENABLE([initramfs],
  AS_HELP_STRING([--disable-initramfs],
		 [disable initramfs hook]))

# Determine current distribution if none explicitly specified
#
AS_IF([test "x$enable_ubuntu" = "x"], [
  AS_IF([test -e /etc/lsb-release], [source /etc/lsb-release])
  AS_IF(AS_EXECUTABLE_P([/usr/bin/lsb_release]),
	[DISTRIB_ID=$(/usr/bin/lsb_release -s -i)])
  AS_IF([test "x$DISTRIB_ID" = "xUbuntu"], [default_ubuntu=yes])
])

# Test for individual distribution selections
#
AS_IF([test "x$enable_ubuntu" = "x"],
      [enable_ubuntu=$default_ubuntu])

# Disable all features by default
#
default_finalrd=no
default_grub_initrd_fallback=no
default_initramfs=no

# Set feature defaults per distribution
#
AS_IF([test "x$enable_ubuntu" = "xyes"], [
  default_finalrd=yes
  default_grub_initrd_fallback=yes
  default_initramfs=yes
])

# Test for individual feature selections
#
AS_IF([test "x$enable_finalrd" = "x"],
      [enable_finalrd=$default_finalrd])
AS_IF([test "x$enable_grub_initrd_fallback" = "x"],
      [enable_grub_initrd_fallback=$default_grub_initrd_fallback])
AS_IF([test "x$enable_initramfs" = "x"],
      [enable_initramfs=$default_initramfs])

# Define automake conditionals
#
AM_CONDITIONAL([FINALRD],
	       [test "x$enable_finalrd" = "xyes"])
AM_CONDITIONAL([GRUBINITRDFALLBACK],
	       [test "x$enable_grub_initrd_fallback" = "xyes"])
AM_CONDITIONAL([INITRAMFS],
	       [test "x$enable_initramfs" = "xyes"])

# Generate output files
#
AC_CONFIG_FILES([
  Makefile
  src/Makefile
  src/finalrd/Makefile
  src/grub-initrd-fallback/Makefile
  src/initramfs/Makefile
])
AC_OUTPUT
