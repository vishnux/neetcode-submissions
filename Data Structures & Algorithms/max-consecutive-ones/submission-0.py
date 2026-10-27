class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt = 0
        res = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                res = max(cnt, res)
                cnt =0
            if nums[i] == 1:
                cnt += 1
        return max(cnt, res)
            
            