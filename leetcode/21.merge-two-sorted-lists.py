#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.


# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:

    def mergeTwoLists(self, list1, list2):
        first_node = tmp_node = ListNode()

        while list1 is not None and list2 is not None:
            val = 0
            if list1.val <= list2.val:
                val = list1.val
                list1 = list1.next
            else:
                val = list2.val
                list2 = list2.next

            tmp_node2 = ListNode(val)
            tmp_node.next = tmp_node2
            tmp_node = tmp_node2

        if list1 is None:
            tmp_node.next = list2
        else:
            tmp_node.next = list1

        return first_node.next

# @lc code=end
