def get_info(name):
    with open(name) as file:
        inf = file.readline().split()
        pairs = [pair.replace('\n', '') for pair in file.readlines()]
        return inf, pairs

def is_team(pair1, pair2):
    flag = False
    for mate in pair2:
        if mate in pair1 and mate != ' ':
            flag = True
            break
    return ('', pair2)[flag]

def get_teams(pairs):
    teams = []
    for i in range(len(pairs)):
        team = pairs[i]
        for j in range(len(pairs)):
            if pairs[i] is not pairs[j]:
                team += is_team(team, pairs[j])
        teams.append(team)
    return map(lambda x: set(x[:-1].split(' ')), teams)


def get_dis(inf, teams):
    teams = filter(lambda x: len(x) == int(inf[1]), teams)
    return teams

inf, pairs = get_info('input.txt')
for x in get_dis(inf, get_teams(pairs)):
    print(' '.join(x))
    break




