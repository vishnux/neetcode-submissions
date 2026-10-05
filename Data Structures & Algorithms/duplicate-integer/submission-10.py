class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_set = set(nums)
        len_nums_set = len(nums_set)
        print(len(nums_set))
        len_nums = len(nums)
        print(len(nums))
        if len(set(nums)) < len(nums):
            return True
        else: 
            return False