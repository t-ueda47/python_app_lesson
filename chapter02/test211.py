"""
いろいろな部品のテスト
"""

import FreeSimpleGUI as sg

# アプリの色合いを決める
sg.theme("DarkBrown3")

# レイアウト設定
layout = [
    [sg.Text("テキストエリアでも\n複数行は表示できます")],
    [sg.Input("入力欄")],
    [sg.Multiline("複数行テキスト　１行目\n２行目", size=(30, 3))],
    [sg.Image("chapter02/futaba.png")],
]

# アプリのウインドウ全体作成
window = sg.Window("入力欄テスト", layout, font=(None, 14), size=(300, 240))

# 入力待ち（プログラムがここで一時停止）
event, values = window.read()

# アプリを閉じる
window.close()
