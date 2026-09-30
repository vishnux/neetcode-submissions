class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         #print(i, nums[i], '---', j, nums[j])
        #         #print(nums[i], '---', nums[j])
        #         if nums[i] == nums[j]:
        #             return True
            nums.sort()
            for i in range(1, len(nums)):
                if nums[i-1] == nums[i]:
                    return True
            return False