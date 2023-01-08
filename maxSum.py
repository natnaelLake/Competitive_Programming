class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        last = len(nums)-1
        count = 0
        indJ= last
        indI = 0
        nums.sort()
        while(indI<indJ):
            if(nums[indI]+nums[indJ]>k):
                indJ = indJ-1
            elif nums[indI] + nums[indI]<k:
                iindI = indI-1
            else:
                count = count +1
                indJ = indJ+1
                indI = indI + 1
        return count