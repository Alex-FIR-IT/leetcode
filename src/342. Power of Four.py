from math import log


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and (power := log(n, 4)) == int(power)