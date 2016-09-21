def solution(s):
    """
    :param s: str
    :return: print nums
    """
    ret = 0
    j = 0
    for i in range(j,len(s)):
        maxtemp = 0
        j = i
        for j in range(j,len(s)):
            if isOkay(s[:i] + s[j+1:]):
                maxtemp += 1
            else:
                if maxtemp > ret:
                    ret = maxtemp
                continue
    print ret

def isOkay(s):
    if ('A' in s) and ('B' in s) and ('C' in s) and ('D' in s) and ('E' in s):
        return True
    else:
        return False

while 1:
    s = raw_input()
    if s!='':
        solution(s)
    else:
        break