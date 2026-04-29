from memeroid import *

def test_wordsplit():
    assert wordsplit("はしん",["はし"]) == ["はし","ん"]
    assert wordsplit("はしょうふう",["はし"]) == ["は","しょ","う","ふ","う"]
    assert wordsplit("はーん",[]) == ["はー","ん"]
    assert wordsplit("あわいどしょー",["あわいどし","どしょー"]) == ["あ","わ","い","どしょー"]
    assert wordsplit("いさささあぞいくいいくぞ",['いくぞ', 'さあ']) == ['い', 'さ', 'さ', 'さあ', 'ぞ', 'い', 'く', 'い', 'いくぞ']
