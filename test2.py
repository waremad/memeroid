import random

ls = ["い","く","ぞ","さ","あ"]

out = ""
for i in range(20):
    out += random.choice(ls)
print(out)
