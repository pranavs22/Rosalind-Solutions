# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 22:24:20 2019

@author: Pranav
"""

#Imports
import requests
import re
from bs4 import BeautifulSoup

file="C:/Rosalind/rosalind_dbpr.txt"
file_o="C:/Rosalind/dbpr_temp.txt"

#Functions
def get_data(file):
    '''This is a helper function that parses data from Uniprot-html format into 
    neat rows and columns which makes it easy to find GO terms
    be used for further data mining. The data is store in file called dbpr_temp.txt
    '''
    with open(file) as f, open(file_o,"w") as o:
        ID=f.readline().strip()
        print("Parsing Data...")
        f=requests.get("http://www.uniprot.org/uniprot/"+ID+".txt")
        data=BeautifulSoup(f.content,'html.parser')
        
        for i in data.contents:
            
            content=i.split("\t")
            o.writelines(content)
        return 
def find_GO(file_o):
    '''
    This function finds out GO terms from the file returned by get_data funtion
    '''
    get_data(file)

    print("Finding GO terms...")
    with open(file_o) as o:
        func=[]
        for i in o:
            if "GO" in i:
                func.append(re.findall(".*(P.*;).*",i))
    for i in func:
        print(str(i)[4:-3])
    return
#Run
if __name__=="__main__":
    find_GO(file_o)