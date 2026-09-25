"""
FreeSimpleGUIのサンプル
"""

import FreeSimpleGUI as sg

layout = [[sg.T(k="txt")], [sg.B("実行", k="btn")]]
win = sg.Window("こんにちはテスト", layout, size=(200, 100))


def execute():
    """ボタンが押されたら走る関数"""
    win["txt"].update("こんにちは")


while True:
    e, v = win.read()
    if e == "btn":
        execute()
    if e is None:
        break
win.close()
