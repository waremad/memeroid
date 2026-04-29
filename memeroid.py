import os

#参照する音声ファイル
dir_path = "default"

#音声ファイル名の取得
chafiles = [f for f in os.listdir(dir_path+"/cha") if f.endswith(".wav")]
worfiles = [f for f in os.listdir(dir_path+"/wor") if f.endswith(".wav")]

#拡張子を除去
for i in range(len(chafiles)):
    chafiles[i] = chafiles[i][:-4]
for i in range(len(worfiles)):
    worfiles[i] = worfiles[i][:-4]

#listを文字数でソートする関数
def lst_sorted(lst):
    out = sorted(lst, key=len, reverse=True)
    return out

#lst = ["さ", "あ", "とうきょう", "さ", "にほん"]
#print(lst_sorted(lst))

#単語を文字数でソート
worfiles = lst_sorted(worfiles)

#print(chafiles,worfiles)

goal = input("??")

def wordsplit(lst):
