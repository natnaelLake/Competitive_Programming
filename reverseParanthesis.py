class Solution:
    def reverseParentheses(self, s: str) -> str:
        Stack = []
        Stack1 = []
        valueStack = []
        j=0
        for i in range(len(s)):
            if s[i] == '(':
                valueStack.append(i)
            else:
                Stack1.append(s[i])
            if s[i] == ')':
                temp = s[valueStack[-1]:i+1]
                s = s[:valueStack[-1]]+temp[::-1]+s[i+1:]
                del valueStack[-1]
        result = ''
        for i in range(len(s)):
            if  s[i] !=')' and s[i] !='(':
                result +=s[i]
        return result