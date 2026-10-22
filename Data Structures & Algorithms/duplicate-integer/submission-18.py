class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sorted_nums = sorted(nums)
        for i in range(1, len(sorted_nums)):
            if sorted_nums[i-1] == sorted_nums[i]:
                print(sorted_nums[i-1])
                print(sorted_nums[i])
                return True
        else:
            return False