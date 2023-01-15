class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subArray = ''
        max_length = 0
        if len(s) == 0 or len(s) == 1:
            return len(s)
        for i in s:
            if i in subArray:
                subArray = subArray[subArray.index(i)+1:]
            subArray = subArray + i
            if max_length < len(subArray):
                max_length = len(subArray)
        return max_length