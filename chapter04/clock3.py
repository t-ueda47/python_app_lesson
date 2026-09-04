"""時計アプリ"""

import datetime
import FreeSimpleGUI as sg

# アプリの色合いを決める
sg.theme("DarkBrown3")

# ウィンドウの中央に数字を入れるテキストエリア
layout = [
    [
        sg.Text(
            "AM 00:00:00",
            font=("Arial", 40),
            key="txt",
            size=(20, 1),
            justification="center",
        )
    ],
]

# アプリのウインドウ全体作成
window = sg.Window("時計", layout, size=(400, 80), keep_on_top=True)


def execute():
    """現在時刻を表示する"""
    now = datetime.datetime.now()
    window["txt"].update(f"{now:%p %I:%M:%S}")


# ループ
while True:
    # 0.5秒間イベントを待ち、何もなければ次へ進む
    event, values = window.read(timeout=500)
    if event is None:
        break
    execute()

# アプリを閉じる
window.close()
