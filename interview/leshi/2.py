def solution(x):
    """
    :param int:
    :return: print step
    """
    if x == 0:
        print 0
        return
    step = 1
    length = 0
    while length < x:
        length += step
        if length == x:
            print step
            return
        step += 1
    step -= 1
    length = length - step
    step -= 1
    ret1 = step + 2*(x-length)
    step += 1
    length += step
    ret2 = step + 2*(length-x)
    print min(ret1,ret2)

while 1:
    s = raw_input()
    if s != '':
        if int(s) >= 0:
            solution(int(s))
        else:
            solution(-int(s))
    else:
        break