#!/bin/sh

# At boot time, check for an iBFT and force an iSCSI boot if one is
# detected.

modprobe iscsi_ibft

if [ -d /sys/firmware/ibft ] ; then
    echo "Attempting iSCSI boot via iBFT:" \
	 $(cat /sys/firmware/ibft/target*/target-name) > /dev/console
    echo "rd.iscsi.ibft rd.iscsi.firmware " > /etc/cmdline.d/50-sanbootable.conf
fi
