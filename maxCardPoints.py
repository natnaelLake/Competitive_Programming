class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        totalSum = sum(cardPoints[:len(cardPoints) - k])
        firstSum = sum(cardPoints)
        ans = firstSum - totalSum
        for i in range(k):
            totalSum -= cardPoints[i]
            totalSum += cardPoints[i + len(cardPoints) - k]
            ans = max(ans, firstSum - totalSum)
        return ans