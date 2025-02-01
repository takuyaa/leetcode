#
# @lc app=leetcode id=643 lang=python3
#
# [643] Maximum Average Subarray I
#
# https://leetcode.com/problems/maximum-average-subarray-i/description/
#
# algorithms
# Easy (44.30%)
# Likes:    3733
# Dislikes: 346
# Total Accepted:    699.3K
# Total Submissions: 1.6M
# Testcase Example:  '[1,12,-5,-6,50,3]\n4'
#
# You are given an integer array nums consisting of n elements, and an integer
# k.
#
# Find a contiguous subarray whose length is equal to k that has the maximum
# average value and return this value. Any answer with a calculation error less
# than 10^-5 will be accepted.
#
#
# Example 1:
#
#
# Input: nums = [1,12,-5,-6,50,3], k = 4
# Output: 12.75000
# Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
#
#
# Example 2:
#
#
# Input: nums = [5], k = 1
# Output: 5.00000
#
#
#
# Constraints:
#
#
# n == nums.length
# 1 <= k <= n <= 10^5
# -10^4 <= nums[i] <= 10^4
#
#
#

# @lc code=start
class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        if len(nums) < k:
            return sum(nums) / len(nums)

        window: int = sum(nums[0:k])
        max_window: int = window
        for i in range(1, len(nums) - (k - 1)):
            window -= nums[i - 1]
            window += nums[i + (k - 1)]
            if window > max_window:
                max_window = window
        return max_window / k


# @lc code=end
