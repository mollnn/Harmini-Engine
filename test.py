import audio_engine
import pitch
import chord

def Note(pitch_name):
    return pitch.pitchName2Level(pitch_name)

if __name__=="__main__":
    audio_engine.init()
    audio_engine.play(Note('C4'))
    audio_engine.play(Note('E4'))
    audio_engine.play(Note('G4'))
    audio_engine.play(Note('C5'))