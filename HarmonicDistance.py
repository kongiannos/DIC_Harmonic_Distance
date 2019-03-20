# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 11:15:44 2019

@author: KonGiannos
"""

#Import packages
import music21 as m21
import numpy as np
import computeDIC as dic
#For plotting correlation coeffiecient vector
import matplotlib.pyplot as plt

def dicDistanceFromFiles(fileName1,fileName2,plot = False):
    #Read 2 xml files
    # parse piece
    p = m21.converter.parse(fileName1)
    # reduction
    r1 = p.parts[-1]
    r2 = p.parts[-2]
    rc = m21.stream.Score()
    rc.insert(0, r1)
    rc.insert(0, r2)
    rcChordified = rc.chordify()
    rcFlat = rcChordified.flat
    reduction = rcFlat.getElementsByClass('Chord')
    chordsAll = []
    for ch in reduction:
        chord = [c.pitch.midi%12 for c in ch]
        chordsAll.append(chord)
    f1 = chordsAll
    
    p = m21.converter.parse(fileName2)
    # reduction
    r1 = p.parts[-1]
    r2 = p.parts[-2]
    rc = m21.stream.Score()
    rc.insert(0, r1)
    rc.insert(0, r2)
    rcChordified = rc.chordify()
    rcFlat = rcChordified.flat
    reduction = rcFlat.getElementsByClass('Chord')
    chordsAll = []
    for ch in reduction:
        chord = [c.pitch.midi%12 for c in ch]
        chordsAll.append(chord)
    f2 = chordsAll
    
    #Compute a list of DICs for each file
    dic1 = dic.computeDICsfromChordList(f1)
    dic2 = dic.computeDICsfromChordList(f2)
    
    #Calculate the respective correlation coefficients (Pearson's product)
    coef = np.zeros(dic1.shape[0])
    for i in range(dic1.shape[0]):
        coef[i] = np.corrcoef(dic1[i,:],dic2[i,:])[0][1]
        
    if plot:
        plt.plot(coef)
        
    #Calculate mean and median
    mean = np.mean(coef)
    median = np.median(coef)
    return coef, mean, median