n = int(input())
a = list(map(int, input().split()))
count = 0
while all([ a[i]%2 == 0 for i in range(n)]):
  for i in range(n):
    a[i] = a[i]>>1
  count = count + 1
print(count)