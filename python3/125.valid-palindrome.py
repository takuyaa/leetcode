#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#
# https://leetcode.com/problems/valid-palindrome/description/
#
# algorithms
# Easy (49.56%)
# Likes:    9902
# Dislikes: 8480
# Total Accepted:    3.8M
# Total Submissions: 7.6M
# Testcase Example:  '"A man, a plan, a canal: Panama"'
#
# A phrase is a palindrome if, after converting all uppercase letters into
# lowercase letters and removing all non-alphanumeric characters, it reads the
# same forward and backward. Alphanumeric characters include letters and
# numbers.
#
# Given a string s, return true if it is a palindrome, or false otherwise.
#
#
# Example 1:
#
#
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
#
#
# Example 2:
#
#
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
#
#
# Example 3:
#
#
# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric
# characters.
# Since an empty string reads the same forward and backward, it is a
# palindrome.
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 2 * 10^5
# s consists only of printable ASCII characters.
#
#
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        pos_forward: int = 0
        pos_backward: int = len(s) - 1

        while pos_forward <= pos_backward:
            if not s[pos_forward].isalpha() and not s[pos_forward].isdigit():
                pos_forward += 1
                continue
            if not s[pos_backward].isalnum() and not s[pos_backward].isdigit():
                pos_backward -= 1
                continue
            if s[pos_forward].lower() != s[pos_backward].lower():
                return False
            pos_forward += 1
            pos_backward -= 1

        return True


# @lc code=end
