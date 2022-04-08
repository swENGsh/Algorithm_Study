def find_run(arr, player):
    for i in range(8):
        if i in arr and i+1 in arr and i+2 in arr:
            return player[-1]
    return

def find_triple(arr, player):
    cnt = [0] * 10
    for i in range(len(arr)):
        cnt[arr[i]] += 1
    if 3 in cnt:
        return player[-1]
    return

T = int(input())
for tc in range(1, T + 1):
    cards = list(map(int, input().split()))
    player1, player2 = [], []
    for card in range(len(cards)):
        if card % 2 == 0:
            player1.append(cards[card])
            if len(player1) >= 3:
                a = find_run(player1, 'player1')
                b = find_triple(player1, 'player1')
                if a :
                    print(a)
                    break
                elif b :
                    print(b)
                    break
        else:
            player2.append(cards[card])
            if len(player2) >= 3:
                c = find_run(player2, 'player2')
                d = find_triple(player2, 'player2')
                if c:
                    print(c)
                    break
                elif d:
                    print(d)
                    break
    else: print(0)


'''
3
9 9 5 6 5 6 1 1 4 2 2 1
5 3 2 9 1 5 2 0 9 2 0 0
2 8 7 7 0 2 2 2 5 4 0 3
'''