n = int(input())
i = 10 ** (n - 1)
count = 0
max_num = (10 ** n) - 1
while i <= max_num:
    list_num = list(map(int, str(1234)))
    len_count = 0
    len_num = len(list_num)
    for i in range(len_num - 1):
        if abs(list_num[i] - list_num[i + 1]) <= 1:
            len_count = len_count + 1
            if len_count == (len_num - 1):
                print(i)
        else:
            break
    i = i + 1
