n = int(input())
cars_places = dict()
ans = []
for i in range(n):
    cmd = input().split()
    if len(cmd) == 5:
        # drove into place
        cars_places[cmd[0]] = cmd[4]
    elif cmd[1] == "drove":
        # drove out
        del cars_places[cmd[0]]
    else:
        # look at
        res = cars_places.get(cmd[2], None)
        ans.append('Not here' if res is None else res)

print(*ans, sep='\n')
