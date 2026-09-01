"""わりかんアプリ"""

import FreeSimpleGUI as sg

# アプリの色合いを決める
sg.theme("DarkBrown3")

# レイアウト作成
layout = [
    [sg.Text("金額と人数を入力してください")],
    [sg.Text("金額"), sg.Input("1000", key="price")],
    [sg.Text("人数"), sg.Input("4", key="member_count")],
    [sg.Button("実行", key="btn"), sg.Text(key="txt")],
]

# アプリのウインドウ全体作成
window = sg.Window("割り勘アプリ", layout, font=(None, 14), size=(320, 150))


def execute():
    """割り勘計算を実行し、画面のテキストを更新する関数。"""
    price = int(values["price"])
    member_count = int(values["member_count"])
    txt = f"1人,{price/member_count: .2f}円"  # 小数点2桁まで
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
