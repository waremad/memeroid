import os

dir_path = "default"

chafiles = [f for f in os.listdir(dir_path+"/cha") if f.endswith(".wav")]
worfiles = [f for f in os.listdir(dir_path+"/wor") if f.endswith(".wav")]

for i in range(len(chafiles)):
    chafiles[i] = chafiles[i][:-4]
for i in range(len(worfiles)):
    worfiles[i] = worfiles[i][:-4]

print(chafiles,worfiles)

goal = input("??")
