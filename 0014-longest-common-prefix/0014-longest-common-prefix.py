class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        small_str = min(strs , key = len)
        prefix = []
        
        for i in range(len(small_str)):
            for ele in strs:
                if small_str[i] != ele[i]:
                    return "".join(prefix)
            prefix.append(small_str[i])

        return "".join(prefix)