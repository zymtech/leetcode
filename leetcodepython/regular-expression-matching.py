# -*- coding: utf-8 -*-


class Solution(object):
    def ismatch(self, s, p):
        if not p:
            return not s
        if len(p)==1 or p[1]!='*':
            if len(s) > 0 and (p[0] == s[0] or p[0] == '.'):
                return self.ismatch(s[1:], p[1:])
            else:
                return False
        else:
            while len(s)>0 and (p[0] == s[0] or p[0] == '.'):
                if self.ismatch(s, p[2:]):
                    return True
                s = s[1:]
                return self.ismatch(s, p[2:])
