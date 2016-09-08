# -*- coding: utf-8 -*-


class Solution(object):
    """
    dp solution
    """
    def jump(self,nums):
        memo = [100000000 for _ in range(len(nums))]
        memo[0] = 0
        for i,j in enumerate(nums):
            if i + j < len(nums) - 1:
                for _ in range(i+1,i+j+1):
                    memo[_] = min(memo[i]+1, memo[_])
            else:
                memo[-1] = min(memo[i] + 1,memo[-1])
        return memo[-1]


class Solution2(object):
    """
    greedy solution
    """
    def jump(self,nums):
        reachable = 0
        curr_reacable = 0
        count = 0
        for i, lenth in enumerate(nums):
            if i > reachable:
                return -1
            if i > curr_reacable:
                curr_reacable = reachable
                count += 1
            reachable = max(reachable, i + lenth)
        return count


if __name__=="__main__":
    nums = []
    print Solution().jump(nums)
    print Solution2().jump(nums)
