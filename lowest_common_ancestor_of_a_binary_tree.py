from utils import TreeNode


# @leet start
class Solution:
    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        """
        This question asks us to find the lowest common ancestor of a binary
        tree. Since it's not a binary search tree, we can't just split the
        tree in half. Instead, we want to find the node where p and q are either
        the node and in one of its subtrees, or in both of its subtrees.

        To do so, we can recurse through the left and right subtrees, and
        check if the current node is p or q. Finally, if left, mid, or right
        are p or q, we can set the parent to our current candidate.

        We continue going down the tree and make progress toward the parent candidate
        until we can't anymore.
        The recursion function needs to return if it contains one of the items
        in its subtree, so it returns node == p or node == q or left or right.
        """
        parent = None

        def recurse(node):
            nonlocal parent
            if not node:
                return False
            left = recurse(node.left)
            right = recurse(node.right)
            mid = node == p or node == q
            if [left, mid, right].count(True) >= 2:
                parent = node
            return mid or left or right

        recurse(root)
        return parent


# @leet end


def test():
    assert 2 + 2 == 4
