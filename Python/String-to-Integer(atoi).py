class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        sign = 1
        if not str:
            return 0
        if str[0] in ["+", "-"]:
            if str[0] == "-":
                sign = -1
            str = str[1:]
        strnum = 0
        for c in str:
            if c.isdigit():
                strnum = strnum * 10 + int(c)
            else:
                break
        strnum *= sign
        if strnum > 2147483647:
            return 2147483647
        if strnum < -2147483648:
            return -2147483648
        return strnum