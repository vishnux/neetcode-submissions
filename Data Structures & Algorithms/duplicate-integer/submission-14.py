class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #Time - O(n^2), space - O(1)
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        # return False

        nums_sort = sorted(nums)
        for i in range(1, len(nums_sort)):
            if nums_sort[i-1] == nums_sort[i]:
                return True
        return False