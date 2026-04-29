from pydub import AudioSegment

dir_path = "default/cha/"
files = list("ささいいいいいぞぞいぞいぞい")

a = AudioSegment.from_wav(dir_path+files[0]+".wav")
files.pop(0)

for i in files:
    b = AudioSegment.from_wav(dir_path+i+".wav")
    a = a + b
a.export("output.wav", format="wav")
