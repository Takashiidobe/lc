# Definition for a Node.

# @leet start
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class Solution:
    def lowestCommonAncestor(self, p: Node, q: Node) -> Node:
        """
        This question is like finding a cycle in a linked list. We're given
        two nodes inside a binary tree and have to find the lowest common ancestor
        We can create a set, where we iterate up the parent pointers for the
        first pointer, saving all values we see, and then for the other side,
        iterating up until we see a value we've already visited, and that would be
        the LCA. That would take $O(h)$ time and $O(h)$ space for the set.

        We can do better.

        This can be done in $O(h)$ time and $O(1)$ space. Imagine the steps to
        find the LCA are `m` and `n` for `p` and `q` respectively. Say we take `p`
        and move it up to the root in `m` steps. If we were to take `n` extra steps
        by swapping its position to `q` and iterate up again, and do the same for
        the original `q`, we would find the LCA in `O(m + n)$` time which is $O(h)$
        and both pointers will meet at the LCA.
        """
        p1, p2 = p, q
        while p1 != p2:
            p1 = p1.parent if p1.parent else q
            p2 = p2.parent if p2.parent else p
        return p1


# @leet end


def test():
    assert 2 + 2 == 4
