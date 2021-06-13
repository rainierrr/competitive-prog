money = { 500: 0, 100: 0, 50: 0 }
for key in money.keys():
  money[key] = int(input())
ans_money = int(input())
count = 0
for i in range(money[500]+1):
  if 500*i > ans_money:
    continue
  for ii in range(money[100]+1):
    if 500*i + 100*ii > ans_money:
      continue
    for iii in range(money[50]+1):
      if 500*i + 100*ii + 50*iii == ans_money:
        count = count + 1
print(count)