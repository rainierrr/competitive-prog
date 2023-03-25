#s = input()

S = "xxxxxxXxxx"

for i, s in enumerate(S):
    if 'A' <= s and s <= 'Z':
        print(i+1)
        break
