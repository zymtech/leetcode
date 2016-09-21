
def solution(m,n):
    count = 0
    for i in range(len(n)-1):
        for j in range(i+1,len(n)):
            if int(n[i])^int(n[j]) > int(m.split()[1]):
                count += 1
    print count

a = 0
m,n = 0,0
while 1:
    s = raw_input()
    if s!='':
        if (a%2):
            n = s
            solution(m,n.split())
        else:
            m = s
        a += 1
    else:
        break