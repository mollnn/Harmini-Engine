from pyaudio import *
import wave
import random
import numpy as np

fmt = 8
channels = 2
rate = 44100
buffer = [[0]*10000000]*2


def read_wave_data(file_path):
    f = wave.open(file_path, "rb")
    params = f.getparams()
    nchannels, sampwidth, framerate, nframes = params[:4]
    str_data = f.readframes(nframes)
    f.close()
    wave_data = np.fromstring(str_data, dtype=np.short)
    wave_data=wave_data[:100000]
    wave_data.shape = -1, 2
    wave_data = wave_data.T
    time = np.arange(0, nframes) * (1.0/framerate)
    return wave_data


def put_sequence(filename, buf, position):
    position=int(position)
    clip = read_wave_data(filename)
    for i in range(len(clip[0])):
        buf[0][position+i] += clip[0][i]
        buf[1][position+i] += clip[1][i]


def put_sequence_to_buffer(filename, position):
    put_sequence(filename, buffer, position)

# def read(filename):
#     chunk = 1
#     wf = wave.open(filename,
#                 'rb')
#     pyau = PyAudio()
#     fmt=pyau.get_format_from_width(wf.getsampwidth())
#     channels=2
#     rate=wf.getframerate()
#     data = wf.readframes(chunk)
#     ans=[]
#     while data != b'':
#         val_left = int.from_bytes(data[:2], 'little', signed=True)
#         val_right = int.from_bytes(data[2:], 'little', signed=True)
#         ans.append([val_left,val_right])
#         data = wf.readframes(chunk)
#     pyau.terminate()
#     return ans


def play(seq):
    chunk = 1
    pyau = PyAudio()
    stream = pyau.open(format=fmt, channels=channels, rate=rate, output=True)
    length = len(seq[0])
    for i in range(length):
        val_left = int(seq[0][i])
        val_right = int(seq[1][i])
        val_left = min(32766, max(-32767, val_left))
        val_right = min(32766, max(-32767, val_right))
        val = 65536*val_left+val_right
        data = int.to_bytes(val, 4, 'little', signed=True)
        stream.write(data)                # 将帧写入数据流对象中，以此播放之
    stream.stop_stream()            # 停止数据流
    stream.close()                        # 关闭数据流
    pyau.terminate()                          # 关闭 PyAudio


def play_buffer():
    play(buffer)

# seq=read_wave_data("instrument/piano_gcd/060.wav")
# play(seq)


# put_sequence_to_buffer("instrument/piano_gcd/060.wav", 0)
# put_sequence_to_buffer("instrument/piano_gcd/060.wav", 50000)
# put_sequence_to_buffer("instrument/piano_gcd/060.wav", 100000)
# put_sequence_to_buffer("instrument/piano_gcd/060.wav", 150000)
# play_buffer()