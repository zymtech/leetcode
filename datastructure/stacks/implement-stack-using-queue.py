# -*- coding: utf-8 -*-
import collections


class Queue():
    def __init__(self):
        self.data = collections.deque()

    def push(self, x):
        self.data.append(x)

    def peek(self):
        return self.data[0]

    def pop(self):
        return self.data.popleft()

    def size(self):
        return len(self.data)

    def empty(self):
        return len(self.data)==0


class Stack():
    def __init__(self):
        self.data = Queue()

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.data.push(x)
        for i in xrange(1,self.data.size()-1):
            self.data.push(self.data.pop())

    def pop(self):
        """
        :rtype: nothing
        """
        self.data.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.data.peek()

    def empty(self):
        """
        :rtype: bool
        """
        return self.data.empty()
