# freemyip_update
Python script to update [freemyip.com](https://freemyip.com) dynamic DNS

# Purpose: 
Make a HTTPS GET request to freemyip.com URL for dynamic DNS update

# How to use: 
1. Put freemyip.com URLS in urls list (remember to keep these secret)
2. Run this script periodically on your host system, e.g., through chronjob daily

# Example usage
1. Place freemyip_update.py in a directory such as /usr/local/bin/
2. Edit freemyip_update.py replacing urls with your own
3. Edit crontab to run periodically, 
   e.g., once per day. On most linux systems: 'crontab -e' add line: 0 0 * * * python /usr/local/bin/freemyip_update.py >> /home/dan/freemyup_update.log

### Output will look something like this:
Sun Mar 14 00:00:01 2021, update-script-test-1.freemyip.com, OK, IP xx.xxx.xxx.xx didn't change. No need to update record.  
Sun Mar 14 00:00:01 2021, update-script-test-2.freemyip.com, OK, IP xx.xxx.xxx.xx didn't change. No need to update record.

