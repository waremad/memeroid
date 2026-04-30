import os
import unicodedata


#参照する音声ファイル
dir_path = "umehara"

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

#print(chafiles,worfiles)

#末尾の文字を母音
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

#1文字を子音
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

def boin_check():
    bo = ["あ","い","う","え","お"]
    non = []
    for i in bo:
        if not(i in chafiles):
            non.append(i)
    if len(non) == []:
        print("母音あり")
    else:
        print("不足母音",non)
    return non

def shiin_check():
    shi = ["か","さ","た","な","は","ま","や","ら","わ","が","ざ","だ","ば","ぱ"]
    for i in chafiles:
        if shiin(i) in shi:
            shi.pop(shi.index(shiin(i)))
    if len(shi) == []:
        print("子音あり")
    else:
        print("不足子音",shi)
    return shi

nom_boin = boin_check()
nom_shiin = shiin_check()
