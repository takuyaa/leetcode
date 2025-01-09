#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#
# https://leetcode.com/problems/ransom-note/description/
#
# algorithms
# Easy (63.40%)
# Likes:    5198
# Dislikes: 516
# Total Accepted:    1.4M
# Total Submissions: 2.3M
# Testcase Example:  '"a"\n"b"'
#
# Given two strings ransomNote and magazine, return true if ransomNote can be
# constructed by using the letters from magazine and false otherwise.
#
# Each letter in magazine can only be used once in ransomNote.
#
#
# Example 1:
# Input: ransomNote = "a", magazine = "b"
# Output: false
# Example 2:
# Input: ransomNote = "aa", magazine = "ab"
# Output: false
# Example 3:
# Input: ransomNote = "aa", magazine = "aab"
# Output: true
#
#
# Constraints:
#
#
# 1 <= ransomNote.length, magazine.length <= 10^5
# ransomNote and magazine consist of lowercase English letters.
#
#
#

# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dic: dict[str, int] = dict()
        for c in magazine:
            dic[c] = dic.get(c, 0) + 1
        for c in ransomNote:
            i = dic.get(c, 0)
            if i <= 0:
                return False
            if i == 1:
                del dic[c]
            else:
                dic[c] = i - 1
        return True


# @lc code=end
