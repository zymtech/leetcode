# -*- coding: utf-8 -*-

import re

def solution(s, a, b):
    if (not s) or (not a) or (not b):
        print "invalid"
        return
    i = s[::-1]
    b1 = isposible(s,a,b)
    b2 = isposible(i,a,b)
    if b1 and b2:
        print "both"
    elif b1 and (not b2):
        print "forward"
    elif (not b1) and b2:
        print "backward"
    else:
        print "invalid"


def isposible(s, a, b):
    rex = '.*' + a + '[a-z]*' + b +'.*'
    if re.match(rex, s):
        return True
    else:
        return False


a = []
while 1:
    s = raw_input()
    if s!='':
        a.append(s)
        if len(a) == 3:
            solution(a[0],a[1],a[2])
            a = []
    else:
        break
