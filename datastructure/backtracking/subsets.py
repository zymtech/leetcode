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


class NoneRecurSolution(object):
    def subsets(self, nums):
        result = [[]]
        #nums.sort()
        for i in xrange(len(nums)):
            size = len(result)
            for j in range(size):
                result.append(list(result[j]))
                result[-1].append(nums[i])
        return result


if __name__ == "__main__":
    nums = [1,4,3]
    print Solution().subsets(nums)
    print NoneRecurSolution().subsets(nums)
