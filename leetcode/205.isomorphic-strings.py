#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#


# @lc code=start


class Solution:
    def transformString(self, s: str) -> str:
        index_mapping = {}
        new_str = []

        for i, c in enumerate(s):
            if c not in index_mapping:
                index_mapping[c] = i
            new_str.append(str(index_mapping[c]))

        return " ".join(new_str)

    def isIsomorphic(self, s: str, t: str) -> bool:
        return self.transformString(s) == self.transformString(t)
        # @lc code=end


if __name__ == "__main__":
    solution = Solution()
    testcases = [
        ("egg", "add", True),
        ("bbbaaaba", "aaabbbba", False)
    ]
    for i, (s, t, ans) in enumerate(testcases):

        print("Test case: ", i)
        print("answer:   ", solution.isIsomorphic(s, t))
        print("expected: ", ans)
        print("===========================")
