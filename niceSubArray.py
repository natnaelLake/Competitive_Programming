class Solution:

    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        count2 = 0

        count = 0

        oddArray = [0]*(len(nums)+1)

        for i in range(len(nums)):

            oddArray[count]+=1

            if(nums[i]&1):

                count +=1

            if count>=k:

                count2 += oddArray[count-k]

        return count2