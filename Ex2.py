#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 12:34:20 2019

@author: frederik
"""

import requests 
import pandas as pd
import numpy as np
from pandas.io.json import json_normalize 

api_key='46pvhgbh919ut8gn'

api_search_url = 'https://api.trove.nla.gov.au/v2/result'

params = {
'q': 'mahatma+gandhi',
'zone' : ' newspaper' , 
'key' : api_key ,
'n' : '100' , 
'encoding' : 'json'       
}

response = requests.get(api_search_url, params=params)

print(response)