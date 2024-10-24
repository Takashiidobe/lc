from typing import Optional
from utils import TreeNode


# @leet start
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        """
        This question asks us to figure out if two trees are flip equivalent,
        so if you can have any sequence of flips (swapping the left and right
        subtree) of either tree, we return true.
        If the trees are not flip equivalent, return false.

        We can solve the problem kind of like same tree -- if both trees are
        the same, we want to return true. If both trees are equal at this level
        and all subsequent levels with one flip, we want to return true.
        So at each level, we check if every level is either the same or if flipping
        this level and either flipping or keeping each subtree the same results
        in equivalent trees.
        """
        def equal(l, r):
            if l is None and r is None:
                return True
            if l is None or r is None:
                return False
            is_flippable = l.val == r.val \
                    and equal(l.left, r.right) \
                    and equal(l.right, r.left)
            is_same = l.val == r.val \
                    and equal(l.left, r.left) \
                    and equal(l.right, r.right)
            return is_flippable or is_same
        return equal(root1, root2)


# @leet end

def test():
	assert(2 + 2 == 4)
