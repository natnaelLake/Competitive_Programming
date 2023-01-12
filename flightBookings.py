class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        answers = [0 for i in range(n)]
        for i in bookings:
            answers[i[0]-1]+=i[2]
            if i[1]<n:
                answers[i[1]]-=i[2]
        for i in range(1,n):
            answers[i] += answers[i-1]
        return answers