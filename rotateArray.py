class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k%len(nums)
        i = 0
        while i<k:
            store = nums.pop()
            nums.insert(0,store)
            i +=1