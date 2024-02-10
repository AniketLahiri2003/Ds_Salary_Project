# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 15:04:22 2024

@author: ANIKET
"""
import glassdoor_Scrappers as gs
import pandas as pd
path= "C:/Users/ANIKET/Documents/ds_salary_proj/chromedriver.exe"

df = gs.get_jobs('data scientist',1500, False, path, 4)
df.to_csv('Uncleaned_DS_jobs.csv', index=False)