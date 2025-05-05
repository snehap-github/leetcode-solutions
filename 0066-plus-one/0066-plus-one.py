class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        is_nine = False
        
        for i in range(len(digits))[::-1]:
            if digits[i] != 9:
                digits[i] = digits[i] + 1
                is_nine = False
                return digits
            else:
                digits[i] = 0
                is_nine = True
                continue

        if is_nine:
            digits.insert(0,1)
            return digits