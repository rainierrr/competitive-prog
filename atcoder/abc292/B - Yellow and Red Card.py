N, Q = input().split()
N = int(N)
Q = int(Q)

events = [tuple(map(int, input().split())) for _ in range(Q)]
violation_dict = {}
for event in events:
    event_kind = event[0]
    player_num = event[1]

    if event_kind == 1:
        yellow_num = violation_dict.get(player_num)
        if yellow_num is None:
            violation_dict[player_num] = 1
        elif yellow_num == 1:
            violation_dict[player_num] = False
    elif event_kind == 2:
        violation_dict[player_num] = False
    else:
        relust = violation_dict.get(player_num)
        if relust is None or relust == 1:
            print("No")
        else:
            print("Yes")
