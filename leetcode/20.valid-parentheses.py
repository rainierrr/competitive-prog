#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        s_list = list(s)

        if len(s_list) == 0 or len(s_list) == 1:
            return False

        stack.append(s_list[0])
        print(stack)

        for i in s_list[1:]:
            if len(stack) != 0:
                if (i == ")" and stack[-1] == "(") or \
                   (i == "}" and stack[-1] == "{") or \
                   (i == "]" and stack[-1] == "["):
                    del stack[-1]
                    continue

            stack.append(i)

        print(stack)
        if len(stack) == 0:
            return True

        return False

# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    testcases = [
        ("({[)", True),

    ]
    for i, (s, ans) in enumerate(testcases):

        print("Test case: ", i)
        print("answer:   ", solution.isValid(s))
        print("expected: ", ans)
        print("===========================")
