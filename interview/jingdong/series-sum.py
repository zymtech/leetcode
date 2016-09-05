#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math


def series_sum(n,m):
    if m<0:
        return
    if m == 1:
        print n
        return
    if m == 0:
        print 0
        return
    sum = n
    n = float(n)
    for i in range(m-1):
        n = math.sqrt(n)
        sum += n
    print round(sum,2)

while 1:
    a = []
    s = raw_input()
    if s!='':
        for x in s.split():
            a.append(int(x))
        series_sum(a[0], a[1])
    else:
        break

