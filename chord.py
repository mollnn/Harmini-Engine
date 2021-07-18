chord_modes = {'M':[0,4,7], 'm':[0,3,7]}

def getChord(start, mode_name='M'):
    chord_mode = chord_modes[mode_name]
    return [i+start for i in chord_mode]