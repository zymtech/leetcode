def jump(nums):
    if not nums:
        print 0
    reachable = 0
    curr_reacable = 0
    count = 0
    for i, lenth in enumerate(nums):
        if i > reachable:
            break
        if i > curr_reacable:
            curr_reacable = reachable
            count += 1
        reachable = max(reachable, i + int(lenth))
    if reachable < len(nums) - 1:
        print -1
    else:
        print count

a = 0
while 1:
    s = raw_input()
    if s!='':
        if (a%2):
            s = s.split()
            jump(s)
        a += 1
    else:
        break