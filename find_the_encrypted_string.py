# @leet start
class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        """
        This class returns the string, where for a string `s`, and an integer `k`,
        for each character `c` in `s`, replacing `c` with the `kth` character after `c` in the string.
        It does this literally.
        """
        return ''.join(s[(i + k) % len(s)] for i in range(len((s))))

# @leet end
sol = Solution()
def test():
	assert(sol.getEncryptedString('dart', 3) == 'tdar')
	assert(sol.getEncryptedString('aaa', 1) == 'aaa')
