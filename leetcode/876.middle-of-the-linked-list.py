#
# @lc app=leetcode id=876 lang=python3
#
# [876] Middle of the Linked List
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional
import copy


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head2 = copy.deepcopy(head)
        length = 0
        while head is not None:
            length += 1
            head = head.next

        count = length // 2
        for i in range(count):
            head2 = head2.next

        return head2
        # @lc code=end
