from get_data import make_dfs


g_black, g_white, g_both = make_dfs(filename='lichess_grossmendPro_2018-01-30.pgn', playername='grossmendPro')

moves = g_white.moves

#print(moves)


all_games = list()

for ind, game in moves.iteritems():
    updated_game = list()
    for move in game:
        if "{" not in move and '-' not in move:
            updated_game.append(move)
    all_games.append(updated_game)

move_one = set()
move_two = set()
move_three = set()
moves_d = dict()
response_to_d4 = set()
last_move = set()

for game in all_games:
    if len(game) > 10:
        move_one.add(game[0])
        if game[0] == 'd4':
            response_to_d4.add(game[1])
            last_move.add(game[-1])

        move_two.add(game[2])

        move_three.add(game[4])


moves_d['d4'] = response_to_d4


print(move_one)
print(move_two)
print(move_three)

print(moves_d)

print(last_move)