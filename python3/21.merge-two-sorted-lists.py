#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#
# https://leetcode.com/problems/merge-two-sorted-lists/description/
#
# algorithms
# Easy (65.87%)
# Likes:    22917
# Dislikes: 2236
# Total Accepted:    5M
# Total Submissions: 7.5M
# Testcase Example:  '[1,2,4]\n[1,3,4]'
#
# You are given the heads of two sorted linked lists list1 and list2.
#
# Merge the two lists into one sorted list. The list should be made by splicing
# together the nodes of the first two lists.
#
# Return the head of the merged linked list.
#
#
# Example 1:
#
#
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
#
#
# Example 2:
#
#
# Input: list1 = [], list2 = []
# Output: []
#
#
# Example 3:
#
#
# Input: list1 = [], list2 = [0]
# Output: [0]
#
#
#
# Constraints:
#
#
# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# Both list1 and list2 are sorted in non-decreasing order.
#
#
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: ListNode | None, list2: ListNode | None
    ) -> ListNode | None:
        n1: ListNode | None = list1
        n2: ListNode | None = list2

        curr: ListNode = ListNode()  # dummy node
        head: ListNode = curr

        while n1 is not None and n2 is not None:
            if n1.val <= n2.val:
                curr.next = ListNode(val=n1.val)
                curr = curr.next
                n1 = n1.next
            else:
                curr.next = ListNode(val=n2.val)
                curr = curr.next
                n2 = n2.next

        while n1 is not None:
            curr.next = ListNode(val=n1.val)
            curr = curr.next
            n1 = n1.next

        while n2 is not None:
            curr.next = ListNode(val=n2.val)
            curr = curr.next
            n2 = n2.next

        return head.next


# @lc code=end
