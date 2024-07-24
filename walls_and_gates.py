from collections import deque


# @leet start
class Solution:
    def wallsAndGates(self, rooms: list[list[int]]) -> None:
        """
        We bfs from each gate to each room, to find the minimum distance.
        This takes $O(mn)$ time instead of the naive bfs from each room
        to a gate, which is $O(m^2n^2)$.
        As long as we BFS from at most $k$ places at the same time and
        terminate after we've visited all the rooms, we can maintain $O(mn)$
        time complexity.
        """
        m, n = len(rooms), len(rooms[0])
        gate, empty_room = 0, 2**31 - 1
        empty_rooms = set()
        q = deque()

        for y in range(m):
            for x in range(n):
                if rooms[y][x] == gate:
                    q.append((y, x, 0))
                    empty_rooms.add((y, x))
                if rooms[y][x] == empty_room:
                    empty_rooms.add((y, x))

        while q:
            y, x, dist = q.popleft()
            if (y, x) in empty_rooms:
                dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
                rooms[y][x] = dist
                empty_rooms.remove((y, x))
                for dy, dx in dirs:
                    q.append((dy + y, dx + x, dist + 1))


# @leet end


def test():
    assert 2 + 2 == 4
