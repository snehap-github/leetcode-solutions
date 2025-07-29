class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1
        for ind in range(len(haystack)):
            if haystack[ind:len(needle)+ind] == needle:
                return ind
        