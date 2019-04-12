# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 10:35:02 2019

@author: KonGiannos
"""

import music21 as m21
import numpy as np

def primeForm(pitchCollection):
    for i in range(len(pitchCollection)):
        pitchCollection[i] = pitchCollection[i]%12
    pitchCollection = list(set(pitchCollection)) #Remove duplicates
    pitchCollection.sort()
    test = pitchCollection + [pitchCollection[0]+12]
    
    
    # Find the largest ordered pitch-class interval
    interval = []
    for i in range(len(test)-1):
        interval.append(test[i+1] - test[i])
    # The position of the largest ordered interval.
    a = (len(interval)-1) - (interval.index(max(interval))) #np.roll() order is the reverse* of the index of max value
    pitchCollection = list(np.roll(pitchCollection,a)) # Get the normal order
    # Transpose so that the first pitch class is 0
    zero = pitchCollection[0]
    pitchCollection[0] = 0
    for i in range(len(pitchCollection)-1):
        pitchCollection[i+1] = (pitchCollection[i+1] - zero)%12

    #Invert the result
    interval1 = []
    for i in range(len(pitchCollection)-1):
        interval1.append(pitchCollection[i+1]-pitchCollection[i]) #order of intervals
    interval2 = interval1[::-1] #reverse the order of intervals
    ch = [pitchCollection[-1]]
    for i in range(len(interval2)):
        ch.append((ch[i]-interval2[i])%12) # write the pitch collection from top to bottom
    inverted = ch[::-1] # reverse the list so it starts from the lower note
    equalIntervals = []
    for i in range(len(interval1)):
            equalIntervals.append(interval1[i] == interval2[i]) # Boolean list where the intervals are compared
    for i in range(len(equalIntervals)): 
        if (equalIntervals[i] == False): # What happens if all values are true?
            if (interval1[i] < interval2[i]):
                final = pitchCollection
            else:
                final = inverted
            break # the checking stops when it finds the first unequal pair of intervals between the normal order and its inversion
    return final
        
def primeFormFromFile(fileName): # REWRITE
    p = m21.converter.parse(fileName)
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
    # Import module pitchClassSetCal and call function primeForm
    for ch in chordsAll:
        primeFormsAll = pitchClassSetCal.primeForm(ch)
    return primeFormsAll

"""
    # Order the pitch class sets 
    testChords = []
    for i in range(len(chordsAll)):
        chordsAll[i] = list(set(chordsAll[i])) #Remove duplicates
        chordsAll[i].sort()
        testChords.append(chordsAll[i]+[chordsAll[i][0]+12])
    
    # Find the largest ordered pitch-class interval
    for i in range(len(testChords)):
        interval = []
        for k in range(len(testChords[i])-1):
            interval.append(testChords[i][k+1] - testChords[i][k])
            # The position of the largest ordered interval.
            a = len(interval) - (interval.index(max(interval))) #np.roll() order is the reverse of the index of max value
        chordsAll[i] = list(np.roll(chordsAll[i],a)) # Get the normal order
    
    # Transpose so that the first pitch class is 0
    for chord in chordsAll:
        zero = chord[0]
        chord[0] = 0
        for k in range(len(chord)-1):
            chord[k+1] = (chord[k+1] - zero)%12

    #Invert the result
    inverted = []
    for chord in chordsAll:
        interval = []
        for i in range(len(chord)-1):
            interval.append(chord[i+1]-chord[i]) #order of intervals
        interval = interval[::-1] #reverse the order of intervals
        ch = [chord[-1]]
        for j in range(len(interval)):
            ch.append((ch[j]-interval[j])%12) # write the pitch collection from top to bottom
        ch = ch[::-1] # reverse the list so it starts from the lower note
        inverted.append(ch)    
"""