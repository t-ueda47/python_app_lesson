"""アプリの作り方を理解しよう"""

import FreeSimpleGUI as sg

# テキスト入力/ボタン/テキスト表示
layout = [
    [sg.Input("フタバ", key="in")],
    [sg.Button("実行", key="btn")],
    [sg.Text(key="txt")],
]

# アプリのウインドウ全体作成
window = sg.Window("あいさつテスト", layout)


def execute():
    """テキストを書き換える関数"""
    txt = "こんにちは、" + values["in"] + "さん！"
    window["txt"].update(txt)


# 入力待ちループ
while True:
    event, values = window.read()
    if event == "btn":
        execute()
    if event is None:
        break

# アプリを閉じる
window.close()
