def solution(s):
    memo = []
    for j,i in enumerate(s):
        if i=='A' or i=='B' or i=='C' or i=='D' or i=='E':
            memo.append(j)
    ret, maxtemp = 0, 0
    memo = sorted(memo)
    for i in range(len(memo)-1):
        if memo[i + 1] - memo[i] > ret:
            ret = memo[i+1] - memo[i]
    print ret-1


while 1:
    s = raw_input()
    if s!='':
        solution(s)
    else:
        break