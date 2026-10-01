class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        A = []
        #nums = [2,1,6,3, 1]
        for i in range(len(nums)):
            A.append([nums[i], i]) # we want to get a dictionary of elements and old index before sorting
        print(A)
        A.sort()
        print(A)
        i, j = 0, len(A) - 1

        while i < j:
            cur = A[i][0] + A[j][0]
            if cur == target:
                if A[i][1] < A[j][1]:
                    return [A[i][1], A[j][1]]
                else:
                    return [A[j][1], A[i][1]]
            elif cur < target:
                i +=1 
            else:
                j-=1
        return []