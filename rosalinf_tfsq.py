# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 11:46:10 2019

@author: Pranav Sahasrabudhe
"""
#imports
import re


#infiles and outfiles
file="C:/Rosalind/rosalind_tfsq.txt"
out_file="C:/Rosalind/rosalind_tfsq_fa.fa"

def convert_fastq(file,outfile):
    '''
    This function converts fastq to fasta format and writes it to a new file
    
    '''
    with open(file) as f,open(out_file,"a") as o :
        while True:
            header=f.readline().strip()
            seq=f.readline().strip()
            f.readline().strip()
            f.readline().strip()
            if len(header)==0:
                break
    
            header=re.sub("@",">",header)
            o.write(header+"\n")
            o.write(seq+"\n")
        
    return "Conversion Successful"    
if __name__=="__main__":
    convert_fastq(file,out_file)
    