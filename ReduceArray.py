class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        hashSet = {}
        count = 0
        arr.sort()
        for i in range(len(arr)):
            hashSet[arr[i]] = hashSet.get(arr[i],0)+1
        arr1 = [0]*len(hashSet)
        arr2 = [0]*len(hashSet)
        a = 0
        for item in hashSet:
            arr1[a] = hashSet[item]
            a = a+1
        arr1.sort()
        a=0
        for i in arr1[::-1]:
            arr2[a] = i
            a = a+1
        count = 1
        for a in range(1,len(arr2)):
            sumNum = 0
            for b in range(0,a):
                sumNum = sumNum + arr2[b]
            if sumNum <(len(arr)//2):
                count = count+1
            if count > len(arr)//2:
                break
        return count
