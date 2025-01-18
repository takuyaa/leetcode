#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#
# https://leetcode.com/problems/single-number/description/
#
# algorithms
# Easy (74.84%)
# Likes:    17080
# Dislikes: 774
# Total Accepted:    3.4M
# Total Submissions: 4.5M
# Testcase Example:  '[2,2,1]'
#
# Given a non-empty array of integers nums, every element appears twice except
# for one. Find that single one.
#
# You must implement a solution with a linear runtime complexity and use only
# constant extra space.
#
#
# Example 1:
#
#
# Input: nums = [2,2,1]
#
# Output: 1
#
#
# Example 2:
#
#
# Input: nums = [4,1,2,1,2]
#
# Output: 4
#
#
# Example 3:
#
#
# Input: nums = [1]
#
# Output: 1
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 3 * 10^4
# -3 * 10^4 <= nums[i] <= 3 * 10^4
# Each element in the array appears twice except for one element which appears
# only once.
#
#
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        res: int = 0
        for num in nums:
            res ^= num
        return res


# @lc code=end
