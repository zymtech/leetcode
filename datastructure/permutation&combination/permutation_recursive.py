# coding: utf-8


class Permutation(object):
    """
    @param : A list of Integers
    @:return : A list of Permutations
    """
    def permutation(self, nums):
        self.ret = []
        if nums:
            self._permutation(nums, 0)
        return self.ret

    def _permutation(self, nums, start):
        if start == len(nums):
            self.ret.append(nums[:])
        else:
            for i in xrange(start, len(nums)):
                nums[i], nums[start] = nums[start], nums[i]
                self._permutation(nums, start+1)
                nums[i], nums[start] = nums[start], nums[i]

if __name__=='__main__':
    nums = [1,3,4]
    print Permutation().permutation(nums)