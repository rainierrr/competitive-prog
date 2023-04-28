def main():
    N = int(input())
    max_range = N - 1

    if N - 1 > 22:
        max_range = 22

    for i in range(2, max_range):
        print(f"? {i}")
        s = int(input())
        count += 1
        if s == 1:
            return i

    return N


if __name__ == '__main__':
    p_1 = main()
    print(f"! {p_1 - 1}")
