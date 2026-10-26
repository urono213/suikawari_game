import random, math

def calc_distance(pos1, pos2):
    diff_x = pos1[0] - pos2[0]
    diff_y = pos1[1] - pos2[1]

    return math.sqrt(diff_x**2 + diff_y**2)

# ボードの初期サイズ
board_size = 5
# スイカの位置のタプル
suika_pos = (random.randrange(0, board_size), random.randrange(0, board_size))
# プレイヤーの位置のタプル
player_pos = (random.randrange(0, board_size), random.randrange(0, board_size))

# スイカとプレイヤーの座標が同じ場合、プレイヤーのみ座標を再取得する
while (suika_pos == player_pos):
    player_pos = (random.randrange(0, board_size))

# ゲームの処理内容
while (suika_pos != player_pos):
    #  スイカとプレイヤーの距離を表示
    distance = calc_distance(player_pos, suika_pos)
    print(f"スイカへの距離：{distance}")

    # キー入力に応じて、プレイヤーを移動する
    c = input("w：上に移動 a：左に移動 s：下に移動 d：右に移動：")

    current_x, current_y = player_pos

    if c == "w":
        current_y = current_y - 1
    elif c == "a":
        current_x = current_x - 1
    elif c == "s":
        current_y = current_y + 1
    elif c == "d":
        current_x = current_x + 1

    player_pos = (current_x, current_y)

print("スイカを割りました！")


