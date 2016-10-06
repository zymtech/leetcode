
def solution(l):
    """
    :param l: list
    :return: print max-depth
    """
    memo = {}
    for i in l:
        if i[0] not in memo:
            memo[i[0]] = [i[1]]
        else:
            memo[i[0]].append(i[1])
    if not memo:
        print 0
        return
    count = 1
    layer = ['0']
    while layer:
        temp = []
        for j in layer:
            if j in memo:
                temp.extend(memo[j])
        layer = temp
        if not layer:
            break
        count += 1
    memo.clear()
    print count
    return

a = raw_input()
lit = []
count = 0
while 1:
    a = raw_input()
    if a !='':
        if len(a.split()) == 2:
            lit.append(a.split())
        else:
            solution(lit)
            count = 0
            lit = []
    else:
        solution(lit)
        break


