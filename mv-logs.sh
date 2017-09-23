#!/bin/sh
# Move all the logs from Pi to external disk
# this will be called from node-red on regular intervals 

ts=`date +"%d-%m-%y-%T"`
SRC="/home/pi/"
DES="/home/pi/exDisk"

if [ -f "$SRC/pi-temp-volts.log" ]
then
	mv $SRC/pi-temp-volts.log $DES/pi-temp-volts-$ts
fi

if [ -f "$SRC/admin-audit.log" ]
then
	mv $SRC/admin-audit.log $DES/admin-audit-$ts
fi

if [ -f "$SRC/internet-download-upload-speed.log" ]
then
	mv $SRC/internet-download-upload-speed.log $DES/internet-download-upload-speed-$ts
fi

if [ -f "$SRC/rack-temp-humidity.log" ]
then
	mv $SRC/rack-temp-humidity.log $DES/rack-temp-humidity-$ts
fi


if [ -f "$SRC/nvr-router-modem-DOWN.log" ]
then
	mv $SRC/nvr-router-modem-DOWN.log $DES/nvr-router-modem-DOWN-$ts
fi

if [ -f "$SRC/internet-up-down.log" ]
then
	mv $SRC/internet-up-down.log $DES/internet-up-down-$ts
fi
