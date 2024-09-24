from typing import Optional
from utils import TreeNode


# @leet start
# Definition for a binary tree node.
class NodeValue:
    def __init__(self, min_node, max_node, max_size):
        self.max_node = max_node
        self.min_node = min_node
        self.max_size = max_size


class Solution:
    """
    This question asks us to find the largest subtree which is also a Binary
    Search Tree. We can do this by enforcing the invariant that each subtree
    is a BST. This can be done in $O(n^2)$ time, by checking for each node,
    if it is a valid BST. We can figure out if a tree is a BST by checking its
    properties, that its left side is less than root.val and its right side
    is greater than root.val for every item in the tree.

    We can optimize this by bubbling up the information all the way to the parent.
    This is done by making it so each tree returns 3 points of information:

    Its allowed maximum val, its allowed minimum val, and its maximum size.
    We then need to handle each case:

    If the node itself is None, it has a size of 0 but it can be any valid BST.
    So we return float('inf') for max, float('-inf') for min, and 0 for size.

    Otherwise, we check the left and right subtrees. If the left and right subtrees
    follow the property of left.max < node.val < right.min, then we have a valid
    BST at our current node. We can set our current max to min(node.val, left.min)
    and our min to max(node.val, right.max) and then return left.size + right.size
    + 1 for our size.

    Otherwise, we need to return that this tree is not a BST, thus we would return
    up the maximum size of the left or right subtree, and then return an invalid
    configuration, where the maximum is the minimum allowed number, and the minimum
    is the maximum allowed number.
    """

    def traverse(self, node):
        if not node:
            return NodeValue(float("inf"), float("-inf"), 0)

        left = self.traverse(node.left)
        right = self.traverse(node.right)

        if left.max_node < node.val < right.min_node:
            return NodeValue(
                min(node.val, left.min_node),
                max(node.val, right.max_node),
                left.max_size + right.max_size + 1,
            )

        return NodeValue(
            float("-inf"), float("inf"), max(left.max_size, right.max_size)
        )

    def largestBSTSubtree(self, node: Optional[TreeNode]) -> int:
        return self.traverse(node).max_size


# @leet end


def test():
    assert 2 + 2 == 4
