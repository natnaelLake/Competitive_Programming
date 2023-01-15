class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i = j = 0
        length = len(nums)
        while j < length:
            if nums[j] == 0:
                k -= 1
            if k < 0:
                if nums[i] == 0:
                    k += 1
                i += 1
            j += 1
        return j-i