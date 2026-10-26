import random, math

# ボードの初期サイズ
board_size = 5

def generate_position(size):
    # 0以上size未満の範囲で、x座標とy座標を生成する
    x = random.randrange(0, size)
    y = random.randrange(0, size)

    return (x, y)

def calc_distance(pos1, pos2):
    # 2点間の距離を求める
    diff_x = pos1[0] - pos2[0]
    diff_y = pos1[1] - pos2[1]

    return math.sqrt(diff_x**2 + diff_y**2)

def move_position(direction, pos):
    # direction に従って、pos を移動する

    current_x, current_y = pos

    if direction == "w":
        current_y = current_y - 1
    elif direction == "a":
        current_x = current_x - 1
    elif direction == "s":
        current_y = current_y + 1
    elif direction == "d":
        current_x = current_x + 1

    return (current_x, current_y)

def suika_wari():
    # スイカの位置のタプル
    suika_pos = generate_position(board_size)
    # プレイヤーの位置のタプル
    player_pos = generate_position(board_size)

    # スイカとプレイヤーの座標が同じ場合、プレイヤーのみ座標を再取得する
    while (suika_pos == player_pos):
        player_pos = generate_position(board_size)

    # スイカとプレイヤーの位置が異なる間、処理を繰返す
    while (suika_pos != player_pos):

        #  スイカとプレイヤーの距離を表示
        distance = calc_distance(player_pos, suika_pos)
        print(f"スイカへの距離：{distance}")

        # キー入力に応じて、プレイヤーを移動する
        c = input("w：上に移動 a：左に移動 s：下に移動 d：右に移動：")
        player_pos = move_position(c, player_pos)

    print("スイカを割りました！")

suika_wari()

