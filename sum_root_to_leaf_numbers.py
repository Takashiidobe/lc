from utils import TreeNode
from typing import Optional


# @leet start
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        """
        This question asks us to return the sum of all the values in a path
        from root to leaf. So, we can do a root to leaf traversal, aggregate
        all the totals, and sum them up.

        Normally I would check for the node to be None to return a path, but
        that double counts paths from root to leaf, so in this case I will just traverse
        from root to leaf and check the condition that the node is a leaf before
        returning.
        Finally, you can either create a new array or backtrack (using append/pop).
        It's slightly faster when backtracking (because there's less memory usage)
        but it's also trickier. I would prefer the extra copy version in an interview
        and then swap to backtracking if required.
        """
        nums = []

        def list_to_num(l):
            return int("".join(map(str, l)))

        def traverse(node, path):
            if node is None:
                return
            path.append(node.val)
            if node.left is None and node.right is None:
                nums.append(list_to_num(path))
                path.pop()
                return
            traverse(node.left, path)
            traverse(node.right, path)
            path.pop()

        traverse(root, [])
        return sum(nums)


# @leet end


def test():
    assert 2 + 2 == 4
