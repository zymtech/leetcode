

def solution(n,m):
    """
    testcase 80% passed
    :param n: string
    :param m: string
    :return: print Bool
    """
    if m[0] == '0':
        if n[0] == '0':
            print 'YES'
            return
        else:
            print 'NO'
            return
    memo = {}
    for i in n:
        if i not in memo:
            memo[i] = 1
        else:
            memo[i] += 1
    for j in m:
        if j not in memo:
            print 'NO'
            return
        else:
            memo[j] -= 1
    for k in memo:
        if memo[k] != 0:
            print 'NO'
            return
    if len(m) == 1:
        if m == n:
            print 'YES'
            return
        else:
            print 'NO'
            return
    if len(m) == 2:
        if m[1] >= m[0]:
            print "YES"
            return
        else:
            print "NO"
            return
    for i in range(1,len(m)-1):
        if m[i] != '0':
            if m[i] >= m[0]:
                if m[i] > m[i+1]:
                    print 'NO'
                    return
            else:
                print 'NO'
                return
    print "YES"
    return


count = 0
m = 0
n = 0
while 1:
    s = raw_input()
    if s != '':
        if count == 0:
            n = s
            count += 1
        elif count == 1:
            m = s
            solution(n,m)
            count, m,n = 0, 0, 0
    else:
        break