#!/usr/bin/env python
# -*- coding: utf-8 -*-


def ispossible(m, n):
    """
    :param m: List[int]
    :param n: List[int]
    :return: Bool
    """
    for i in range(len(n)-1):
        if 2*(m[i+1] - m[i]) <= (n[i+1] - n[i]):
            return False
    return True


def evalation(m,n):
    """
    :param m: List[int]
    :param n: List[int]
    :return: print max possible evalation or IMPOSSIBLE
    """
    if not ispossible(m,n):
        print "IMPOSSIBLE"
        return
    max_evalation = float("-inf")
    for i in range(len(m)-1):
        diff = n[i] + (m[i+1]-m[i])/2+(n[i+1] - n[i])
        if diff > max_evalation:
            max_evalation = diff
            if max_evalation < n[i+1]:
                max_evalation = n[i+1]
    print max_evalation

lastone = 0
m, n = [], []
count = 0
line = 100000000
while 1:
    s = raw_input()
    if s!='':
        if int(count) <= int(line):
            if count == 0:
                line = int(s.split()[1])
                lastone = int(s.split([0]))
                count += 1
            else:
                temp = s.split()
                m.append(int(temp[0]))
                n.append(int(temp[1]))
                count += 1
        else:
            m.append(lastone)
            n.append(n[-1] + m[-1]-m[-2])
            evalation(m,n)
            count = 1
            m,n = [], []
            line = int(s.split()[1])
    else:
        evalation(m,n)
        break

