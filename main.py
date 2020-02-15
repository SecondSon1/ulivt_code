def chess_to_cartesian(coord):
    letter = coord[0]
    num = coord[1]
    return ord(letter) - ord('a'), int(num) - 1


def possible(coord):
    if coord in coords:
        return False
    return not (coord[0] < 0 or coord[0] > 7 or coord[1] < 0 or coord[1] > 7)


knight, n = map(str, input().split())
n = int(n)
knight = chess_to_cartesian(knight)
coords = set([chess_to_cartesian(i) for i in input().split()])
lu = knight[0] - 2, knight[1] + 1
ld = knight[0] - 2, knight[1] - 1
ur = knight[0] + 1, knight[1] + 2
ul = knight[0] - 1, knight[1] + 2
ru = knight[0] + 2, knight[1] + 1
rd = knight[0] + 2, knight[1] - 1
dr = knight[0] + 1, knight[1] - 2
dl = knight[0] - 1, knight[1] - 2
available = [i for i in [lu, ld, ur, ul, ru, rd, dr, dl] if possible(i)]
print(len(available))
