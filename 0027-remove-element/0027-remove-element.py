class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        val_count = nums.count(val)

        for i in range(val_count):
            nums.remove(val)

        return len(nums)
        