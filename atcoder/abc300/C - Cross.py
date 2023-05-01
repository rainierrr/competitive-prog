
def find_cross(i, j, h, w):
    n = 0

    while True:
        print(i, j, n)
        if i-n < 0 or j-n < 0 or i+n >= h-1 or j+n >= w-1:
            break
        if grid[i-n][j-n] == '#' and grid[i][j+n] == '#' and grid[i+n][j] == '#' and grid[i+n][j+n] == '#':
            n = n + 1

    return n


h, w = 0, 0
grid = []


def main():
    h, w = map(int, input().split())
    grid = [list(input()) for _ in range(h)]
    ans = [0] * min(h, w)
    if h < 3 or w < 3:
        return ans
    for i in range(h):
        print(grid[i])
    for i in range(1, h-1):
        for j in range(1, w-1):
            if grid[i][j] == '#':
                n = find_cross(i, j, h, w)
                if n != 0:
                    ans[n] = ans[n] + 1

    return ans


if __name__ == '__main__':

    print(main())
