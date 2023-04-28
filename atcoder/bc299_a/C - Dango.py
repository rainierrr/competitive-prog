def main():
    N = int(input())
    s_list = list(input())
    count = 0
    max_count = 0

    for s in s_list:
        if s == "o":
            count += 1
        else:
            if count > max_count:
                max_count = count
            count = 0

    if count > max_count and N > count:
        max_count = count

    if max_count == 0:
        return -1
    return max_count


if __name__ == '__main__':
    print(main())
