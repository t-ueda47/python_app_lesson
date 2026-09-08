"""ファイル保存ダイアログを表示するプログラム"""

from pathlib import Path
import FreeSimpleGUI as sg

# カレントディレクトリ（現在実行中のフォルダ）を初期位置に指定する
current_dir = Path.cwd()
savename = sg.popup_get_file(
    "テキストファイルを選択してください。", initial_folder="test.txt"
)
print(savename)
