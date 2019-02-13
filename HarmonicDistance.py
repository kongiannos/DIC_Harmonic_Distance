# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 11:15:44 2019

@author: KonGiannos
"""

#Import packages
from music21 import *
import numpy as np
import computeDIC as dic
import reduction

#Read 2 xml files
f1 = reduction.chordifyReduction('file1.xml')
f2 = reduction.chordifyReduction('file2.xml')

#Compute a list of DICs for each file
DIC1 = dic.computeDICsfromChordList(f1)
DIC2 = dic.computeDICsfromChordList(f2)

#Calculate the respective correlation coefficients (Pearson's product)
coef = []
if len(DIC1) != len(DIC2):
    for i in len(DIC1):
        coef[i] = np.corrcoef(DIC1[i],DIC2[i])[0][1]
else:
    print('The harmonisations do not have the same amount of chords')
    