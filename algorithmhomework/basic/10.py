# -*- coding: utf-8 -*-

def sum(n, s):
    n and sum(n-1, s)
    s += temp
    return s

if __name__=='__main__':
    n = raw_input()
    print sum(int(n),1)-1

