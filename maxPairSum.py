class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        maxNum = 0
        nums.sort()
        i = 0
        j = len(nums)-1
        while(i<j):
            nums[i] = nums[i] + nums[j]
            i = i+1
            j = j-1
        maxNum = nums[0]
        for k in range(len(nums)//2):
            if maxNum < nums[k]:
                maxNum = nums[k]

        return maxNum