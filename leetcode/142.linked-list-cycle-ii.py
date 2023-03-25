#
# @lc app=leetcode id=142 lang=python3
#
# [142] Linked List Cycle II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast: break
        else:
            return None

        while head != slow:
            head = head.next
            slow = slow.next
        return head
# class Solution:
#     def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if head is None or head.next is None:
#             return None

#         node_set = set()

#         while head is not None:
#             node_id = id(head)
#             if node_id in node_set:
#                 return head
#             else:
#                 node_set.add(node_id)

#             head = head.next

#         return None

# @lc code=end
