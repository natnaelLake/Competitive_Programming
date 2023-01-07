class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        answer = []
        arr = []
        for i in range(len(l)):
            count, temp, diff= 0,0,0
            for j in range(l[i],r[i]+1):
                arr.append(nums[j])  
            arr.sort()  
            for j in range(len(arr)-1):
                diff = (arr[j+1])-(arr[j])
                if j != 0:
                    if diff == temp:
                        count = count+1
                temp = diff
            if count == len(arr)-2:
                answer.append(True)
            else:
                answer.append(False)
            arr.clear()
        return answer