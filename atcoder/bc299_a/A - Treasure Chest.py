def main():
    _ = int(input())
    s_list = input().split("|")

    for i in list(s_list[1]):
        if i == "*":
            return "in"
    return "out"

if __name__ == '__main__':
    print(main())
