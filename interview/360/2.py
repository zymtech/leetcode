# -*- coding: utf-8 -*-

global memory
global newcount
global memcount
memcount = {}
newcount = 0

def solution(maxmem, a):
    global memory
    memory = [0]*int(maxmem)
    for i in a:
        if len(i.split()) == 1:
            ope_def()
        else:
            operation, mem = i.split()[0], i.split()[1]
        if operation == "new":
            ope_new(mem)
        elif operation == 'del':
            ope_del(mem)

def ope_def():
    pass

def ope_new(mem):
    global memcount
    global newcount
    count = 0
    for j,i in enumerate(memory):
        if i == 0:
            count += 1
        else:
            count = 0
        if count == mem:
            newcount += 1
            for i in range(j,j-mem-1):
                memory[i] = 1
        memcount[newcount] = [j-mem,j]

def ope_del(mem):
    global memory
    global memcount
    global newcount
    if mem > newcount:
        return
    for i in memcount[mem]:
        memory[i] = 0

a = []
s = raw_input()
count = 0
c = int(s.split()[0])
maxmem = int(s.split()[1])
init = 1
while 1:
    if init:
        s = raw_input()
    if s!='':
        a.append(s)
        count += 1
        if count == c:
            solution(maxmem,a)
            s = raw_input()
            count = 0
            c = int(s.split()[0])
            maxmem = int(s.split()[1])
    else:
        break