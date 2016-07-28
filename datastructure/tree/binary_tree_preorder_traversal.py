# coding: utf-8


class Solution():
    def __init__(self):
        self.ret = []

    def preorderTraversal(self, root):
        if root is not None:
            self.ret.append(root.val)
            self.preorderTraversal(root.left)
            self.preorderTraversal(root.right)
        return self.ret