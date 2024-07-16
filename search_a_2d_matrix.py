# @leet start
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        """
        This problem asks to to search in a 2D matrix where each row is sorted
        in non-decreasing order and the first integer of every row is greater
        then the last integer of the previous row.

        The brute force would be $O(m * n)$ time, where you search every cell for
        the value.

        However, the question asks for a solution in $O(\log{}m * n)$ time.
        To do so, we can binary search to find the row that could contain the value
        and then binary search inside that row to check if the value exists.

        This can be expressed a bit more tersely by using a bisect function.
        """
        left, right = 0, len(matrix) - 1

        row_idx = None

        while left <= right:
            mid = (left + right) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                row_idx = mid
                break
            elif matrix[mid][-1] < target:
                left = mid + 1
            else:
                right = mid - 1

        if row_idx is None:
            return False

        row = matrix[row_idx]

        left, right = 0, len(row) - 1
        while left <= right:
            mid = (left + right) // 2
            if row[mid] == target:
                return True
            elif row[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False


# @leet end
sol = Solution()


def test():
    assert sol.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3)
    assert not sol.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13)
