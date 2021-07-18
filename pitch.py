def pitchName2Level(pitch_name):
    ans=12+int(pitch_name[1])*12
    ans+={'A':-3,'B':-1,'C':0,'D':2,'E':4,'F':5,'G':7}[pitch_name[0]]
    if len(pitch_name)>2:
        if pitch_name[2]=='#': ans+=1
        if pitch_name[2]=='b': ans-=1
    return ans

if __name__=="__main__":
    print(pitchName2Level('C4'))
    print(pitchName2Level('C4b'))
    print(pitchName2Level('C4#'))
    print(pitchName2Level('E4'))