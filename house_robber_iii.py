from utils import TreeNode
from typing import Optional


# @leet start
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        """
        This question asks us to solve a problem where we traverse a binary tree,
        and have to maximize our payoff given we can only take a parent or child
        node at every time.
        So, if we take our current node, we cannot take the left or right subtree's
        payoff as well.
        Thus, for each node, we want to be able to state the payoff for taking
        it (its node.val + skipping its next level) or skipping the current node,
        (taking the maximum of either skipping or taking its left and right child).

        To do this, we have each node return its max payoff if we take this
        node or if we don't take this node, and apply it to the starting node.
        This is done by returning a tuple, of (rob, skip) for each node. For
        each node, we either have the choice of robbing (where we take the node)
        or skipping. We return that for each node. Then, at the end, we start
        from the root and get the maximum result from that traversal.
        """

        def dp(node):
            if not node:
                return (0, 0)
            left = dp(node.left)
            right = dp(node.right)
            rob = node.val + left[1] + right[1]
            skip = max(left) + max(right)
            return (rob, skip)

        return max(dp(root))


# @leet end


def test():
    assert 2 + 2 == 4
