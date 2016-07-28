# -*- coding: utf-8 -*-


class Solution(object):
    def __init__(self):
        self.ret = []

    def inorderTraversal(self, root):
        if root is not None:
            self.inorderTraversal(root.left)
            self.ret.append(root.val)
            self.inorderTraversal(root.right)
        return self.ret
