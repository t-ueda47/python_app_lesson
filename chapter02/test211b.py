"""
いろいろな部品のテストB
"""

import FreeSimpleGUI as sg

# アプリの色合いを決める
sg.theme("DarkBrown3")

# レイアウト設定
layout = [
    [sg.Text("テキストエリアでも\n複数行は表示できます")],
    [sg.Input("入力欄")],
    [
        sg.Multiline(
            "【第1条】\n本アプリは学習用プロトタイプです。\n\n【第2条】\n無断転載を禁じます。",
            size=(45, 5),
            font=("MS Gothic", 12),  # フォントをMS ゴシック・サイズ12に指定
            disabled=True,  # 編集不可（読み取り専用）に設定
        )
    ],
    [sg.Image("chapter02/futaba.png")],
]

# アプリのウインドウ全体作成
window = sg.Window("入力欄テスト", layout, font=(None, 14), size=(400, 240))

# 入力待ち（プログラムがここで一時停止）
event, values = window.read()

# アプリを閉じる
window.close()
