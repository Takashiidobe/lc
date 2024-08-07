from typing import Optional
from utils import ListNode
from heapq import heapify, heappush, heappop


# @leet start
class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        """
        To merge K sorted lists, we can first put all of the head node vals of the list
        into a heap, along with their indices.

        While we have items in our heap, we construct a list by popping the minimum
        value from the heap and then adding a new value from the list that we
        popped from, using the index provided alongside the heap.

        At the end, we return the resulting list.
        """

        dummy = ListNode()
        curr = dummy

        heap = []

        for index, l in enumerate(lists):
            if l is not None:
                heap.append((l.val, index))
                lists[index] = lists[index].next

        heapify(heap)

        while heap:
            min_val, index = heappop(heap)
            curr.next = ListNode(min_val)
            curr = curr.next

            if lists[index] is not None:
                heappush(heap, (lists[index].val, index))
                lists[index] = lists[index].next

        return dummy.next


# @leet end


def test():
    assert 2 + 2 == 4
