# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 10:53:35 2019

@author: Pranav
"""
dna='ACGATGACATATAGCGATATAGATAT'
motif = 'ATAT'


import time
start = time.clock()
i = dna.find(motif)
while i != -1:
    print(i+1)
    i = dna.find(motif, i +1)
print(time.clock()- start)

##Solution2

import time
start = time.clock()
for i in range(len(dna)):
    if dna[i:].startswith(motif):
        print (i+1)
print(time.clock()- start)
