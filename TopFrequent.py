class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashSet = {}
        count = 0
        nums.sort()
        a = 0
        for i in range(len(nums)):
            hashSet[nums[i]] = hashSet.get(nums[i],0)+1
        maxList = list(hashSet.values())
        maxListKey = list(hashSet.keys())
        maxList.sort(reverse = True)
        maxList = maxList[:k]
        maxArr = [0]*len(maxList)
        a = 0
        print(maxList)
        for value in maxList:
            print(hashSet.keys())
            for mainKey in hashSet.keys():
                print(hashSet.keys())
                if hashSet[mainKey]==value:
                    maxArr[a] = mainKey
                    a = a+1
                    maxList = maxList[a:]
                    del hashSet[mainKey]
                    break
        return maxArr