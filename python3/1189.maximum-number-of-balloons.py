#
# @lc app=leetcode id=1189 lang=python3
#
# [1189] Maximum Number of Balloons
#
# https://leetcode.com/problems/maximum-number-of-balloons/description/
#
# algorithms
# Easy (59.72%)
# Likes:    1772
# Dislikes: 111
# Total Accepted:    251.2K
# Total Submissions: 420.7K
# Testcase Example:  '"nlaebolko"'
#
# Given a string text, you want to use the characters of text to form as many
# instances of the word "balloon" as possible.
#
# You can use each character in text at most once. Return the maximum number of
# instances that can be formed.
#
#
# Example 1:
#
#
#
#
# Input: text = "nlaebolko"
# Output: 1
#
#
# Example 2:
#
#
#
#
# Input: text = "loonbalxballpoon"
# Output: 2
#
#
# Example 3:
#
#
# Input: text = "leetcode"
# Output: 0
#
#
#
# Constraints:
#
#
# 1 <= text.length <= 10^4
# text consists of lower case English letters only.
#
#
#
# Note: This question is the same as  2287: Rearrange Characters to Make Target
# String.
#
#

# @lc code=start
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        b_count: int = 0
        a_count: int = 0
        l_count: int = 0
        o_count: int = 0
        n_count: int = 0
        for c in text:
            if c == "b":
                b_count += 1
            elif c == "a":
                a_count += 1
            elif c == "l":
                l_count += 1
            elif c == "o":
                o_count += 1
            elif c == "n":
                n_count += 1
        return min(b_count, a_count, l_count // 2, o_count // 2, n_count)


# @lc code=end
