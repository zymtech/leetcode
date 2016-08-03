import itertools
from collections import Counter

def solution(a):
    l = []
    b=''
    for i,j in enumerate(a):
        if j in ['n','t','e','s']:
            b += j
    iter = itertools.permutations(b,4)
    l.append(list(iter))
    tup = ('n','t','e','s')
    print l[0]
    return Counter(l[0])[tup]

if __name__=='__main__':
    print solution("nnttes")
