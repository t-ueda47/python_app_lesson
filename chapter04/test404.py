"""予定までどのくらい？"""

import datetime

# 3つのスケジュールがあります
sch = [
    ["朝礼", 8, 30],
    ["A社との打合せ", 15, 30],
    ["企画会議", 16, 40],
    ["資料整理", 17, 20],
]

now = datetime.datetime.now()  # 現在時刻取得
print(f"現在={now:%H:%M:%S}")  # 現在時刻表示

for s in sch:
    # 各スケジュールと現在時刻の差
    dt = now.replace(hour=s[1], minute=s[2], second=0) - now
    print(f"{s} = あと{dt}")
