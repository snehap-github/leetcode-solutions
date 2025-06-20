class Solution:
    def isValid(self, s: str) -> bool:

        op = ('(','{','[')
        cl = (')','}',']')
        l = []

        if len(s)%2 != 0:
            return False

        for br in s:
            if br in op:
                l.append(br)
            else:
                if len(l) ==0 or op.index(l.pop()) != cl.index(br):
                    return False

        return len(l) == 0