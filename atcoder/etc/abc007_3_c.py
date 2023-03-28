from collections import deque


def bfs():
    q = deque([start])  # キュー初期化
    dist[start[0]][start[1]] = 0  # 距離カウントの初期化

    while True:
        y, x = q.pop()
        # print(f"現在地: {y},{x}")

        candidate = []

        if x > 0:
            candidate.append([y, x-1])  # 左
        if y > 0:
            candidate.append([y-1, x])  # 上

        if x < rc[1] - 1:
            candidate.append([y, x+1])  # 右
        if y < rc[0] - 1:
            candidate.append([y+1, x])  # 下

        # print(f"候補：{candidate}")
        for p in candidate:

            if maze[p[0]][p[1]] == '.' and (dist[p[0]][p[1]] == 0 or dist[p[0]][p[1]] > dist[y][x] + 1):
                dist[p[0]][p[1]] = dist[y][x] + 1
                q.append(p)

        if len(q) == 0:
            return


rc, start, end = [list(map(int, input().split())) for _ in range(3)]
maze = [list(input()) for _ in range(rc[0])]
dist = [[0 for _ in range(rc[1])] for _ in range(rc[0])]
start = [start[0] - 1, start[1] - 1]
end = [end[0] - 1, end[1] - 1]
# print(rc, start, end)
# for i in maze:
#     print(i)


bfs()
print(dist[end[0]][end[1]])
# for i in dist:
#     print(i)
# print(f"答え：{dist[end[0]][end[1]]}")
