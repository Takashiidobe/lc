from utils import TreeNode
from typing import Optional
# @leet start


class Solution:
    def lowestCommonAncestor(
        self, root: Optional[TreeNode], p: TreeNode, q: TreeNode
    ) -> Optional[TreeNode]:
        """
        To find the least common ancestor of two nodes in a BST, we want to
        find the node which splits `p` and `q` into different sides of the tree.
        If `p` and `q` are on the same side of the tree, there is a better LCA to find.
        So we check the root's value. If it is greater than both `p` and `q`, we go left
        to find a smaller node value.
        If it is smaller than both `p` and `q`, we go right to find a smaller node value.
        If `p` is greater than root and `q` is smaller (or vice-versa) we've found the LCA.
        Return that node in this case.
        """
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return root


# @leet end


def test():
    assert 2 + 2 == 4
