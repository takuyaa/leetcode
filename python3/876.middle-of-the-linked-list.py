#
# @lc app=leetcode id=876 lang=python3
#
# [876] Middle of the Linked List
#
# https://leetcode.com/problems/middle-of-the-linked-list/description/
#
# algorithms
# Easy (79.80%)
# Likes:    12074
# Dislikes: 386
# Total Accepted:    2.2M
# Total Submissions: 2.8M
# Testcase Example:  '[1,2,3,4,5]'
#
# Given the head of a singly linked list, return the middle node of the linked
# list.
#
# If there are two middle nodes, return the second middle node.
#
#
# Example 1:
#
#
# Input: head = [1,2,3,4,5]
# Output: [3,4,5]
# Explanation: The middle node of the list is node 3.
#
#
# Example 2:
#
#
# Input: head = [1,2,3,4,5,6]
# Output: [4,5,6]
# Explanation: Since the list has two middle nodes with values 3 and 4, we
# return the second one.
#
#
#
# Constraints:
#
#
# The number of nodes in the list is in the range [1, 100].
# 1 <= Node.val <= 100
#
#
#

# @lc code=start
from typing import Optional, Self


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next: Optional[Self] = None) -> None:
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        is_even: bool = True
        current: Optional[ListNode] = head
        middle: Optional[ListNode] = head

        while current is not None:
            is_even = not is_even
            if is_even:
                middle = middle.next if middle is not None else None
            current = current.next

        return middle


# @lc code=end
