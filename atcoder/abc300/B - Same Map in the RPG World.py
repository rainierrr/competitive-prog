from collections import deque
import copy


def counter(mize):
    count = [0] * len(mize)
    for i in range(len(mize)):
        for j in range(len(mize[i])):
            if mize[i][j] == '#':
                count[i] = count[i] + 1
    return count


def checker(a_mize, b_mize):
    for hh in range(h-1):
        for jj in range(w-1):
            if deque(a_mize[hh]) == b_mize[hh]:
                break
            if jj == w-2:
                return False
            b_mize[hh].append(b_mize[hh].popleft())
    return True


h, w = 0, 0


def main():
    h, w = map(int, input().split())
    a_mize = [list(input()) for _ in range(h)]
    b_mize = deque([deque(list(input())) for _ in range(h)])

    count_a = deque(counter(a_mize))
    count_b = deque(counter(b_mize))

    for i in range(0, h-1):
        if count_a == count_b and checker(a_mize, copy.deepcopy(b_mize)):
            return "Yes"
        if i == h-2:
            return "No"

        count_b.append(count_b.popleft())
        b_mize.append(b_mize.popleft())


if __name__ == '__main__':
    print(main())
