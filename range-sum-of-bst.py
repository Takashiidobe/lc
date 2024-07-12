from typing import Optional
from utils import TreeNode, to_bst

# @leet start
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        """
        This function calculates the range sum of a BST between two numbers, `low` and `high`, inclusive.
        To do this, imagine we have a tree node. There are two cases:
        1. The node is null. In this case, we return 0.
        2. The node is non-null.
        In the non-null case, there are three cases:
        1. If the node's value is within low..high.
            a. In this case, we add the node's total to the sum and recurse to
            the left and right nodes, since they both can also be in range.
        2. If the node's value is $\lt$ low.
            a. In this case, we know that the left node will always be less than the current node value.
            Thus, we only want to check to the right. We do not add our current value to the sum, and
            continue to recurse to the right hand side.
        3. If the node's value is $\gt$ high.
            a. In this case, we know the right node value is too high. Thus, we only check to the left.
            We do not add our current value to the total, and only recurse to the left hand side,
            since that would lower the next node's value.
        """
        if not root:
            return 0
        if low <= root.val <= high:
            return root.val + \
                    self.rangeSumBST(root.left, low, high) + \
                    self.rangeSumBST(root.right, low, high)
        elif root.val > high:
            return self.rangeSumBST(root.left, low, high)
        elif root.val < low:
            return self.rangeSumBST(root.right, low, high)
        raise RuntimeError("This should be unreachable")


# @leet end
sol = Solution()
def test():
    assert(sol.rangeSumBST(to_bst([10,5,15,3,7,None,18]), 7, 15) == 32)
    assert(sol.rangeSumBST(to_bst([10,5,15,3,7,13,18,1,None,6]), 6, 10) == 23)

