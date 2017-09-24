# cmu
Central monitoring Unit for home internet and other infrastructure at home

## CleanupDropbox.py

This program is for automatically manage the files when you use your dropbox account to manage the repository for automatic upload of files This program checks your drop box for the following

If the total used space exceeds the threshold set delete the LONGTERM folder contents (this will help keep the account sleek)
If the total number of files in SHORTTERM folder exceeds the threshold set in MAXCOUNT then move the files to LONGTERM (this will enable loading the folder contents on a mobile device faster)

## mv-logs.sh
This program makes sure your Raspberry Pi's internal memory does not get
filled up and moves the logs to a connected external mounted hard disk

## node-red flow cmu
This is the central program to manager all the orchestration. Checkout the Dahboard-sample.png
to understand what is monitored and how it looks like.
### Internet Stats
**Ping:** Regular 1 minute ping to monitor active internet
**Download & Upload:** Regular 15 minutes speed calculator (uses speedtest_cli)
**Last known internet:** Last known status of the internet

### Intranet status
Regular 5 second ping to the modem, network router and NVR

### Pi status
Regular 1 second stats of the pi temperature & volts. If Pi temperature >=75 an email alert is sent. If Pi temperature is >=80 the Pi is shutdown automatically
Regular 5 second status of the Pi memory used, free and total memory

### Central Storage
Regular 5 hour check of the total storage used. Pi on-board, Pi external hard disk and dropbox cloud storage

### Rack Stats
Regular 5 seconds check of Rack temperature, Humidity and Pressure outputs from SenseHAT on the Pi

### Weather
Regular 2 hours check of the location weather reported from OpenWeatherMap APIs. Temperature, Humidity, Pressure and summary text.
