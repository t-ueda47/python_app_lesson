"""干支調べアプリ"""

import FreeSimpleGUI as sg

# アプリの色合いを決める
sg.theme("DarkBrown3")

# レイアウト作成
layout = [
    [sg.Text("指定された年の干支を調べます。")],
    [sg.Text("西暦何年ですか？"), sg.Input("2022", key="century")],
    [sg.Button("実行", key="btn"), sg.Text(key="txt")],
]

# アプリのウインドウ全体作成
window = sg.Window("干支調べアプリ", layout, font=(None, 14), size=(320, 170))


def execute():
    """十二支"""
    eto = ["申", "酉", "戌", "亥", "子", "丑", "寅", "卯", "辰", "巳", "午", "未"]
    century = int(values["century"])
    etonum = century % 12
    txt = f"{century}年は、{eto[etonum]}年です。"
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
