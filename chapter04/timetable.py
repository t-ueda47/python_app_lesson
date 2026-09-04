"""時間割アプリ"""

import datetime
import FreeSimpleGUI as sg

# アプリの色合いを決める
sg.theme("DarkBrown3")

layout = [
    [
        sg.Text(
            font=("Arial", 24),
            key="txt",
        )
    ],
    [
        sg.ML(
            font=("Arial", 18),
            size=(40, 12),
            key="ml_txt",
        )
    ],
]

# アプリのウインドウ全体作成
window = sg.Window(
    "時間割アプリ", layout, font=(None, 14), size=(450, 260), keep_on_top=True
)


# スケジュール
sch = [
    ["1時限", 8, 50],
    ["2時限", 10, 30],
    ["昼休み", 12, 40],
    ["3時限", 13, 20],
    ["4時限", 15, 10],
    ["5時限", 17, 00],
    ["6時限", 18, 50],
]


def execute():
    """各スケジュールへの残り時間の書き換え"""
    now = datetime.datetime.now()  # 現在時刻取得
    window["txt"].update(f"{now:%H%M%S}")
    ml_txt = ""

    for s in sch:
        # 各スケジュールと現在時刻の差
        dt = now.replace(hour=s[1], minute=s[2], second=0) - now
        if dt.total_seconds() > 0:
            ml_txt += f"{s[0]}【{s[1]:02d}:{s[2]:02d}】あと{dt}です。\n"
        else:
            ml_txt += f"{s[0]}【{s[1]:02d}:{s[2]:02d}】---\n"
    window["ml_txt"].update(ml_txt)


while True:
    event, _ = window.read(timeout=500)  # valuesは使用しないのでダミー変数「_」
    if event is None:
        break
    execute()

# アプリを閉じる
window.close()
