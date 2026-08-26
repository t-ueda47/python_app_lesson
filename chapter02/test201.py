"""３つの部品を表示するアプリ"""

import FreeSimpleGUI as sg

# テキスト入力/ボタン/テキスト表示
layout = [
    [sg.Input("フタバ", key="in")],
    [sg.Button("実行", key="btn")],
    [sg.Text(key="txt")],
]

# アプリのウインドウ全体作成
window = sg.Window("あいさつテスト", layout)

# 入力待ち（プログラムがここで一時停止）
event, values = window.read()

# アプリを閉じる
window.close()
