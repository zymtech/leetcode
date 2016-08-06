# -*- coding: utf-8 -*-


class Solution(object):
    def permute(self, nums):
        """
        :param nums: list[int]
        :return: list[list]
        """
        self.ret = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                nums[i], nums[j] = nums[j], nums[i]
                # append后面是nums[:],要不然保存的是nums的引用
                self.ret.append(nums[:])
                nums[i], nums[j] = nums[j], nums[i]
        return self.ret

if __name__ == '__main__':
    nums = [1,2,3]
    print Solution().permute(nums)

