class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        maxCap = 0
        basket = {}
        j = 0
        for i in range(len(fruits)):
            a = fruits[i]
            if a not in basket:
                basket[a] = 1
            else:
                basket[a] += 1
            while len(basket) > 2:
                k = fruits[j]
                basket[k] -= 1
                if basket[k] == 0:
                    del basket[k]
                j += 1
            maxCap = max(maxCap, i - j+1)
        return maxCap