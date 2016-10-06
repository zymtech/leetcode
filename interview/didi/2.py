import sys

def solution(array,num):

    if num == 0 or num < 1:
        return None
    elif len(array) == 0:
        return None
    else:
        if array[0] == num:
            return [array[0]]
        else:
            with_v = solution(array[1:],(num - array[0]))
            if with_v:
                return [array[0]] + with_v
            else:
                return solution(array[1:],num)



s = 0
l = []
count = 1
while 1:
    line = sys.stdin.readline()
    if line:
        if count == 2:
            for i in line.split():
                l.append(int(i))
            ret = len(solution(l,s))
            if ret:
                print ret
            else:
                print 0
            count = 1
        else:
            if len(line.split()) != 2:
                break
            s = int(line.split()[1])
            count += 1
    else:
        break