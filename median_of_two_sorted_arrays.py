# @leet start
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        l, r = 0, m

        while l <= r:
            x_mid = (l + r) // 2
            y_mid = (m + n + 1) // 2 - x_mid

            max_x = float("-inf") if x_mid == 0 else nums1[x_mid - 1]
            max_y = float("-inf") if y_mid == 0 else nums2[y_mid - 1]
            min_x = float("inf") if x_mid == m else nums1[x_mid]
            min_y = float("inf") if y_mid == n else nums2[y_mid]

            if max_x <= min_y and max_y <= min_x:
                if (m + n) % 2 == 0:
                    return (max(max_x, max_y) + min(min_x, min_y)) / 2
                else:
                    return max(max_x, max_y)
            elif max_x > min_y:
                r = x_mid - 1
            else:
                l = x_mid + 1

        return -1.0


# @leet end


def test():
    assert 2 + 2 == 4
