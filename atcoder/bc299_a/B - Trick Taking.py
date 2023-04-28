def main():
    N, T = map(int, input().split())
    c_list = list(map(int, input().split()))
    r_list = list(map(int, input().split()))

    max_num = 0
    max_idx = 0

    if T in c_list:
        for i in range(N):
            if c_list[i] == T and r_list[i] > max_num:
                max_num = r_list[i]
                max_idx = i
        return max_idx+1

    max_num = 0
    max_idx = 0

    for i in range(N):
        if c_list[i] == c_list[0] and r_list[i] > max_num:
            max_num = r_list[i]
            max_idx = i
    return max_idx+1


if __name__ == '__main__':
    print(main())
