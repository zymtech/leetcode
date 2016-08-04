# -*- coding: utf-8 -*-
"""
网易内推笔试编程第一题
给定字符串，找出包含'ntes'的所有组合，顺序不能变
比如：’nnttes' 输出 4
"""

class Solution(object):
    def solution(self, s):
        for i, j in enumerate(s):
            if j not in ['n', 't', 'e', 's']:
               del s[i]
        # cosidering dynamic programming