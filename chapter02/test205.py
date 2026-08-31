"""
こんにちは、〇〇さん！
アプリ（色違い）
"""

import FreeSimpleGUI as sg

# アプリの色合いを決める
sg.theme("BrightColors")

# テキスト入力/ボタン/テキスト表示
layout = [
    [sg.Input("フタバ", key="in")],
    [sg.Button("実行", key="btn")],
    [sg.Text(key="txt")],
]

# アプリのウインドウ全体作成
window = sg.Window("あいさつテスト", layout, font=(None, 14), size=(250, 120))


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
