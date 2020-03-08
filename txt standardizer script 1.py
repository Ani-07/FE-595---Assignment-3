# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 12:11:17 2020

@author: Anirudh Raghavan
"""
# Objective - To standardize text files

# Target Files

# 1. HW_595
# 2. Company Details
# 3. result

import re
import pandas as pd


def text_standardizer (File_Name):
    file1 = open(File_Name,
             "r")
    data = file1.read()
    rx_name = re.compile(r'Name: (?P<name>.*)\n')
    rx_purpose = re.compile(r'Purpose: (?P<purpose>.*)')
    names = rx_name.findall(data)
    purposes = rx_purpose.findall(data)

    NLP_data = pd.read_csv("NLP Data.csv")
    for i in range(len(purposes)):
        NLP_data = NLP_data.append({'Name' : names[i], 'Purpose' : purposes[i]},ignore_index=True)

    NLP_data.to_csv("NLP data.csv",index=False)


if __name__ == "__main__":
    text_standardizer("595_HW2.txt")
    text_standardizer("Company_Details.txt")
    text_standardizer("result.txt")
