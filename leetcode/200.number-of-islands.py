#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
from collections import deque
# @lc code=end


def exploreIsland(grid):
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == "1":  # 未発見の島の探索
                return [y, x]  # 未発見の島の座標を返す

    return False  # 未発見の島がない場合


def bfs(grid, start):
    q = deque([start])  # キューの初期化
    grid[start[0]][start[1]] = "*"

    moves = [[-1, 0], [0, -1], [0, 1], [1, 0]]  # 上左右下

    while True:
        y, x = q.pop()  # キューの取り出し
        print(f"現在地：{y}, {x}")
        for move in moves:

            next_y = y + move[0]
            next_x = x + move[1]
            if next_x < 0 or next_x >= len(grid[0]):  # Y軸の境界線の検知
                continue
            if next_y < 0 or next_y >= len(grid):  # X 軸の境界線の検知
                continue
            if grid[next_y][next_x] == "1":
                grid[next_y][next_x] = "*"
                print(f"キュー:{[next_y, next_x]}")
                q.append([next_y, next_x])

        if len(q) == 0:
            break


def numIslands(grid):
    isLandCount = 0

    while True:
        result = exploreIsland(grid)
        print(f"島発見:{result}")
        if not (result):  # 島が発見できない場合
            return isLandCount
        isLandCount += 1
        bfs(grid, result)  # 同一の島を埋める
        for i in grid:
            print(i)


grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]
print(numIslands(grid))
