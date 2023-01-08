class Solution:
    def isValid(self, s: str) -> bool:
        openStr = ['(','{','[']
        closeStr = [')','}',']']
        stack = []
        for i in s:
            if i in closeStr and len(stack)==0:
                return False
            else:
                if i in openStr:
                    stack.append(i)
                elif i in closeStr:
                    ind = closeStr.index(i)
                    if openStr[ind] == stack[len(stack)-1]:
                        stack.pop()
                    else:
                        return False
        if len(stack) == 0:
            return True
        else :
            return False