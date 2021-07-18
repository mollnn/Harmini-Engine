from pygame import mixer 
import time

def init(): 
    mixer.init()

def play(id=60, duration=1):
    mixer.music.load("instrument/piano_gcd/%03d.wav"%id)
    mixer.music.play()
    time.sleep(duration)
    mixer.music.stop()

if __name__=="__main__":
    init()
    play(60,0.5)
    play(62,0.5)
    play(64,0.5)
    play(65,0.5)
    play(67,0.5)
    play(69,0.5)
    play(71,0.5)
    play(72,2)