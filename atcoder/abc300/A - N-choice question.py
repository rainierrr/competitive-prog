def s_input(): return input()
def s_map(): return


def main():
    n, a, b = map(int, input().split())
    c_list = list(map(int, input().split()))
    return c_list.index(a+b) + 1


if __name__ == '__main__':
    print(main())
