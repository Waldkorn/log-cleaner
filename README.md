# Log Cleaner

Log cleaner is a python script used to clean up old logs. It will keep old logs for a specified amount of days in a tar.gz file and delete them once they expire.

## Setup

### step 1:

Edit logcleaner.py and edit the following values in Main():

 - log\_folder: set path to the folder where you store your logs.
 - archives\_folder: set path to the folder where you want to archive old logs. __Notice__: make sure this folder exists before running the script.
 - days\_to\_keep\_archives: set the amount of days you want to store your archives.

### step 2:

Make logcleaner.py executable:
```
chmod +x /path/to/logcleaner.py
```

### step 3:

Add an entry to your crontab to ensure logcleaner.py runs daily:
```
0 5 * * * nice path/to/logcleaner.py
```
