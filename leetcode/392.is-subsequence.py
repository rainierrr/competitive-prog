#
# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#
import itertools

# @lc code=start


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s = list(s)
        t = list(t)
        if len(s) == 0:
            return True

        for tt in t:
            if s[0] == tt:
                print(s[0], tt)
                del s[0]
            if len(s) == 0:
                return True

        return False
        # @lc code=end


if __name__ == "__main__":
    solution = Solution()
    testcases = [
        ("abc", "ahbgdc", True),
        ("axc", "ahbgdc", False),
        ("acb", "ahbgdc", False),
        ("", "ahbgdc", True)
    ]
    for i, (s, t, ans) in enumerate(testcases):

        print("Test case: ", i)
        print("answer:   ", solution.isSubsequence(s, t))
        print("expected: ", ans)
        print("===========================")
