N = int(input())
comb = {}
for i in range(1, N+1):
    for j in range(i, N+1):
        tmp = i * j
        if tmp < N:
            num = comb.get(tmp)
            count = 1 if i == j else 2
            if num is None:
                comb[tmp] = count
            else:
                comb[tmp] += count
        else:
            break

sum = 0

for i in range(1, N+1):
    if comb.get(i) is not None and comb.get(N-i) is not None:
        sum += comb.get(i) * comb.get(N-i)

print(sum)
