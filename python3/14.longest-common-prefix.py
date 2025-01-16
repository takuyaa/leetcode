#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#
# https://leetcode.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (44.44%)
# Likes:    18551
# Dislikes: 4657
# Total Accepted:    4.1M
# Total Submissions: 9.2M
# Testcase Example:  '["flower","flow","flight"]'
#
# Write a function to find the longest common prefix string amongst an array of
# strings.
#
# If there is no common prefix, return an empty string "".
#
#
# Example 1:
#
#
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
#
#
# Example 2:
#
#
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
#
#
#
# Constraints:
#
#
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters if it is non-empty.
#
#
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        lcp = strs[0]

        if len(strs) == 1:
            return strs[0]

        min_length = min([len(str) for str in strs])
        for pos in range(min_length):
            for str in strs[1:]:
                if str[pos] != lcp[pos]:
                    return lcp[:pos]

        return lcp[:min_length]


# @lc code=end
