#
# @lc app=leetcode id=1480 lang=python3
#
# [1480] Running Sum of 1d Array
#
# https://leetcode.com/problems/running-sum-of-1d-array/description/
#
# algorithms
# Easy (86.91%)
# Likes:    8045
# Dislikes: 354
# Total Accepted:    2M
# Total Submissions: 2.3M
# Testcase Example:  '[1,2,3,4]'
#
# Given an array nums. We define a running sum of an array as runningSum[i] =
# sum(nums[0]…nums[i]).
#
# Return the running sum of nums.
#
#
# Example 1:
#
#
# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
#
# Example 2:
#
#
# Input: nums = [1,1,1,1,1]
# Output: [1,2,3,4,5]
# Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1,
# 1+1+1+1+1].
#
# Example 3:
#
#
# Input: nums = [3,1,2,10,1]
# Output: [3,4,6,16,17]
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 1000
# -10^6 <= nums[i] <= 10^6
#
#
#

# @lc code=start
class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        acc: int = 0
        ret: list[int] = [0] * len(nums)

        for i in range(len(nums)):
            acc += nums[i]
            ret[i] = acc

        return ret


# @lc code=end
