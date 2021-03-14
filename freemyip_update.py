#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 06:56:40 2021

@author: danripp

Purpose: Make a HTTPS GET request to freemyip.com URL for dynamic DNS update
How to use: 
1. Put freemyip.com URLS in urls list (remember to keep these secret)
2. Run this script periodically on your host system, e.g., through chronjob daily
3. Check freemyip_updates.log as needed
"""

import requests
import time


#list of urls to make update request to.  Note: add &verbose=yes to end of url for more detailed response and logging
#note the urls must be kept secret or anyone could update them! 
urls = ["https://freemyip.com/update?token=f34d6ecb2197a65bc73069bd&domain=update-script-test-1.freemyip.com&verbose=yes",
        "https://freemyip.com/update?token=47db14a8ad2b1bd00ec2cd84&domain=update-script-test-2.freemyip.com&verbose=yes"
        ]


#makes GET request to urls and log responses
for i in urls:
    try:
        r = requests.get(i) 
        resp = r.text.split('\n')  
    except:
        resp = ["ERROR", "Request failed. Check URL or internet connectivity."]
        
    #logging
    domain = i.split('domain=')
    domain = domain[1].split('&verbose=')
    domain = domain[0]
      
    log = time.ctime() + ", " + domain + ", " + resp[0] + ", " + resp[1]  
    print(log)
    
