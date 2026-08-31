"""
文字列のレイアウトテスト
"""

import FreeSimpleGUI as sg

# アプリの色合いを決める
sg.theme("DarkBrown3")

# テキスト表示。インプット表示
layout = [
    [sg.Text("ABCDE", size=(30, 1), justification="left")],
    [sg.Text("ABCDE", size=(30, 1), justification="center")],
    [sg.Input("ABCDE", size=(30, 1), justification="right")],
]

# アプリのウインドウ全体作成
window = sg.Window("文字列レイアウトテスト", layout, font=(None, 14), size=(300, 120))

# 入力待ち（プログラムがここで一時停止）
event, values = window.read()

# アプリを閉じる
window.close()
