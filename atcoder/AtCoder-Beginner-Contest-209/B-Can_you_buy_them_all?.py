product_num, money = list(map(int, input().split()))
products = list(map(int, input().split()))
if money - (sum(products) - (len(products) / 2)) >= 0:
  print("Yes")
else:
  print("No")