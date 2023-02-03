#
# @lc app=leetcode id=724 lang=python3
#
# [724] Find Pivot Index
#

# @lc code=start
from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        right_sum = 0
        left_sum = sum(nums)
        for i in range(0, len(nums)):
            left_sum -= nums[i]
            if right_sum == left_sum:
                return i
            right_sum += nums[i]

        return -1
        # @lc code=end


if __name__ == "__main__":
    s = Solution()
    testcases = [
        ([1, 7, 3, 6, 5, 6], 3),
        ([2, 1, -1], 0)
    ]
    for i, (inp, ans) in enumerate(testcases):
        print("Test case: ", i)
        print("answer:   ", s.pivotIndex(inp))
        print("expected: ", ans)
