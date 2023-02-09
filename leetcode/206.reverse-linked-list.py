#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        ans = ListNode(head.val, None)

        while head.next:
            head = head.next
            ans = ListNode(head.val, next=ans)

        return ans

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    ans = ListNode(val=1, next=ListNode(
        val=2, next=ListNode(val=3, next=ListNode(val=4))))
    testcases = [
        (ans, True),

    ]
    for i, (s, ans) in enumerate(testcases):

        print("Test case: ", i)
        print("answer:   ", solution.reverseList(s))
        print("expected: ", ans)
        print("===========================")
