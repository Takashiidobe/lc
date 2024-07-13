from utils import TreeNode, to_bst
from typing import Optional
# @leet start
class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> Optional[TreeNode]:
        """
        To turn a sorted list into a BST, we can look at the properties of a sorted list and a BST.
        To build a BST, we want the following properties:
        The current node's val should be node.left.val < node.val < node.right.val
        Since the list is sorted, the middle value perfectly splits the tree in two.
        So, the root node's value is the middle value.
        Then, we recurse onto the right hand side by defining its value as between the midpoint and the end.
        Likewise, the left hand side is between the start and the midpoint.
        """
        if not nums:
            return None
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root

# @leet end
sol = Solution()
def test():
	assert(sol.sortedArrayToBST([-10, -3, 0, 5, 9]) == to_bst([-10, -3, 0, 5, 9]))
	assert(sol.sortedArrayToBST([]) == to_bst([]))
	assert(sol.sortedArrayToBST([1, 3]) == to_bst([1, 3]))
