"""数字が変わるアプリ"""

import FreeSimpleGUI as sg

# ウィンドウの中央に数字を入れるテキストエリア
layout = [
    [
        sg.Text(
            font=("Arial", 40),
            key="txt",
            size=(20, 1),
            justification="center",
        )
    ],
]

# アプリのウインドウ全体作成
# keep_on_top=windowを常に手前に
window = sg.Window("時計テスト", layout, size=(320, 80), keep_on_top=True)

# カウントアップする数字
counter = 0

# ループ
while True:
    # 0.5秒間イベントを待ち、何もなければ次へ進む
    event, values = window.read(timeout=500)
    counter = counter + 1

    window["txt"].update(f"{counter}")

    if event is None:
        break

# アプリを閉じる
window.close()
