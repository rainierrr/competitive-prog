#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, num, target):
        d = dict()
        for index, number in enumerate(num):
            try:
                return ((d[target-number]+1, index+1))
            except:
                d[number] = index

# @lc code=end

