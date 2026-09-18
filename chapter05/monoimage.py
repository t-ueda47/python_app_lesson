"""画像の加工（モノクロ）アプリ"""

import io
import os  # パス操作用に追加
import FreeSimpleGUI as sg
from PIL import Image

# グローバル変数の初期定義
IMAGE = None
LOAD_DIR = None  # ファイルパスではなく「フォルダーパス」を保持する

# アプリの色合いを決める
sg.theme("DarkBrown3")

# ファイルを開く/保存ボタン、テキストエリア、画像表示エリア
layout = [
    [
        sg.Button(
            "ファイルを開く",
            key="btn1",
        ),
        sg.Text(key="txt"),
    ],
    [
        sg.Button(
            "ファイルを保存",
            key="btn2",
        ),
    ],
    [
        sg.Image(key="img", size=(400, 400), background_color="black"),
    ],
]

# アプリのウインドウ全体作成(resizable=Trueで可変にする)
window = sg.Window("モノクロ画像に変換", layout, size=(320, 400), resizable=True)


def loadimage():
    """画像ファイルを読み込む"""

    global IMAGE, LOAD_DIR  # pylint: disable=global-statement

    loadname = sg.popup_get_file("画像ファイルを選択してください。")
    if not loadname:
        return

    try:
        # 読み込んだファイルの「フォルダーの場所」だけを取得して保存
        LOAD_DIR = os.path.dirname(loadname)

        # 画像ファイルを読み込む(モノクロ加工)
        IMAGE = Image.open(loadname).convert("L")

        # 表示用コピーを作成してリサイズ（元画像の高解像度を保持）
        img_display = IMAGE.copy()
        img_display.thumbnail((300, 300))

        # 画像をバイナリデータに変換する
        bio = io.BytesIO()
        img_display.save(bio, format="PNG")

        # バイナリデータを取得する
        img_data = bio.getvalue()

        # 画面の表示欄（txt）にもフルパスではなく「ファイル名のみ」を表示したい場合は os.path.basename を使用
        filename = os.path.basename(loadname)
        window["img"].update(data=img_data)
        window["txt"].update(filename)
    except OSError:
        window["img"].update(data=None)
        window["txt"].update("画像ファイルの読み込みに失敗しました。")


def saveimage():
    """画像ファイルの保存"""
    if IMAGE is None:
        return

    # initial_folder で開く場所を指定し、default_path は指定しない（または空にする）
    save_input = sg.popup_get_file(
        "保存するファイル名を入力してください（例: output.png）",
        save_as=True,
        initial_folder=LOAD_DIR,  # 開くフォルダーを元画像と同じ場所に固定
        default_extension=".png",
    )

    if not save_input:
        sg.PopupTimed("ファイル名を入力してください。")
        return

    # ユーザーがフォルダーを選び直さずファイル名だけ入力した場合、またはパス付きの場合に対応
    if not os.path.isabs(save_input):
        # ファイル名だけが入力された場合、読み込み元フォルダーと結合する
        savename = os.path.join(LOAD_DIR, save_input)
    else:
        savename = save_input

    if not savename.endswith(".png"):
        savename = savename + ".png"

    try:
        IMAGE.save(savename)
        saved_filename = os.path.basename(savename)
        window["txt"].update(saved_filename + " を保存しました。")
    except OSError:
        window["txt"].update("失敗しました。")


while True:
    event, values = window.read()
    if event == "btn1":
        loadimage()
    if event == "btn2":
        saveimage()

    if event is None:
        break
window.close()
