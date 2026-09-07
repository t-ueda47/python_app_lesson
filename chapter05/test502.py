"""テキストファイルの読み込み"""

from pathlib import Path
import chardet


def loadtext(filename):
    """テキストファイルを読み込む"""
    with open(filename, "rb") as file:  # rb=バイナリーモード
        raw_bytes = file.read()  # ファイルオブジェクトをバイナリーに変換
        enc = chardet.detect(raw_bytes)["encoding"]  # 文字コードの取得
        path = Path(filename)  # Pathクラスからインスタンスを生成
        txt = path.read_text(encoding=enc)  # strオブジェクトを作成
        print(f"{filename}:{txt}")


loadtext("chapter05\\utest.txt")
loadtext("chapter05\\stest.txt")
