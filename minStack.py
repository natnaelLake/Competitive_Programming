class MinStack:

    def __init__(self):
        self.Stack = []
    def push(self, val: int) -> None:
        self.Stack.append(val)
        return None
    def pop(self) -> None:
        print(self.Stack)
        return self.Stack.pop()
        
    def top(self) -> int:
        top = 0
        for i in range(len(self.Stack)):
            if i == len(self.Stack)-1:
                top = self.Stack[i]
        return top
    def getMin(self) -> int:
        minVal = 0
        minVal = self.Stack[0]
        for i in range(len(self.Stack)-1):
            for j in range(i+1,len(self.Stack)):
                if minVal> self.Stack[j]:
                    minVal = self.Stack[j]
        return minVal

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()