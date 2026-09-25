"""QRコード作成アプリ"""

import io
from pathlib import Path
import qrcode  # QRコード使用
import FreeSimpleGUI as sg

# グローバル変数の初期定義
IMAGE = None
BASE_DIR = Path(__file__).parent  # Pythonファイルがあるディレクトリ

# アプリの色合いを決める
sg.theme("DarkBrown3")

# URLとURL入力エリア、QRコード作成ボタン、
# QRコード作成ボタン、ファイル保存ボタンとテキストエリア
# QRコード表示エリア
layout = [
    [
        sg.Text("URL"),
        sg.InputText(key="in1"),
    ],
    [
        sg.Button(
            "QRコード作成",
            key="btn1",
        ),
    ],
    [
        sg.Button(
            "ファイルを保存",
            key="btn2",
        ),
        sg.Text(key="txt"),
    ],
    [
        sg.Image(key="img"),
    ],
]

# アプリのウインドウ全体作成(resizable=Trueで可変にする)
window = sg.Window("QRコード作成", layout, size=(320, 400), resizable=True)


def execute():
    """QRコードを生成"""
    global IMAGE  # pylint: disable=global-statement
    if not values["in1"]:
        sg.PopupTimed("URLを入力してください。")
        return
    IMAGE = qrcode.make(values["in1"])  # QRコード画像を生成
    IMAGE.thumbnail((300, 300))
    bio = io.BytesIO()
    IMAGE.save(bio, format="PNG")
    window["img"].update(data=bio.getvalue())


def saveimage():
    """QRコード画像の保存"""
    if IMAGE is None:
        return
    savename = sg.popup_get_file(
        "png画像名をつけて保存してください。",
        save_as=True,
        initial_folder=str(BASE_DIR),
    )
    if not savename:
        sg.PopupTimed("png画像名を入力してください。")
        return
    if not savename.endswith(".png"):
        savename = savename + ".png"

    # ファイル名のみ返ってきた場合でも、選択フォルダ（BASE_DIR）配下に保存されるようパスを絶対パス化
    save_path = Path(savename)
    if not save_path.is_absolute():
        save_path = BASE_DIR / savename

    try:
        IMAGE.save(save_path)
        window["txt"].update(save_path.name + "を保存しました。")
    except (OSError, ValueError):  # ファイル保存に関するエラーのみを補足
        window["txt"].update("保存に失敗しました。")


while True:
    event, values = window.read()
    if event == "btn1":  # QRコード作成ボタン
        execute()
    if event == "btn2":  # ファイルに保存ボタン
        saveimage()
    if event is None:
        break
window.close()
