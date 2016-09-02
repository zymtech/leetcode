# -*- coding: utf-8 -*-


class Solution(object):
    def subsets(self, nums):
        """
        leetcode 78
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return self.recursive([], nums)

    def recursive(self,cur,nums):
        if not nums:
            return [cur]
        return self.recursive(cur, nums[1:]) + self.recursive(cur + [nums[0]],\
                                                              nums[1:])
if __name__ == "__main__":
    nums = [1,3,4]
    print Solution().subsets(nums)
