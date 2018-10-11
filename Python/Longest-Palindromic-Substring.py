class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """ 
        if len(s) <= 1:
            return s
        sub = s[1]
        for i in range(len(s) - 1):  
            s1 = self.isPalindromic(s, i, i)
            if len(s1) > len(sub):
                sub = s1
            s2 = self.isPalindromic(s, i, i + 1)
            if len(s2) > len(sub):
                sub = s2
        return sub
        
    def isPalindromic(self, s, x, y):
        while x >= 0 and y < len(s) and s[x] == s[y]:
                x -= 1
                y += 1
        return s[(x + 1) : y]