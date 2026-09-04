"""ストップウォッチアプリ"""

import datetime
import FreeSimpleGUI as sg

# グローバル変数の初期定義
START_FLAG = False
START = None

# アプリの色合いを決める
sg.theme("DarkBrown3")

layout = [
    [
        sg.Text(
            font=("Arial", 40),
            key="txt",
            size=(20, 1),
            justification="center",
        )
    ],
    [
        sg.Push(),
        sg.B("START/STOP", k="btn"),
        sg.Push(),
    ],
]

# アプリのウインドウ全体作成
window = sg.Window("ストップウォッチ", layout, size=(400, 120), keep_on_top=True)


def execute():
    """経過時間を表示する"""
    if START_FLAG:  # フラグがカウント中なら
        now = datetime.datetime.now()
        delta = now - START  # 経過時間を算出
        window["txt"].update(delta)  # 経過時間を表示


def startstop():
    """ボタンが押されたら呼び出される
    スタートとストップを切り替える"""
    global START, START_FLAG  # pylint: disable=global-statement
    if START_FLAG:  # カウント中なら
        START_FLAG = False  # フラグを停止中にする
    else:
        START = datetime.datetime.now()  # カウント開始
        START_FLAG = True  # フラグをカウント中にする


while True:
    # 0.5秒間イベントを待ち、何もなければ次へ進む
    event, values = window.read(timeout=50)

    if event == "btn":
        startstop()
    if event is None:
        break
    execute()

# アプリを閉じる
window.close()
