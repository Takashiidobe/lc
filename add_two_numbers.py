from utils import ListNode
from typing import Optional


# @leet start
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        """
        To add two linked list, we can employ the grade school addition algorithm.

        While both lists have a member, we can use divmod 10 to get the carry
        and the digit to place in the resulting linked list node.

        Finally, we have to increment the two list nodes and the result.

        At the end we may have one list with remaining members, so we do the same
        algorithm, just without the other list.

        Finally, we have to make sure to save the carry if it still exists after
        all this time into the last linked list node.
        """
        carry = 0
        dummy = ListNode()
        ret_node = dummy

        def add_to_end(l):
            nonlocal carry, dummy
            while l:
                carry, digit = divmod(l.val + carry, 10)
                new_node = ListNode(digit)
                dummy.next = new_node
                dummy = dummy.next
                l = l.next

        while l1 and l2:
            carry, digit = divmod(l1.val + l2.val + carry, 10)
            new_node = ListNode(digit)
            dummy.next = new_node
            dummy = dummy.next
            l1 = l1.next
            l2 = l2.next

        add_to_end(l1)
        add_to_end(l2)
        if carry:
            dummy.next = ListNode(carry)

        return ret_node.next


# @leet end


def test():
    assert 2 + 2 == 4
