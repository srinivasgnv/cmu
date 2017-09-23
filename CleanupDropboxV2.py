# This program is for automatically manage the files when you use your
# dropbox account to manage the repository for automatic upload of files
# This program checks your drop box for the following
# 1. If the total used sapce exceeds the threshold set delete the
# LONGTERM folder contents (this will help keep the account sleek)
# 2. If the total number of files in SHORTTERM folder exceeds the threshold
# set in MAXCOUNT then move the files to LONGTERM (this will enable loading
# the folder contents on a mobile device faster)

import argparse
import contextlib
import datetime
import os
import six
import sys
import time
import unicodedata
import dropbox

TOKEN='TOKEN'
SHORTTERM='/Shorterm'
LONGTERM='/Longterm'
# set maxsz i.e threshold for total quota used in MB
MAXSZ=200
# set MAXCOUNT i.e number of files in shortterm
MAXCOUNT=500
count=0

dbx=dropbox.Dropbox(TOKEN)

# get free space
# if freespace <= 10%
#  delete Backup folder and recreate it

#usedSpace in MB
usedSpace=(dbx.users_get_space_usage().used)/(1024*1024)
print('Total Used Quota in MB')
print(usedSpace)
print('Threshold set to in MB')
print(MAXSZ)
if usedSpace >= MAXSZ:
    # delete the contents of LONGTERM
    print('Started Deleting LONGTERM')
    res=dbx.files_list_folder('LONGTERM')
    for entry in res.entries:
        fileName='LONGTERM/'+entry.name
        dbx.files_delete(fileName)
    print('Completed Deleting LONGTERM')

# get number of files in SHORTTERM
# if number >=4K
#  move all SHORTTERM files to LONGTERM

res=dbx.files_list_folder('SHORTTERM')
for entry in res.entries:
    count=count+1

print('Total number of files in SHORTTERM ')
print(count)
print('Threshold set to ')
print(MAXCOUNT)
if count >= MAXCOUNT:
    # move all files from SHORTTERM to LONGTERM
    print('Started Moving files from SHORTTERM')
    res=dbx.files_list_folder('SHORTTERM')
    for entry in res.entries:
        fromFile='SHORTTERM/'+entry.name
        toFile='LONGTERM/'+entry.name
        dbx.files_move(fromFile,toFile)
    print('Completed moving files to LONGTERM')
