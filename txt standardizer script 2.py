# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 15:10:55 2020

@author: Anirudh Raghavan
"""

# Objective - To standardize text files

# Target Files

# output_Webscrap_HW2.txt

import re
import pandas as pd

def text_standardizer2 (File_Name):
    file1 = open(File_Name,
             "r")
    data = file1.read()
    rx_name = re.compile(r'Name: (?P<name>.*)\n')
    rx_purpose = re.compile(r'Purpose: (?P<purpose>.*)')
    names = rx_name.findall(data)
    purposes = rx_purpose.findall(data)
    
    for i in range(len(names)):
        tmp = names[i]
        index = tmp.find("Purpose")
        tmp = tmp[:index-1]
        names[i] = tmp

    NLP_data = pd.read_csv("NLP Data.csv")
    for i in range(len(purposes)):
        NLP_data = NLP_data.append({'Name' : names[i], 'Purpose' : purposes[i]},ignore_index=True)

    NLP_data.to_csv("NLP data.csv",index=False)

if __name__ == "__main__":
    text_standardizer2("output_Webscrap_HW2.txt")