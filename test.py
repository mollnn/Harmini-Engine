import audio_engine
import pitch
import chord
import random
import math


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
    ans = []
    for chord_name in harmony_proceed:
        for i in range(num_note_in_chord):
            while True:
                note = getRandomNoteInChord(chord_name)
                if random.randint(0, 2) == 0:
                    note -= 12
                if len(ans) > 0:
                    ran = random.random()
                    if abs(note-ans[-1]) == 0 and ran > 0.001:
                        continue
                    ran = random.random()
                    if math.pow(2, -abs(note-ans[-1])) < ran:
                        continue
                if len(ans) > 1:
                    ran = random.random()
                    if abs(note-ans[-2]) == 0 and ran > 0.01:
                        continue
                    ran = random.random()
                    if math.pow(1.2, -abs(note-ans[-2])) < 0.8*ran:
                        continue
                ans.append(note)
                break
    return ans


def playNoteSeries(note_series, bpm=120):
    audio_engine.init()
    for i in note_series:
        audio_engine.play(i, 60/bpm)


if __name__ == "__main__":
    audio_engine.init()
    harmony_proceed = ['C4M', 'G4M', 'A5m', 'E4m', 'F4M', 'C4M', 'F4M',
                       'G4M', 'F4M', 'G4M', 'E4m', 'A5m', 'D4m', 'G4M', 'C4M', 'C4M']
    note_series = generatorNaive(harmony_proceed, 4)
    playNoteSeries(note_series, 180)
