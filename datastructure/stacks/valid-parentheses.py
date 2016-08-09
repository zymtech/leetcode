# -*- coding: utf-8 -*-


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        left = ['(','{','[']
        right = [')','}',']']
        pair = ['()','{}','[]']
        for char in s:
            if (not stack) or ((stack[-1] in left) == (char in left)) or ((stack[-1] in right) == (char in right)):
                stack.append(char)
            else:
                if (stack[-1] + char) in pair:
                    stack.pop()
                else:
                    return False
        if not stack:
            return True
        else:
            return False

if __name__ == '__main__':
    print Solution().isValid('([])')