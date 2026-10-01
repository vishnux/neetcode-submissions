class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashmap_nums = {}
        for i in range(len(nums)):
            hashmap_nums[nums[i]] = i
            #print(hashmap_nums)
            #print('target', target)
        print(hashmap_nums)
        for i in range(len(nums)):
            if target - nums[i] in hashmap_nums:
                if i != hashmap_nums[target - nums[i]]:
                    print('target', target)
                    print('ith element', nums[i], 'index of element', i)
                    print('element',target - nums[i])
                    print('index of element', hashmap_nums[target - nums[i]])
                    #print(nums[i])
                    #print('index', nums[target - nums[i]])
                    #print(nums[i], nums[len(nums)-i])
                    if i < hashmap_nums[target - nums[i]]:
                        return [i, hashmap_nums[target - nums[i]]]
                    else :
                        return [ hashmap_nums[target - nums[i]], i]
        return [-1, -1]
