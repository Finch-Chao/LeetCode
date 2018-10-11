class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows <= 1 or numRows >= len(s):
            return s
        a = numRows * ['']
        l, step = 0, -1
        for i in s:
            a[l] += i
            if l % (numRows - 1) == 0:
                step = -step
            l += step
        return ''.join(a)
        