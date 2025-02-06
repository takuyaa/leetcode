#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#
# https://leetcode.com/problems/happy-number/description/
#
# algorithms
# Easy (57.25%)
# Likes:    10859
# Dislikes: 1539
# Total Accepted:    1.7M
# Total Submissions: 3M
# Testcase Example:  '19'
#
# Write an algorithm to determine if a number n is happy.
#
# A happy number is a number defined by the following process:
#
#
# Starting with any positive integer, replace the number by the sum of the
# squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it
# loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
#
#
# Return true if n is a happy number, and false if not.
#
#
# Example 1:
#
#
# Input: n = 19
# Output: true
# Explanation:
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1
#
#
# Example 2:
#
#
# Input: n = 2
# Output: false
#
#
#
# Constraints:
#
#
# 1 <= n <= 2^31 - 1
#
#
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        seen: set[int] = set()

        num: int = n
        while True:
            sum: int = 0
            while num // 10 != 0:
                sum += (num % 10) ** 2
                num //= 10
            sum += num**2

            if sum in seen:
                return False  # avoid infinite loop

            if sum == 1:
                return True

            seen.add(sum)
            num = sum


# @lc code=end
