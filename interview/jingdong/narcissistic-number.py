#!/usr/bin/env python
# -*- coding: utf-8 -*-


def narcissistic(m,n):
    count = 0
    for i in range(m,n+1):
        si = str(i)
        sum = 0
        for j in si:
            sum += int(j)**3
        if sum == i:
            print i,
            count += 1
    if not count:
        print 'no'

while 1:
    a = []
    s = raw_input()
    if s != "":
        for x in s.split():
            a.append(int(x))
        narcissistic(a[0], a[1])
    else:
        break

