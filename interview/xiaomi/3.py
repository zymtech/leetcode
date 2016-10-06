def solution(a):
    ret = []
    for i in a.split():
        ret.append(i[::-1])
    print ' '.join(ret)

while 1:
    a = raw_input()
    if not a:
        break
    solution(a[::-1])
