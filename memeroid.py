import os
import unicodedata
from pydub import AudioSegment
from datetime import datetime



#参照する音声ファイル
dir_path = "umehara"
long_time = 200

#音声ファイル名の取得
chafiles = [f for f in os.listdir(dir_path+"/cha") if f.endswith(".wav")]
worfiles = [f for f in os.listdir(dir_path+"/wor") if f.endswith(".wav")]

#拡張子を除去
for i in range(len(chafiles)):
    chafiles[i] = unicodedata.normalize("NFC",chafiles[i][:-4])
for i in range(len(worfiles)):
    worfiles[i] = unicodedata.normalize("NFC", worfiles[i][:-4])

#listを文字数でソートする関数
def lst_sorted(lst):
    out = sorted(lst, key=len, reverse=True)
    return out

#lst = ["さ", "あ", "とうきょう", "さ", "にほん"]
#print(lst_sorted(lst))

#単語を文字数でソート
worfiles = lst_sorted(worfiles)
chafiles = sorted(chafiles)

print(chafiles,worfiles)

#
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
            a = nt.find(ni)
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
def bar_boin(text):
    aiueo=[
        ["あ","か","さ","た","な","は","ま","や","ら","わ","が","ざ","だ","ば","ぱ","ぁ","ゃ"],
        ["い","き","し","ち","に","ひ","み","り","ぎ","じ","ぢ","び","ぴ","ぃ"],
        ["う","く","す","つ","ぬ","ふ","む","ゆ","る","ん","ぐ","ず","づ","ぶ","ぷ","ぅ","ゅ"],
        ["え","け","せ","て","ね","へ","め","れ","げ","ぜ","で","べ","ぺ","ぇ"],
        ["お","こ","そ","と","の","ほ","も","よ","ろ","を","ご","ぞ","ど","ぼ","ぉ","ょ"]
    ]
    print("text",text)
    text = text[-2]

    for k in aiueo:
        if text in k:
            return k[0]+"ー"

#
wordlst = wordsplit(goal)
#wordlst = [""]

#伸ばし棒処理
j = 0
for i in range(len(wordlst)):
    if "ー" in wordlst[i+j]:
        print("wordlst[i+j]",wordlst[i+j])
        wordlst.insert(i+j+1, bar_boin(wordlst[i+j]))
        print("wordlst",wordlst)
        wordlst[i+j] = wordlst[i+j][:-1]
        j += 1

print(wordlst)

#末尾の文字の母音
def boin(text):
    aiueo=[
        ["あ","か","さ","た","な","は","ま","や","ら","わ","が","ざ","だ","ば","ぱ","ぁ","ゃ"],
        ["い","き","し","ち","に","ひ","み","り","ぎ","じ","ぢ","び","ぴ","ぃ"],
        ["う","く","す","つ","ぬ","ふ","む","ゆ","る","ん","ぐ","ず","づ","ぶ","ぷ","ぅ","ゅ"],
        ["え","け","せ","て","ね","へ","め","れ","げ","ぜ","で","べ","ぺ","ぇ"],
        ["お","こ","そ","と","の","ほ","も","よ","ろ","を","ご","ぞ","ど","ぼ","ぉ","ょ"]
    ]

    for k in aiueo:
        if text[-1] in k:
            return k[0]

#1文字の子音
def shiin(text):
    akstn=[
        ["あ","い","う","え","お"],
        ["か","き","く","け","こ"],
        ["さ","し","す","せ","そ"],
        ["た","ち","つ","て","と"],
        ["な","に","ぬ","ね","の","ん",],
        ["は","ひ","ふ","へ","ほ"],
        ["ま","み","む","め","も"],
        ["や","ゆ","よ"],
        ["ら","り","る","れ","ろ"],
        ["わ","を"],
        ["が","ぎ","ぐ","げ","ご"],
        ["ざ","じ","ず","ぜ","ぞ"],
        ["だ","ぢ","づ","で","ど"],
        ["ば","び","ぶ","べ","ぼ"],
        ["ぱ","ぴ","ぷ","ぺ","ぽ"]
    ]

    for k in akstn:
        if text in k:
            return k[0]

#ない一文字合成
def one_docking(text):
    text_boin = boin(text)
    text_shiin = shiin(text)
    print(text_boin,text_shiin,chafiles)
    if text_boin in chafiles:
        print(1,text_boin,text_shiin)
        index_shiin = -1
        for i in chafiles:
            if shiin(i) == text_shiin:
                index_shiin = chafiles.index(i)
                break
        print(2,index_shiin)
        if index_shiin == -1:
            raise ValueError(f"音声なし: {text}")
        else:
            a = AudioSegment.from_wav(dir_path+"/cha/"+text_boin+".wav")
            b = AudioSegment.from_wav(dir_path+"/cha/"+chafiles[index_shiin]+".wav")
            return a.overlay(b)
    else:
        raise ValueError(f"音声なし: {text}")

#ない文字合成
def docking(text):
    if len(text) == 1:
        if text in ["っ"," ","　","_","＿"]:
            return AudioSegment.silent(duration=long_time)
        elif text in [",","，","、",".","．","。"]:
            return AudioSegment.silent(duration=long_time*2)
        else:
            return one_docking(text)
    elif text[-1] == "ー":
        if text[-2] in chafiles:
            a = AudioSegment.from_wav(dir_path+"/cha/"+text[-2]+".wav")
            return a+a
        else:
            raise ValueError(f"音声なし: {text}")
    elif text[-1] in mini_bar:
        if len(text) == 2:
            a = docking(text[0])
            b = docking(text[1])
            return a+b
        else:
            raise ValueError(f"音声なし: {text}")
    else:
        raise ValueError(f"音声なし: {text}")

#文字や単語を音声ファイルに変換する関数
def audio_worcha(text):
    if text == "　":
        text = "_"

    if text in chafiles:
        audio = AudioSegment.from_wav(dir_path+"/cha/"+text+".wav")
    elif text in worfiles:
        audio = AudioSegment.from_wav(dir_path+"/wor/"+text+".wav")
    else:
        audio = docking(text)

    print(text)

    # 長さが足りない場合に無音追加
    if len(audio) < long_time:
        silence = AudioSegment.silent(duration=long_time - len(audio))
        audio = audio + silence

    return audio

a = audio_worcha(wordlst[0])
wordlst.pop(0)

for i in wordlst:
    b = audio_worcha(i)
    a = a + b

s = datetime.now().strftime("%Y%m%d_%H%M")
a.export(s+"_"+goal+".wav", format="wav")
