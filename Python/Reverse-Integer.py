class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        l = list(str(abs(x)))
        l.reverse()
        r = int(''.join(l))
        if r > 2147483647:
            return 0
        else:
            return r if x >= 0 else r * ( - 1)