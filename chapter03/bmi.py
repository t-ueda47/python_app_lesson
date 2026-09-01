"""BMI値計算アプリ"""

import FreeSimpleGUI as sg

# アプリの色合いを決める
sg.theme("DarkBrown3")

# レイアウト作成
layout = [
    [sg.Text("身長と体重を入力してください")],
    [sg.Text("身長cm"), sg.Input("160", key="height")],
    [sg.Text("体重kg"), sg.Input("60", key="weight")],
    [sg.Button("実行", key="btn"), sg.Text(key="txt")],
]

# アプリのウインドウ全体作成
window = sg.Window("BMI計算アプリ", layout, font=(None, 14), size=(320, 150))


def execute():
    """BMIを計算し、画面のテキストを更新する関数。"""
    height = float(values["height"]) / 100.0
    weigt = float(values["weight"])
    bmi = weigt / (height * height)
    txt = f"BMI値は、{bmi:.2f}です。"
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
