# -*- coding: utf-8 -*-


class Solution(object):
    """
    dynamic programming solution
    """
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        f = [0 for i in range(len(nums)+1)]
        f[0] = 0
        f[1] = nums[0]
        for i in xrange(2,len(nums)+1):
            f[i] = max(nums[i-1] + f[i-2], f[i-1])
        return f[-1]


class ForceSearch_Solution(object):
    """Force Search Solution"""
    def rob(self, nums):
        index = len(nums) - 1
        return self.search(index, nums)

    def search(self, index, nums):
        if index < 0:
            return 0
        return max(nums[index] + self.search(index-2, nums), self.search(index-1, nums))

if __name__=='__main__':
    nums = [1,3,4]
    print Solution().rob(nums)
    print ForceSearch_Solution().rob(nums)