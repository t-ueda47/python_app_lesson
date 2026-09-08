"""ファイル保存ダイアログを表示するプログラム"""

import FreeSimpleGUI as sg

savename = sg.popup_get_file(
    "名前をつけて保存してください。", default_path="test.txt", save_as=True
)
print(savename)
