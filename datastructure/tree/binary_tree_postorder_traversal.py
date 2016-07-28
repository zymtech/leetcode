# -*- coding: utf-8 -*-


class Solution(object):
    def __init__(self):
        self.ret = []

    def postorderTraversal(self, root):
        if root is not None:
            self.postorderTraversal(root.right)
            self.postorderTraversal(root.left)
            self.ret.append(root.val)
        return self.ret