# -*- coding: utf-8 -*-
import collections


class Queue():
    def __init__(self):
        self.data = collections.deque()

    def push(self, x):
        self.data.append(x)

    def peek(self, x):
        return self.data[0]

    def pop(self, x):
        return self.data.popleft()

    def size(self, x):
        return len(self.data)

    def empty(self):
        return len(self.data)==0


class Stack():
    def __init__(self):
