class MinStack:

    def __init__(self):
        self.Stack = []
        self.minStack = []
    def push(self, val: int) -> None:
        self.Stack.append(val)
        if len(self.minStack) != 0:
            smallest = min(val,self.minStack[-1])
            self.minStack.append(smallest)
        else:
            self.minStack.append(val)
        return None
    def pop(self) -> None:
        print(self.Stack)
        self.minStack.pop()
        return self.Stack.pop()
    def top(self) -> int:
        return self.Stack[-1]
    def getMin(self) -> int:
        
        return self.minStack[-1]