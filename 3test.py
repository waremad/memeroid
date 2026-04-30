from pydub import AudioSegment

dir_path = "umehara"

a = AudioSegment.from_wav(dir_path+"/cha/"+"う.wav")
b = AudioSegment.from_wav(dir_path+"/cha/"+"か.wav")

c = a.overlay(b)

c.export("く.wav", format="wav")