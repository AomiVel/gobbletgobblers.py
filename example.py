from main import GobbletGobblers
gobb = GobbletGobblers('佐藤', '田中', '  ')

print(f'先攻: {gobb.sen.player} ({gobb.sen.color})\n後攻: {gobb.kou.player} ({gobb.kou.color})')
input('\n確認ができたらEnterキーを押してください')
print('\n\n')
while not gobb.won:
    print(f'''   1111 2222 3333
  +----+----+----+
A | {gobb.board['a1']['t']} | {gobb.board['a2']['t']} | {gobb.board['a3']['t']} | A
  +----+----+----+
B | {gobb.board['b1']['t']} | {gobb.board['b2']['t']} | {gobb.board['b3']['t']} | B
  +----+----+----+
C | {gobb.board['c1']['t']} | {gobb.board['c2']['t']} | {gobb.board['c3']['t']} | C
  +----+----+----+
   1111 2222 3333''')
    print(f'\n{gobb.now_player.player} ({gobb.now_player.color}) のターンです ({gobb.turn}ターン目)')
    print(f'手持ちのゴブレット: [ {", ".join(gobb.now_player.gobbs)} ]')
    mode = input(f'選択可能なモード: [ {", ".join(gobb.now_player.modes)} ]\n    mode: ')
    if mode == 'p':
        choices_put = gobb.choices_put()
        place = input(f'設置可能場所: [ {", ".join([key for key in choices_put.keys() if not choices_put[key] == None])} ]\n    place: ')
        size = input(f'選択可能サイズ: [ {", ".join(choices_put[place])} ]\n    size: ')
        gobb.put(place, size)
    if mode == 'm':
        choices_move_from = gobb.choices_move_from()
        from_ = input(f'移動可能ゴブレットの場所: [ {", ".join(choices_move_from)} ]\n    place: ')
        choices_move_to = gobb.choices_move_to(from_)
        to = input(f'選択可能な移動先: [ {", ".join(choices_move_to)} ]\n    place: ')
        gobb.move(from_, to)

print(f'\n勝者: {gobb.winner.player} ({gobb.winner.color})\n')
