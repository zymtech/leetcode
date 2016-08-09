# -*- coding: utf-8 -*-


class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        if not pattern:
            return False
        pattern = self.pattern(pattern)
        str = self.pattern(str.split(' '))
        for p in pattern:
            if p not in str:
                return False
            else:
                str.remove(p)
        if str:
            return False
        else:
            return True

    def pattern(self, pattern):
        p = {}
        for i,j in enumerate(pattern):
            if j in p:
                p[j].append(i)
            else:
                p[j] = [i]
        l = []
        for _ in p:
            l.append(p[_])
        return l

if __name__=='__main__':
    pattern = 'ab'
    str = 'b a'
    print Solution().pattern(pattern)
    print Solution().pattern(str.split(' '))
    print Solution().wordPattern(pattern, str)