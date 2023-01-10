class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        rightSum = 0
        totalSum = 0
        leftSum = 0
        value = 0
        for i in range(len(nums)):
            totalSum = totalSum + nums[i]
        for j in range(len(nums)):
            leftSum = totalSum - nums[j]
            if rightSum == leftSum:
                value = j
                break
            else:
                value = -1
            rightSum = rightSum + nums[j]
            totalSum = leftSum
            print(leftSum,rightSum)
            
        return value