"""テキスト読み込みアプリ"""

from pathlib import Path
import FreeSimpleGUI as sg
import chardet

# グローバル変数の初期定義
LOAD_NAME = None
ENC = "UTF-8"

# アプリの色合いを決める
sg.theme("DarkBrown3")

# Multilineウインドウとファイルを開く、ファイルを保存ボタン
layout = [
    [
        sg.Button(
            "ファイルを開く",
            key="btn_load",
        ),
        sg.Text(key="button_txt"),
    ],
    [
        sg.Button(
            "ファイルを保存",
            key="btn_save",
        ),
    ],
    [
        sg.Multiline(key="multi_txt", font=(None, 14), size=(80, 15)),
    ],
]
# アプリのウインドウ全体作成(resizable=Trueで可変にする)
window = sg.Window("テキストファイルの保存", layout, resizable=True)


def loadtext():
    """テキストファイルを読み込む"""

    global LOAD_NAME, ENC  # pylint: disable=global-statement

    LOAD_NAME = sg.popup_get_file("テキストファイルを選択してください。")
    if not LOAD_NAME:
        return  # ファイルを選択せずにOK押せばreturn

    with open(LOAD_NAME, "rb") as file:
        raw_bytes = file.read()
        ENC = chardet.detect(raw_bytes)["encoding"]
        path = Path(LOAD_NAME)
        txt = path.read_text(encoding=ENC)
        window["button_txt"].update(LOAD_NAME)
        window["multi_txt"].update(txt)


def savetext():
    """MultiTxtに書かれた文字を保存する"""
    global LOAD_NAME  # pylint: disable=global-statement

    savename = sg.popup_get_file(  # ファイル保存ダイアログを開く
        "名前をつけて保存してください。", default_path=LOAD_NAME, save_as=True
    )

    if not savename:
        sg.PopopTimed("ファイル名を入力してください。")
        return
    if savename.find(".") == -1:
        savename = savename + ".txt"  # 拡張子がなければ追加

    p = Path(savename)
    p.write_text(values["multi_txt"], encoding=ENC)
    window["button_txt"].update(savename)
    LOAD_NAME = savename


# 入力待ちループ
while True:
    event, values = window.read()
    if event == "btn_load":
        loadtext()
    if event == "btn_save":
        savetext()
    if event is None:
        break


# アプリを閉じる
window.close()
