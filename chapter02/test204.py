"""配色のテーマ"""

import FreeSimpleGUI as sg

# 全テーマ名を取得してソート(Python標準メソッド)
all_themes = sorted(sg.theme_list())

theme_rows = []

for theme_name in all_themes:
    # テーマごとの配色を適用してミニ画面ブロックを作る
    sg.theme(theme_name)

    # theme_previewer に含まれる要素をミニサイズで完全再現
    preview_elements = [
        [
            sg.Text("Text element", size=(10, 1)),
            sg.Input("Input data here", size=(12, 1)),
        ],
        [
            sg.Button("Ok", size=(4, 1)),
            sg.Button("Disabled", disabled=True, size=(7, 1)),
            sg.Checkbox("", default=True),
            sg.Slider(
                range=(1, 10),
                default_value=1,
                orientation="h",
                size=(12, 10),
                disable_number_display=True,
            ),
        ],
    ]

    # テーマ名をタイトルにした枠（Frame）で囲む
    frame = sg.Frame(
        title=theme_name,
        layout=preview_elements,
        title_color=sg.theme_text_color(),
        background_color=sg.theme_background_color(),
        pad=(5, 10),
    )

    theme_rows.append([frame])

# 全体をスクロール可能な Column で包む
layout = [
    [
        sg.Text(
            "全テーマ プレビュー一覧（スクロール対応）", font=("メイリオ", 12, "bold")
        )
    ],
    [
        sg.Column(
            theme_rows,
            scrollable=True,
            vertical_scroll_only=True,
            size=(360, 600),  # ウィンドウ内のスクロール表示領域サイズ
            expand_x=True,
            expand_y=True,
        )
    ],
    [sg.Button("閉じる", key="-CLOSE-")],
]

# メインウィンドウは標準テーマで表示
sg.theme("DefaultNoMoreNagging")
window = sg.Window("Theme Viewer Scrollable", layout, resizable=True)

while True:
    event, values = window.read()
    if event in (None, "-CLOSE-"):
        break

window.close()
