class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        alpha_dict = dict()
        num = 1
        for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            alpha_dict[c] = num
            num += 1
        
        answer = 0
        for pos in list(range(len(columnTitle)-1,-1,-1)):
            answer += alpha_dict[columnTitle[::-1][pos]] * pow(26,pos)

        return answer