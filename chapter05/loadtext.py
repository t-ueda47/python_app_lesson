"""テキスト読み込みアプリ"""

from pathlib import Path
import FreeSimpleGUI as sg
import chardet

# アプリの色合いを決める
sg.theme("DarkBrown3")

# Multilineウインドウとボタン
layout = [
    [
        sg.Button(
            "ファイルを開く",
            key="btn",
        ),
        sg.Text(key="button_txt"),
    ],
    [
        sg.Multiline(key="multi_txt", font=(None, 14), size=(80, 15)),
    ],
]
# アプリのウインドウ全体作成
window = sg.Window("テキストファイルの読み込み", layout)


def loadtext():
    """テキストファイルを読み込む"""
    loadname = sg.popup_get_file("テキストファイルを選択してください。")
    if not loadname:
        return  # ファイルを選択せずにOK押せばreturn

    with open(loadname, "rb") as file:
        raw_bytes = file.read()
        enc = chardet.detect(raw_bytes)["encoding"]
        path = Path(loadname)
        txt = path.read_text(encoding=enc)
        window["button_txt"].update(loadname)
        window["multi_txt"].update(txt)


# 入力待ちループ
while True:
    event, values = window.read()
    if event == "btn":
        loadtext()
    if event is None:
        break


# アプリを閉じる
window.close()
