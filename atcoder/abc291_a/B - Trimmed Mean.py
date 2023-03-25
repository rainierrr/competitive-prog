n = int(input())
x_list = list(map(int, input().split()))


x_list = sorted(x_list)

print(sum(x_list[n:-n])/len(x_list[n:-n]))
