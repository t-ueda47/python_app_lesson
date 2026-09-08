"""ファイル選択ダイアログを表示するプログラム"""

import FreeSimpleGUI as sg

loadname = sg.popup_get_file("テキストファイルを選択してください。")
print(loadname)
