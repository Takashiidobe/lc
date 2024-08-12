from utils import TreeNode
from typing import Optional


# @leet start
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        """
        This question asks us to construct a binary tree from a preorder and
        inorder traversal. To do so, we note that the first item in a preorder
        traversal is always the root of the current tree, so we can make our root
        with `preorder[0]`.

        To find the left side of the tree, we find the index of `preorder[0]`
        in the inorder array, because that cuts the left and right subtrees.
        So, to build the left of the current tree, we can recursively pass
        `preorder[1:i + 1]` and `inorder[:i]`, which passes the left sides of
        the preorder and inorder arrays to `buildTree` and set that as our
        left side.

        We do the same for the right side, which is `preorder[i + 1:]`, and
        `inorder[i+1:]`.

        This solution is $O(n^2)$ time, and a faster solution would require
        putting all the indexes in a hashmap for constant time access to find
        the index.
        """
        return self.faster(preorder, inorder)

    def simple(self, preorder, inorder):
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        i = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1 : i + 1], inorder[:i])
        root.right = self.buildTree(preorder[i + 1 :], inorder[i + 1 :])

        return root

    def faster(self, preorder, inorder):
        def array_to_tree(left, right):
            nonlocal preorder_index
            if left > right:
                return None

            root_value = preorder[preorder_index]
            root = TreeNode(root_value)

            preorder_index += 1

            root.left = array_to_tree(left, inorder_index_map[root_value] - 1)
            root.right = array_to_tree(inorder_index_map[root_value] + 1, right)

            return root

        preorder_index = 0

        inorder_index_map = {num: i for i, num in enumerate(inorder)}

        return array_to_tree(0, len(preorder) - 1)


# @leet end


def test():
    assert 2 + 2 == 4
