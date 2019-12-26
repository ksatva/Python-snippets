#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 19:58:45 2019

@author: k as root
"""

import requests

url = 'http://google.com/favicon.ico'
r = requests.get(url, allow_redirects=True)

# code to download the media at http://google.com/favicon.ico and save it as google.ico.
open('google.ico', 'wb').write(r.content)
