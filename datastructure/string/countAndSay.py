# -*- coding: utf-8 -*-


class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n==1:
            return '1'
        else:
            ret = self.generate(self.countAndSay(n-1))
        return ret

    def generate(self, n):
        count = 1
        r = ''
        for i in range(0,len(n)-1):
            if n[i] == n[i+1]:
                count += 1
            else:
                r += str(count) + n[i]
                count = 1
        r += str(count) + n[-1]
        return r

if __name__ == '__main__':
    print Solution().countAndSay(5)