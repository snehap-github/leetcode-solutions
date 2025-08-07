class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        mapping = dict()

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            if (s[i] in mapping and mapping[s[i]] != t[i]) or (s[i] not in mapping and t[i] in mapping.values()):
                return False
            mapping[s[i]] = t[i]

        return True

        