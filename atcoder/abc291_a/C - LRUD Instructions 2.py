n = int(input())
S = input()


x = 0
y = 0
coordinate = {"0x0": True}
ans = ""
for s in S:
    if s == "R":
        x += 1
    elif s == "L":
        x -= 1
    elif s == "U":
        y += 1
    else:
        y -= 1
    key = str(x) + "x" + str(y)
    v = coordinate.get(key)

    if v is not None:
        ans = "Yes"
        break
    coordinate[key] = True
if ans:
    print(ans)
else:
    print("No")
