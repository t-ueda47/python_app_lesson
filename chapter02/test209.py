"""
レイアウト（２次元配列）のテスト
"""

import FreeSimpleGUI as sg

# アプリの色合いを決める
sg.theme("DarkBrown3")

# テキスト表示。ボタン表示
layout = [
    [sg.Text("1行1列目"), sg.Text("1行2列目")],
    [sg.Text("2行1列目"), sg.Text("2行2列目")],
    [sg.Text("3行1列目"), sg.Button("ボタン")],
]

# アプリのウインドウ全体作成
window = sg.Window("要素レイアウトテスト", layout, font=(None, 14), size=(250, 120))

# 入力待ち（プログラムがここで一時停止）
event, values = window.read()

# アプリを閉じる
window.close()
