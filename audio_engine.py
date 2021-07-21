from pydub import AudioSegment, playback

# Music Description
# [{srcname, start, duration, offset},{},{},...]


def readAudio(filename, format_name):
    return AudioSegment.from_file(filename, format_name)


def playMusic(music_desc):
    buf = AudioSegment.silent(duration=30000)
    for note_dec in music_desc:
        srcname = note_dec["srcname"]
        start = note_dec["start"]
        duration = note_dec["duration"]
        offset = note_dec["offset"]
        power = note_dec["power"]
        src_audio = readAudio(srcname, "wav")
        buf = buf.overlay(
            src_audio[start:start+duration].fade_out(300)+power, position=offset)
    playback.play(buf)
