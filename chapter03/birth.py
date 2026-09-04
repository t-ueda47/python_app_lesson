"""出生の秘密アプリ"""

import FreeSimpleGUI as sg

# アプリの色合いを決める
sg.theme("DarkBrown3")

# レイアウト作成
layout = [
    [sg.Text("あなたの出生の秘密をお答えしましょう。")],
    [sg.Text("あなたは何歳？"), sg.Input("18", key="my_age")],
    [sg.Text("お母さんは何歳？"), sg.Input("48", key="mama_age")],
    [sg.Button("実行", key="btn"), sg.Text(key="txt")],
]

# アプリのウインドウ全体作成
window = sg.Window("出生の秘密アプリ", layout, font=(None, 14), size=(420, 170))


def execute():
    """母と自分の年齢を入れて出生日を計算"""
    my_age = int(values["my_age"])
    mama_age = int(values["mama_age"])
    txt = f"お母さんが{mama_age - my_age}歳のときあなたを産みましたよ。"
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
