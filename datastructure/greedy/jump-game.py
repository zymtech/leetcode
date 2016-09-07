class Solution:
    # greedy solution
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        reachable = 0
        for i, length in enumerate(A):
            if i > reachable:
                break
            reachable = max(reachable, i + length)
        return reachable >= len(A) - 1


class Solution2:
    # dynamic programming solution
    def __init__(self):
        self.memo = []

    def canJump(self, nums):
        """
        dp solution
        :param nums: List[int]
        :return: bool
        """
        # memo: -1 stands for UNKNOWN
        #        0 stands for unreachable
        #        1 stands for reachable
        self.memo = [-1 for _ in range(len(nums))]
        self.memo[-1] = 1
        return self.canJumpFromPosition(0, nums)

    def canJumpFromPosition(self, position, nums):
        if self.memo[position] != -1:
            if self.memo[position] == 1:
                return True
            elif self.memo[position] == 0:
                return False
        furthestjump = min(position + nums[position], len(nums)-1)
        for i in range(position + 1, furthestjump + 1):
            if self.canJumpFromPosition(i, nums):
                self.memo[i] = 1
                return True
        self.memo[position] = 0
        return False

if __name__ == "__main__":
    num1 = [2,3,1,1,4]
    nums2 = [3,2,1,0,4]
    solution = Solution()
    print solution.canJump(num1)
    print solution.canJump(nums2)
    print Solution2().canJump(num1)
    print Solution2().canJump(nums2)