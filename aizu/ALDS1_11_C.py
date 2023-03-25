from collections import deque

n = int(input())
num_list = [list(map(int, input().split())) for _ in range(n)]
dist = [-1 for _ in range(n+1)]
dist[1] = 0

q = deque([1])
while len(q) != 0:
    idx = q.popleft()
    if num_list[idx-1][1] == 0:
        continue
    nexts = num_list[idx-1][2:]
    for i in nexts:
        if dist[i] > -1:
            continue
        dist[i] = dist[idx] + 1
        q.append(i)

for idx, i in enumerate(dist[1:]):
    if idx != 0 and i == 0:
        i = -1

    print(idx+1, i)
