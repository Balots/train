def get_turns(value, num):
    turns = {}
    for turn in range(value, num):
        for x in range(1, int(num**(0.5)) + 1):
            if x <= int((turn+x)**0.5):
                try:
                    turns[turn] += [x]
                except Exception:
                    turns[turn] = [x]
            else:
                break
    return turns


turns = get_turns(1, 10)
print(turns)


def turn(t, moves):
    moves = iter(moves)
    return None

print(turn(1, turns[1]))





