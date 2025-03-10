#
# @lc app=leetcode id=1512 lang=python3
#
# [1512] Number of Good Pairs
#
# https://leetcode.com/problems/number-of-good-pairs/description/
#
# algorithms
# Easy (89.39%)
# Likes:    5568
# Dislikes: 271
# Total Accepted:    881.5K
# Total Submissions: 985.8K
# Testcase Example:  '[1,2,3,1,1,3]'
#
# Given an array of integers nums, return the number of good pairs.
#
# A pair (i, j) is called good if nums[i] == nums[j] and i < j.
#
#
# Example 1:
#
#
# Input: nums = [1,2,3,1,1,3]
# Output: 4
# Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
#
#
# Example 2:
#
#
# Input: nums = [1,1,1,1]
# Output: 6
# Explanation: Each pair in the array are good.
#
#
# Example 3:
#
#
# Input: nums = [1,2,3]
# Output: 0
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 100
# 1 <= nums[i] <= 100
#
#
#

# @lc code=start
class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        hm: dict[int, int] = {}
        for num in nums:
            count: int = hm.get(num, 0)
            hm[num] = count + 1

        pairs: int = 0
        for _, count in hm.items():
            if count < 2:
                continue
            # calcurate nC2
            pairs += count * (count - 1) // 2
        return pairs


# @lc code=end
