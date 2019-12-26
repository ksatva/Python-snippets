#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Title - 

Created on Fri Sep 27 02:05:50 2019
@author: k as root
"""

import requests
url = 'https://httpbin.org/ip'
proxies = {
    "http": 'http://209.50.52.162:9050', 
    "https": 'http://209.50.52.162:9050'
}
response = requests.get(url,proxies=proxies)
print(response.json())