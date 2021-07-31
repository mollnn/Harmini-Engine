from pydub import AudioSegment
from matplotlib import pyplot as plt
l=48
r=48+36-1
s=2

cnt=0

src = AudioSegment.from_wav("src.wav")
for i in range(l,r+1):
    filename="%03d.wav"%i
    t_l=cnt*s
    t_r=t_l+s
    cnt+=1
    wav = src[t_l*1000:t_r*1000]
    arr = wav.get_array_of_samples()
    # plt.plot(arr)
    # plt.show()
    wav.export(filename,format='wav')
