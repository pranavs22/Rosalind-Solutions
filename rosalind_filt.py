# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 15:38:07 2019

@author: Pranav
"""
def convert_phred(letter):
    """Converts a single character into a phred score"""
    return ord(letter)-33

file="C:/Rosalind/rosalind_filt_4_dataset.txt"
def check_phred(file):
    '''
    This function calculates phred sore for each of the reads and filters 
    as per the set cut-off. It returns the number of filtered reads.
    
    '''
    count=total=0
    with open(file) as f:

        data=f.readline().strip().split()
        threshold=int(data[0])
        p=int(data[1])    
    
        
        while True:
            q_scores=[]
            header=f.readline().strip()
            
            seq=f.readline()
            l=len(seq)
            q_header=f.readline().strip()
            q_score=f.readline().strip()
            total+=1
            if len(header)==0:
                break    
            n=1
            for i in q_score:
                P=convert_phred(i) 
                
                q_scores.append(P)
                if P >= threshold:
                   
                    n+=1
            if float(n)>=((p*l)/100):
                count+=1
                
              
    return count


if __name__=="__main__":
    count=check_phred(file)
    print(count)