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
                if random.randint(0, 1) == 0:
                    note += 12
                if len(ans) > 0:
                    ran = random.random()
                    if abs(note-ans[-1]) == 0 and ran > 0.0003:
                        continue
                    ran = random.random()
                    if math.pow(1.15, -abs(note-ans[-1])) < ran:
                        continue
                if len(ans) > 1:
                    ran = random.random()
                    if abs(note-ans[-2]) == 0 and ran > 0.003:
                        continue
                    ran = random.random()
                    if math.pow(1.05, -abs(note-ans[-2])) < 0.8*ran:
                        continue
                ans.append(note)
                break
    return ans


if __name__ == "__main__":
    harmony_proceed = ['C4M', 'G4M', 'A5m', 'E4m', 'F4M', 'C4M', 'F4M',
                       'G4M', 'F4M', 'G4M', 'E4m', 'A5m', 'D4m', 'G4M', 'C4M', 'C4M']

    bpm = 72*4*2
    music_desc = []
    tim = 0
    note_series = generatorNaive(harmony_proceed, 8)
    for i in range(len(note_series)):
        note = note_series[i]
        note_desc = {}
        note_desc["srcname"] = "instrument/piano_gcd/%03d.wav" % note
        note_desc["start"] = 0
        note_desc["duration"] = 400
        note_desc["offset"] = tim
        note_desc["power"] = -16+random.random()
        music_desc.append(note_desc)
        tim += 60000/bpm
    tim = 0
    note_series = generatorNaive(harmony_proceed, 4)
    for i in range(len(note_series)):
        note = note_series[i]
        note_desc = {}
        note_desc["srcname"] = "instrument/piano_gcd/%03d.wav" % note
        note_desc["start"] = 0
        note_desc["duration"] = 400
        note_desc["offset"] = tim
        note_desc["power"] = -5+random.random()
        music_desc.append(note_desc)
        tim += 2*60000/bpm
    for i in range(len(harmony_proceed)):
        c = getChord(harmony_proceed[i])
        tim = i*8*60000/bpm
        for note in c:
            note_desc = {}
            note_desc["srcname"] = "instrument/piano_gcd/%03d.wav" % (note-12)
            note_desc["start"] = 0
            note_desc["duration"] = 1600
            note_desc["offset"] = tim+4*60000/bpm
            note_desc["power"] = -19+random.random()
            music_desc.append(note_desc)
        for note in c[:1]:
            note_desc = {}
            note_desc["srcname"] = "instrument/piano_gcd/%03d.wav" % (note-24)
            note_desc["start"] = 0
            note_desc["duration"] = 1600
            note_desc["offset"] = tim
            note_desc["power"] = -12+random.random()
            music_desc.append(note_desc)
        offs = 0
        for note in c:
            offs += 1
            note_desc = {}
            note_desc["srcname"] = "instrument/piano_gcd/%03d.wav" % (note-24)
            note_desc["start"] = 0
            note_desc["duration"] = 1000
            note_desc["offset"] = tim+offs*60000/bpm
            note_desc["power"] = -17+random.random()
            music_desc.append(note_desc)
    print("start")
    audio_engine.playMusic(music_desc)