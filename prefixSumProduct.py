class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftPro = [0]*len(nums)
        rightPro = [0]*len(nums)
        totPro = [0]*len(nums)
        leftPro[0] = 1
        rightPro[len(nums)-1] = 1
        for i in range(1,len(nums)):
            leftPro[i] = nums[i-1]*leftPro[i-1]
        for j in range(len(nums)-2,-1,-1):
            rightPro[j] = nums[j+1] * rightPro[j+1]
        for i in range(len(nums)):
            totPro[i] = leftPro[i]*rightPro[i]
        return totPro