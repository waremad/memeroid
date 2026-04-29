import os
import unicodedata

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

mini_bar = ["ぁ","ぃ","ぅ","ぇ","ぉ","ゃ","ゅ","ょ","ー"]

#文字列を単語優先で分割する関数
def wordsplit(text,worfiles=worfiles):
    #print(text)
    if text == "":
        return []
    if len(text) == 1:
        return [text]
    if len(text) == 2 and text[1] in mini_bar:
        return [text]
    out = []
    for i in worfiles:
        ni = unicodedata.normalize("NFC", i)
        nt = unicodedata.normalize("NFC", text)

        #print(0,i,text,ni in nt)
        if ni in nt:
            #print(1,ni,nt)
            a = text.find(ni)
            b = a + len(ni)
            if b == len(nt):
                #print(2,b,len(nt))
                return wordsplit(nt[:a]) + [nt[a:b]] + wordsplit(nt[b:])
            if nt[b] in mini_bar:
                pass
            else:
                #print(3,b,len(nt))
                return wordsplit(nt[:a]) + [nt[a:b]] + wordsplit(nt[b:])
            #print(4,a,b,text)
    nt = unicodedata.normalize("NFC", text)
    for i in nt:
        if i in mini_bar:
            out[-1] += i
        else:
            out.append(i)
    #print(out)
    return out

#伸ばし棒の前の文字を母音にして返す
def boin(text):
    aiueo=[
        ["あ","か","さ","た","な","は","ま","や","ら","わ","が","ざ","だ","ば","ぱ","ぁ","ゃ"],
        ["い","き","し","ち","に","ひ","み","り","ぎ","じ","ぢ","び","ぴ","ぃ"],
        ["う","く","す","つ","ぬ","ふ","む","ゆ","る","ん","ぐ","ず","づ","ぶ","ぷ","ぅ","ゅ"],
        ["え","け","せ","て","ね","へ","め","れ","げ","ぜ","で","べ","ぺ","ぇ"],
        ["お","こ","そ","と","の","ほ","も","よ","ろ","を","ご","ぞ","ど","ぼ","ぉ","ょ"]
    ]

    text = text[-2]

    for i in aiueo:
        if text in i:
            return i[0]+"ー"

wordlst = wordsplit(goal)

#伸ばし棒処理
j = 0
for i in range(len(wordlst)):
    if "ー" in wordlst[i+j]:
        wordlst.insert(i+j+1, boin(wordlst[i]))
        wordlst[i+j] = wordlst[i+j][:-1]
        j += 1



print(wordlst)
