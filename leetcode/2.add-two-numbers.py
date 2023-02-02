#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ans = []
        tmp_num = 0
        while(1):
            if l1 == None and l2 == None:
                if tmp_num != 0:
                    ans.append(tmp_num)
                break
            elif l1 == None:
                sum_num = l2.val + tmp_num
                l2 = l2.next
                tmp_num = 0
            elif l2 == None:
                sum_num = l1.val + tmp_num
                l1 = l1.next
            else:
                sum_num = l1.val + l2.val + tmp_num
                l1 = l1.next
                l2 = l2.next

            sum_list = list(map(int, list(str(sum_num))))
            if len(sum_list) == 2:
                ListNode()
                ans.append(sum_list[1])
                tmp_num = sum_list[0]
            else:
                ans.append(sum_list[0])
                tmp_num = 0

        link = None
        for i in reversed(ans):
            link = ListNode(i, link)

        return link
# @lc code=end

