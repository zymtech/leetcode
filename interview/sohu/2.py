def solution(m,n):
    """

    :param m: string
    :param n: string
    :return: print str
    """
    pick = len(m) - n
    ret = []
    count = pick - 1
    while count >= 0:
        temp = max(m[:len(m)-count])
        ret.append(temp)
        index = m[:len(m)-count].index(str(temp))
        m = m[index+1:]
        count -= 1
    print int(''.join(ret))

a = 0
m,n = 0,0
while 1:
    s = raw_input()
    if s!='':
        if (a%2):
            n = s
            solution(m,int(n))
        else:
            m = s
        a += 1
    else:
        break