#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#
# https://leetcode.com/problems/majority-element/description/
#
# algorithms
# Easy (65.38%)
# Likes:    20169
# Dislikes: 692
# Total Accepted:    3.7M
# Total Submissions: 5.7M
# Testcase Example:  '[3,2,3]'
#
# Given an array nums of size n, return the majority element.
#
# The majority element is the element that appears more than ⌊n / 2⌋ times. You
# may assume that the majority element always exists in the array.
#
#
# Example 1:
# Input: nums = [3,2,3]
# Output: 3
# Example 2:
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2
#
#
# Constraints:
#
#
# n == nums.length
# 1 <= n <= 5 * 10^4
# -10^9 <= nums[i] <= 10^9
#
#
#
# Follow-up: Could you solve the problem in linear time and in O(1) space?
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        counts: dict[int, int] = {}

        for num in nums:
            count = counts.get(num, 0)
            counts[num] = count + 1

        max_count: int = 0
        ret: int = 0
        for key, count in counts.items():
            if count > max_count:
                max_count = count
                ret = key

        return ret


# @lc code=end
