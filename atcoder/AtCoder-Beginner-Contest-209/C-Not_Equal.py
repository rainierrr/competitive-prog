length = int(input())
nums = list(map(int, input().split()))

def dfs(nums):
  if len(nums) == length:
      print(nums)
      return
  for v in range(length):
    nums.append(v)
    dfs(nums)
    nums.pop()


count = 0
dfs([])
print(count)