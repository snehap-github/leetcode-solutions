class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join([c.lower() for c in s if c.isalnum()])
        reverse_s = s[::-1]
        return s == reverse_s
        

        