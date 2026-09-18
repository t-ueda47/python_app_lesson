"""画像読み込みアプリ"""

import io
import FreeSimpleGUI as sg
from PIL import Image

# アプリの色合いを決める
sg.theme("DarkBrown3")

# ファイルを開く、テキストエリア、画像表示エリア
layout = [
    [
        sg.Button(
            "ファイルを開く",
            key="btn1",
        ),
        sg.Text(key="txt"),
    ],
    [
        sg.Image(key="img", size=(400, 400), background_color="black"),
    ],
]
# アプリのウインドウ全体作成(resizable=Trueで可変にする)
window = sg.Window("画像ファイルを表示", layout, size=(400, 400), resizable=True)


def loadimage():
    """画像ファイルを読み込む"""
    loadname = sg.popup_get_file("画像ファイルを選択してください。")
    if not loadname:  # Noneや空文字列の場合はFalseになるので、notでTrueにする
        return  # ファイルを選択せずにOK押せばreturn

    try:
        # 画像ファイルを読み込む
        image = Image.open(loadname)
        # 画像をリサイズする
        image.thumbnail((400, 400))
        # 画像をバイナリデータに変換する
        bio = io.BytesIO()
        image.save(bio, format="PNG")
        # バイナリデータを取得する
        img_data = bio.getvalue()
        # 画像を表示する
        window["img"].update(data=img_data)
        window["txt"].update(loadname)
    except OSError:  # OSError（ファイル入出力系の汎用エラー）
        # sg.popup_error("画像ファイルの読み込みに失敗しました。")
        window["img"].update(data=None)
        window["txt"].update("画像ファイルの読み込みに失敗しました。")


while True:
    event, values = window.read()
    if event == "btn1":
        loadimage()
    if event is None:
        break
window.close()
