"""テキストファイルへの書き込み"""

from pathlib import Path


def savetext(filename):
    """テキストファイルへの書き込み"""
    path = Path(filename)
    txt = "書き出しテスト用のテキストデータです。"
    path.write_text(txt, encoding="UTF-8")


savetext("chapter05/output.txt")
