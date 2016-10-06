# sum of subsets

import sys

global result
result = 0

def find(arr, num, path=()):
   global result
   if not arr:
       return
   if arr[0] == num:
       result += 1
   else:
       find(arr[1:], num - arr[0], path + (arr[0],))
       find(arr[1:], num, path)

while 1:
    try:
        n = int(sys.stdin.readline().split()[1])
        line = sys.stdin.readline().strip()
        values = map(int, line.split())
        find(values,n)
        print result
    except BaseException:
        break
