#
# @lc app=leetcode id=303 lang=python3
#
# [303] Range Sum Query - Immutable
#
# https://leetcode.com/problems/range-sum-query-immutable/description/
#
# algorithms
# Easy (66.36%)
# Likes:    3389
# Dislikes: 1945
# Total Accepted:    642K
# Total Submissions: 962.3K
# Testcase Example:  '["NumArray","sumRange","sumRange","sumRange"]\n[[[-2,0,3,-5,2,-1]],[0,2],[2,5],[0,5]]'
#
# Given an integer array nums, handle multiple queries of the following
# type:
#
#
# Calculate the sum of the elements of nums between indices left and right
# inclusive where left <= right.
#
#
# Implement the NumArray class:
#
#
# NumArray(int[] nums) Initializes the object with the integer array nums.
# int sumRange(int left, int right) Returns the sum of the elements of nums
# between indices left and right inclusive (i.e. nums[left] + nums[left + 1] +
# ... + nums[right]).
#
#
#
# Example 1:
#
#
# Input
# ["NumArray", "sumRange", "sumRange", "sumRange"]
# [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
# Output
# [null, 1, -1, -3]
#
# Explanation
# NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
# numArray.sumRange(0, 2); // return (-2) + 0 + 3 = 1
# numArray.sumRange(2, 5); // return 3 + (-5) + 2 + (-1) = -1
# numArray.sumRange(0, 5); // return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^4
# -10^5 <= nums[i] <= 10^5
# 0 <= left <= right < nums.length
# At most 10^4 calls will be made to sumRange.
#
#
#

# @lc code=start
class NumArray:
    def __init__(self, nums: list[int]) -> None:
        if len(nums) == 0:
            self.tree = []
            return

        max_level = (len(nums) - 1).bit_length() + 1
        N: int = 2**max_level

        self.N = N
        self.tree: list[int] = [0] * N

        # initialize leaf nodes
        for i in range(0, len(nums)):
            self.tree[(N >> 1) + i] = nums[i]

        # initialize intermediate nodes and root node
        for i in reversed(range(1, N >> 1)):
            self.tree[i] = self.tree[i << 1] + self.tree[(i << 1) + 1]

    def _query(self, a: int, b: int, k: int, l: int, r: int) -> int:
        if r <= a or b <= l:
            return 0
        if a <= l and r <= b:
            return self.tree[k]
        else:
            vl = self._query(a=a, b=b, k=(k << 1), l=l, r=((l + r) >> 1))
            vr = self._query(a=a, b=b, k=((k << 1) + 1), l=((l + r) >> 1), r=r)
            return vl + vr

    def sumRange(self, left: int, right: int) -> int:
        if left == right:
            return self.tree[(self.N >> 1) + left]

        return self._query(a=left, b=(right + 1), k=1, l=0, r=(self.N >> 1))


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
# @lc code=end
