# @leet start
class SparseVector:
    """
    This question asks us to compute the dot product of two matrices that are
    sparse. We don't want to multiply a bunch of zeroes, so we can keep the non
    zero numbers in a hashmap and then sum the result later on.
    """

    def __init__(self, nums: list[int]):
        self.nonzeroes = {}
        for i, n in enumerate(nums):
            if n != 0:
                self.nonzeroes[i] = n

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: "SparseVector") -> int:
        result = 0
        for i, n in self.nonzeroes.items():
            if i in vec.nonzeroes:
                result += n * vec.nonzeroes[i]
        return result


# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
# @leet end


def test():
    assert 2 + 2 == 4
