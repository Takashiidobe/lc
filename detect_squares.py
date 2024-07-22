from collections import defaultdict


# @leet start
class DetectSquares:
    """
    This class detects the squares that are axis aligned given a query point
    and 3 points that have been seen in the stream.

    When adding a point, we just add it to a hashmap.

    When counting, we iterate through all the points in the map,
    and calculate the axis adjacent points by comparing each with the current point.

    We then calculate the diagonal of each point and then see how many times the points
    appear in the set to return the final count.
    """

    def __init__(self):
        self.points = defaultdict(int)

    def add(self, point: list[int]) -> None:
        self.points[tuple(point)] += 1

    def count(self, point: list[int]) -> int:
        count = 0
        x1, y1 = point
        for (x2, y2), n in self.points.items():
            x_dist, y_dist = abs(x1 - x2), abs(y1 - y2)
            if x_dist == y_dist and x_dist > 0:
                corner1 = (x1, y2)
                corner2 = (x2, y1)

                if corner1 in self.points and corner2 in self.points:
                    count += n * self.points[corner1] * self.points[corner2]
        return count


def test():
    assert 2 + 2 == 4
