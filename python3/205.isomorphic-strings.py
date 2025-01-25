#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#
# https://leetcode.com/problems/isomorphic-strings/description/
#
# algorithms
# Easy (46.10%)
# Likes:    9462
# Dislikes: 2165
# Total Accepted:    1.6M
# Total Submissions: 3.5M
# Testcase Example:  '"egg"\n"add"'
#
# Given two strings s and t, determine if they are isomorphic.
#
# Two strings s and t are isomorphic if the characters in s can be replaced to
# get t.
#
# All occurrences of a character must be replaced with another character while
# preserving the order of characters. No two characters may map to the same
# character, but a character may map to itself.
#
#
# Example 1:
#
#
# Input: s = "egg", t = "add"
#
# Output: true
#
# Explanation:
#
# The strings s and t can be made identical by:
#
#
# Mapping 'e' to 'a'.
# Mapping 'g' to 'd'.
#
#
#
# Example 2:
#
#
# Input: s = "foo", t = "bar"
#
# Output: false
#
# Explanation:
#
# The strings s and t can not be made identical as 'o' needs to be mapped to
# both 'a' and 'r'.
#
#
# Example 3:
#
#
# Input: s = "paper", t = "title"
#
# Output: true
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 5 * 10^4
# t.length == s.length
# s and t consist of any valid ascii character.
#
#
#

# @lc code=start
class Solution:
    def _types(self, s: str) -> list[int]:
        types: list[int] = [0] * len(s)

        type_id: int = 0
        types_map: dict[str, int] = {}
        for i in range(len(s)):
            c: str = s[i]
            got: int | None = types_map.get(c)
            if got is None:
                types_map[c] = type_id
                types[i] = type_id
                type_id += 1
            else:
                types[i] = got
        return types

    def isIsomorphic(self, s: str, t: str) -> bool:
        assert len(s) == len(t)
        return self._types(s) == self._types(t)


# @lc code=end
