from utils import TreeNode
from typing import Optional


# @leet start
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        This problem asks to return true if one of the trees is a subtree of another.
        There are 3 ways to do this:
        1. Naive $O(n^2)$: We check each node to see if they are subtrees.
        2. Serialization $O(m + n)$: We serialize both trees and validate the subtree property.
        3. Hashing $O(m + n)$: We hash each subtree of the tree to some value, taking into consideration
        its left and right sutbrees.

        This function implements the serialization aprpoach.
        If the node is null, we return a "#" to denote that (any character that doesn't show up works)
        If the tree is non null, we prefix it with a "^" to denote the start of a subtree
        And then concatenate the serialization of the left, current node, and right tree.

        We then do serialize both trees, and check if the subtree is in the tree.
        We can do this in $O(m + n)$ time.
        """

        def serialize(node) -> str:
            if not node:
                return "#"
            return f"^{serialize(node.left)}{node.val}{serialize(node.right)}"

        serialized_root = serialize(root)
        serialized_sub = serialize(subRoot)

        return serialized_sub in serialized_root


# @leet end


def test():
    assert 2 + 2 == 4
