class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums.sort(key = int)
        i = len(nums)
        count = 0;
        while i>=0:
            count = count+1
            i=i-1
            if count == k:
               return nums[i]
