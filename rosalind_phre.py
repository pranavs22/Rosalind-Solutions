# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 11:55:50 2019

@author: Pranav Sahasrabudhe
"""
def convert_phred(letter):
    """Converts a single character into a phred score"""
    return ord(letter)-33

file="C:/Rosalind/rosalind_phre.txt"

def count_reads(file):
    count=0
    with open(file) as f:
        cut_off=f.readline().strip()
        while True:
            q_scores=[]
            header=f.readline().strip()
            
            f.readline().strip()
            f.readline().strip()
            q_score=f.readline().strip()
            if len(header)==0:
                break      
            for i in q_score:
                P=convert_phred(i)            
                q_scores.append(P)
            
            avg=float((sum(q_scores))/(len(q_scores)))
#            print(avg)       #Check Average
            if avg < float((int(cut_off))):
                count+=1
            
           
    return count

if __name__=="__main__":
    count=count_reads(file)
    print(count)