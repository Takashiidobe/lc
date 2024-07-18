from math import inf
from utils import TreeNode


# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        This function counts the nodes in a tree where on the path from root to X
        there are no nodes with a value greater than X.

        We do this by dfsing through the tree, counting the maximum value we've seen
        so far. If we haven't seen a value greater than the current node, we add 1
        to the count.

        For the left and right nodes, we want to maximize the value we've seen,
        so if we see a new greater node, we'll use that as the new max so far,
        otherwise, we'll use the old max.

        At the end after counting we end up with the correct amount of good nodes.
        """
        count = 0

        def dfs(node, max_so_far):
            nonlocal count
            if max_so_far <= node.val:
                count += 1
            if node.right:
                dfs(node.right, max(max_so_far, node.val))
            if node.left:
                dfs(node.left, max(max_so_far, node.val))

        dfs(root, -inf)
        return count


# @leet end


def test():
    assert 2 + 2 == 4
