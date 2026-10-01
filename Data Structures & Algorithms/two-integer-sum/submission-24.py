class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashmap_nums = {}
        for i in range(len(nums)):
            hashmap_nums[nums[i]] = i
        print(hashmap_nums)
        for i in range(len(nums)):
            if target - nums[i] in hashmap_nums:
                if i != hashmap_nums[target - nums[i]]:
                    #if i < hashmap_nums[target - nums[i]]:
                    return [i, hashmap_nums[target - nums[i]]]
                    # else :
                    #     return [ hashmap_nums[target - nums[i]], i]
        return [-1, -1]
