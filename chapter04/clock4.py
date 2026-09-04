"""時計アプリ（日付入り）"""

import datetime
import FreeSimpleGUI as sg

# アプリの色合いを決める
sg.theme("DarkBrown3")

# 1行目：年月日・曜日、2行目：時間の2行構成にする
# 第一引数に"0000/00/00"など入れなくても書き換わります
layout = [
    [
        sg.Text(
            font=("Arial", 20),
            key="txt_date",
            size=(20, 1),
            justification="center",
        )
    ],
    [
        sg.Text(
            font=("Arial", 40),
            key="txt",
            size=(20, 1),
            justification="center",
        )
    ],
]

# アプリのウインドウ全体作成
window = sg.Window("時計", layout, size=(400, 120), keep_on_top=True)


def execute():
    """現在時刻を表示する"""
    now = datetime.datetime.now()

    # 年月日と曜日（例: 2026年09月04日(Fri)）
    window["txt_date"].update(f"{now:%Y年%m月%d日(%a)}")
    # 時間とAM/PM（例: AM 09:30:15）
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
