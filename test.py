import audio_engine
import pitch
import chord
import random


def getNote(pitch_name):
    return pitch.pitchName2Level(pitch_name)


def getChord(chord_name):
    pitch_name = chord_name[0:2]
    mode_name = chord_name[2:]
    return chord.getChord(getNote(pitch_name), mode_name)


def getRandomNoteInChord(chord_name):
    chord = getChord(chord_name)
    ans = random.choice(chord)
    return ans


def generatorNaive(harmony_proceed, num_note_in_chord):
    harmony_proceed = ['C4M', 'G4M', 'A5m',
                       'E4m', 'F4M', 'C4M', 'F4M', 'G4M', 'C4M']
    ans = []
    for chord_name in harmony_proceed:
        for i in range(num_note_in_chord):
            note = getRandomNoteInChord(chord_name)
            ans.append(note)
    return ans


def playNoteSeries(note_series, bpm=120):
    audio_engine.init()
    for i in note_series:
        audio_engine.play(i, 60/bpm)


if __name__ == "__main__":
    audio_engine.init()
    harmony_proceed = ['C4M', 'G4M', 'A5m',
                       'E4m', 'F4M', 'C4M', 'F4M', 'G4M', 'C4M']
    note_series = generatorNaive(harmony_proceed, 4)
    playNoteSeries(note_series, 120)
