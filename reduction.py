# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 11:24:37 2019

@author: KonGiannos
"""

import music21 as m21

def chordifyReduction(pieceName):
    # parse piece
    p = m21.converter.parse(pieceName)
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
    return chordsAll  