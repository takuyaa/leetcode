#
# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#
# https://leetcode.com/problems/is-subsequence/description/
#
# algorithms
# Easy (48.14%)
# Likes:    9998
# Dislikes: 563
# Total Accepted:    1.8M
# Total Submissions: 3.8M
# Testcase Example:  '"abc"\n"ahbgdc"'
#
# Given two strings s and t, return true if s is a subsequence of t, or false
# otherwise.
#
# A subsequence of a string is a new string that is formed from the original
# string by deleting some (can be none) of the characters without disturbing
# the relative positions of the remaining characters. (i.e., "ace" is a
# subsequence of "abcde" while "aec" is not).
#
#
# Example 1:
# Input: s = "abc", t = "ahbgdc"
# Output: true
# Example 2:
# Input: s = "axc", t = "ahbgdc"
# Output: false
#
#
# Constraints:
#
#
# 0 <= s.length <= 100
# 0 <= t.length <= 10^4
# s and t consist only of lowercase English letters.
#
#
#
# Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k
# >= 10^9, and you want to check one by one to see if t has its subsequence. In
# this scenario, how would you change your code?
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False

        pos = 0
        for c in s:
            p = t.find(c, pos)
            if p >= 0:
                pos = p + 1
            else:
                return False
        return True


# @lc code=end
