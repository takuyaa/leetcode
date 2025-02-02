#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#
# https://leetcode.com/problems/palindrome-linked-list/description/
#
# algorithms
# Easy (54.73%)
# Likes:    17043
# Dislikes: 916
# Total Accepted:    2.2M
# Total Submissions: 4.1M
# Testcase Example:  '[1,2,2,1]'
#
# Given the head of a singly linked list, return true if it is a palindrome or
# false otherwise.
#
#
# Example 1:
#
#
# Input: head = [1,2,2,1]
# Output: true
#
#
# Example 2:
#
#
# Input: head = [1,2]
# Output: false
#
#
#
# Constraints:
#
#
# The number of nodes in the list is in the range [1, 10^5].
# 0 <= Node.val <= 9
#
#
#
# Follow up: Could you do it in O(n) time and O(1) space?
#

# @lc code=start
# Definition for singly-linked list.
from typing import Self


class ListNode:
    def __init__(self, val: int = 0, next: Self | None = None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        assert head is not None

        array: list[int] = []
        while head is not None:
            array.append(head.val)
            head = head.next

        for i in range(-(len(array) // -2)):
            if array[i] != array[len(array) - 1 - i]:
                return False

        return True


# @lc code=end
