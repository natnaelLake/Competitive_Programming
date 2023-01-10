from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hash = defaultdict(lambda:0)
        count = 0
        totalSum = 0
        for i in range(len(nums)):
            totalSum += nums[i]
            if totalSum == k:
                count += 1
            if (totalSum-k) in hash:
                count  += hash[totalSum - k]
            hash[totalSum] +=1
        return count