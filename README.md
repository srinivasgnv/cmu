# cmu
Central monitoring Unit for home internet and other infrastructure at home

#CleanupDropbox.py

This program is for automatically manage the files when you use your dropbox account to manage the repository for automatic upload of files This program checks your drop box for the following

If the total used sapce exceeds the threshold set delete the LONGTERM folder contents (this will help keep the account sleek)
If the total number of files in SHORTTERM folder exceeds the threshold set in MAXCOUNT then move the files to LONGTERM (this will enable loading the folder contents on a mobile device faster)

#mv-logs.sh
This program makes sure your Raspberry Pi's internal memory does not get
filled up and moves the logs to a connected external mounted hard disk

#node-red flow
This is the central program to manager all the orchestration 
