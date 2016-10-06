import sys

import math


def translate(num,base_num):
    if num < base_num:
        return str(num)
    else:
        n = int(math.log10(num)/math.log10(base_num))+1
        trans_num = ''
        for i in range(n):
            num_add = num/(base_num**(n-i-1))
            trans_num = trans_num + str(num_add)
            num = num - num_add*(base_num**(n-i-1))
        return trans_num

while 1:
    line = sys.stdin.readline()
    if line:
        a = line.split()
        if len(a) == 2:
            print translate(int(a[0]), int(a[1]))
    else:
        break