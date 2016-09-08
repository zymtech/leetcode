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
    class Solution(object):
        """
        dp solution
        """
        def canJump(self, nums):
            """
            :type nums: List[int]
            :rtype: bool
            """
            memo = [-1 for _ in range(len(nums))]
            memo[0] = 1
            for i, j in enumerate(nums):
                if memo[i] == 1:
                    if i + j < len(nums) - 1:
                        for _ in range(i + 1, i + j + 1):
                            memo[_] = 1
                    else:
                        return True
            return False

if __name__ == "__main__":
    num1 = [2,3,1,1,4]
    nums2 = [3,2,1,0,4]
    solution = Solution()
    print solution.canJump(num1)
    print solution.canJump(nums2)
    print Solution2().canJump(num1)
    print Solution2().canJump(nums2)