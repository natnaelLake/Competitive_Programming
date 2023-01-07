class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        count,sum,flag = 0,0,0
        
        for i in range(len(piles)-1):
            max = i
            for j in range(i+1,len(piles)):
                if(piles[max]< piles[j]):
                    max = j
                if j==len(piles)-1:
                    count = count +1
                    if count == 2:
                        flag = flag + 1
                        sum = sum + piles[max]
                        count = 0
            if flag ==len(piles)//3:
                break;   
            if i!=max:
                temp = piles[i]
                piles[i] = piles[max]
                piles[max] = temp
        return sum
