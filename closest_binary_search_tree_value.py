from collections import deque
from typing import Optional
from utils import TreeNode, to_binary_tree
# @leet start
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        """
        This problem is about finding the closest tree node value to a target.
        To find the closest value, we want to minimize abs(node.val - target) for
        each node in the tree.

        Naively this is pretty easy -- we iterate through all the nodes in the tree
        and then calculate abs(node.val - target) and return the closest node.
        This takes $O(n)$ time.

        If this was a binary tree, this would be the best we could do -- we must
        traverse all the nodes in a binary tree to find the closest value, because
        we have no way to prune any of the nodes during our search, since there is
        no ordering.

        However, since this is a Binary Search Tree, with a given ordering, we can
        reduce our time spent to $O(log_2(n))$, if the tree is balanced.

        To do this, we have to prune one side of the tree as we go down in, thus
        only looking at $log_2(n)$ nodes.

        There are three possible cases:
        1. node.val == target.
        In this case, we can just return this value, since the target is in the tree.
        2. node.val > target.
        We can check to see if we have the closest value. As well, we only want to check
        values on the left, since they could possibly be closer to the target.
        Any values on the right will only be greater, and thus, further from the target.
        3. node.val < target.
        We can check to see if we have the closest value. As well, we only want to check
        values on the right, since they could possibly be closer to the target.
        Any values on the left will only be lesser, and thus, further from the target.

        So, we code that up and return the closest node.
        """
        q = deque()
        if not root:
            raise RuntimeError('Root must not be None')
        q.append(root)
        min_dist = abs(root.val - target)
        min_val = root.val
        while q:
            node = q.popleft()
            if abs(node.val - target) < min_dist:
                min_dist = abs(node.val - target)
                min_val = node.val
            if abs(node.val - target) == min_dist:
                min_val = min(min_val, node.val)
            if node.right and node.val < target:
                q.append(node.right)
            if node.left and node.val > target:
                q.append(node.left)
        return min_val

# @leet end
sol = Solution()
def test():
    assert(sol.closestValue(to_binary_tree([4,2,5,1,3]), 3.714) == 4)
    assert(sol.closestValue(to_binary_tree([1]), 4.23) == 1)
