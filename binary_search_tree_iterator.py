from utils import TreeNode
from typing import Optional


# @leet start
class BSTIterator:
    """
    This question asks us to define a binary search tree iterator. We can
    do this by traversing the tree and then collecting all of the results
    into an array, and indexing into it, checking if the pointer is in or
    out of bounds. However, this takes $O(n)$ time, so it's memory expensive.
    We can do this in $O(h)$ memory if we use an iterable. Unfortunately,
    python doesn't have the ability to peek an iterable, unless you use
    `more_itertools` which leetcode doesn't support, so we can do it the old
    fashioned way of traversing the tree first and then calculating its length
    and then making an iterable.
    """

    def __init__(self, root: Optional[TreeNode]):
        self.len = 0
        self.i = -1

        def get_len(node):
            if not node:
                return
            self.len += 1
            get_len(node.left)
            get_len(node.right)

        get_len(root)

        def traverse(node):
            if not node:
                return
            yield from traverse(node.left)
            yield node.val
            yield from traverse(node.right)

        self.inorder = traverse(root)

    def next(self) -> int:
        self.i += 1
        return next(self.inorder)

    def hasNext(self) -> bool:
        return self.i < self.len - 1


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
# @leet end


def test():
    assert 2 + 2 == 4
