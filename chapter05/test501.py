"""テキストの文字コードを調べる"""

import chardet


def loadtext(filename):
    """受け取ったファイルの文字コード調べる"""
    with open(filename, "rb") as file:  # rb=バイナリーモード
        raw_bytes = file.read()  # ファイルオブジェクトをバイナリーに変換
        enc = chardet.detect(raw_bytes)["encoding"]
        print(f"{filename}は、{enc}")


loadtext("chapter05\\utest.txt")
loadtext("chapter05\\stest.txt")
