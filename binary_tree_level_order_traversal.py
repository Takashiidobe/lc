from typing import Optional
from utils import TreeNode
from collections import deque


# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        """
        This function returns the level order traversal of a binary tree.
        It does this by BFSing through the nodes, and keeping the level
        of each node during the traversal.

        This could be made terser by using a defaultdict (so you dont have to initialize
        any of the lists by level.
        """
        if not root:
            return []
        res = []
        q = deque([(root, 0)])

        while q:
            node, level = q.popleft()
            if len(res) <= level:
                res.append([])
            res[level].append(node.val)
            if node.left:
                q.append((node.left, level + 1))
            if node.right:
                q.append((node.right, level + 1))

        return res


# @leet end


def test():
    assert 2 + 2 == 4
