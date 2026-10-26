import random, math

def calc_distance(x1, y1, x2, y2):
    diff_x = x1 - x2
    diff_y = y1 - y2

    return math.sqrt(diff_x**2 + diff_y**2)

suika_x = random.randrange(0, 5)
suika_y = random.randrange(0, 5)

player_x = random.randrange(0, 5)
player_y = random.randrange(0, 5)

# スイカとプレイヤーの座標が同じ場合、プレイヤーのみ座標を再取得する
while (suika_x == player_x) and (suika_y == player_y):
    player_x = random.randrange(0, 5)
    player_y = random.randrange(0, 5)

# ゲームの処理内容
while (suika_x != player_x) or (suika_y != player_y):
    #  スイカとプレイヤーの距離を表示
    distance = calc_distance(player_x, player_y, suika_x, suika_y)
    print(f"スイカへの距離：{distance}")

    # キー入力に応じて、プレイヤーを移動する
    c = input("w：上に移動 a：左に移動 s：下に移動 d：右に移動：")
    if c == "w":
        player_y = player_y - 1
    elif c == "a":
        player_x = player_x - 1
    elif c == "s":
        player_y = player_y + 1
    elif c == "d":
        player_x = player_x + 1

print("スイカを割りました！")


