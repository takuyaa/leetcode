#
# @lc app=leetcode id=219 lang=python3
#
# [219] Contains Duplicate II
#
# https://leetcode.com/problems/contains-duplicate-ii/description/
#
# algorithms
# Easy (47.45%)
# Likes:    6516
# Dislikes: 3185
# Total Accepted:    1.2M
# Total Submissions: 2.5M
# Testcase Example:  '[1,2,3,1]\n3'
#
# Given an integer array nums and an integer k, return true if there are two
# distinct indices i and j in the array such that nums[i] == nums[j] and abs(i
# - j) <= k.
#
#
# Example 1:
#
#
# Input: nums = [1,2,3,1], k = 3
# Output: true
#
#
# Example 2:
#
#
# Input: nums = [1,0,1,1], k = 1
# Output: true
#
#
# Example 3:
#
#
# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
# 0 <= k <= 10^5
#
#
#

# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        s: set[int] = set()
        for i in range(min(k + 1, len(nums))):
            if nums[i] in s:
                return True
            s.add(nums[i])
        for i in range(k + 1, len(nums)):
            s.remove(nums[i - k - 1])
            if nums[i] in s:
                return True
            s.add(nums[i])
        return False


# @lc code=end
