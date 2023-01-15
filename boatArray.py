class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        final = len(people)-1
        first = 0
        answer = 0
        people.sort()
        while first<=final:
            carry = limit - people[final]
            final -=1
            if people[first]<=carry:
                first+=1
            answer+=1
        return answer