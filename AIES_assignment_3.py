import itertools

def solution1():

    letters = ['s','e','n','d','m','o','r','y']
    digits = range(10)

    for p in itertools.permutations(digits, len(letters)):

        d = dict(zip(letters, p))

        if d['s'] == 0 or d['m'] == 0:
            continue

        send  = 1000*d['s'] + 100*d['e'] + 10*d['n'] + d['d']
        more  = 1000*d['m'] + 100*d['o'] + 10*d['r'] + d['e']
        money = 10000*d['m'] + 1000*d['o'] + 100*d['n'] + 10*d['e'] + d['y']

        if send + more == money:
            print("SEND + MORE = MONEY")
            return send, more, money


def solution2():

    letters = ['c','r','o','s','a','d','n','g','e']
    digits = range(10)

    for p in itertools.permutations(digits, len(letters)):

        d = dict(zip(letters, p))

        if d['c'] == 0 or d['r'] == 0:
            continue

        cross  = 10000*d['c'] + 1000*d['r'] + 100*d['o'] + 10*d['s'] + d['s']
        roads  = 10000*d['r'] + 1000*d['o'] + 100*d['a'] + 10*d['d'] + d['s']
        danger = 100000*d['d'] + 10000*d['a'] + 1000*d['n'] + 100*d['g'] + 10*d['e'] + d['r']

        if cross + roads == danger:
            print("CROSS + ROADS = DANGER")
            return cross, roads, danger


print(solution1())
print(solution2())