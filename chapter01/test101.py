"""
tkinterのサンプル
"""

import tkinter as tk


def execute():
    """ボタンが押されたら走る関数"""
    txt = "こんにちは。"
    lbl.configure(text=txt)


root = tk.Tk()
root.title("こんにちはテスト")
root.geometry("400x200")

lbl = tk.Label(text="")
btn = tk.Button(text="実行", command=execute)

lbl.pack()
btn.pack()
tk.mainloop()
