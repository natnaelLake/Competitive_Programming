class MyQueue:
    def __init__(self):
        self.s1 = []
        self.s2 = []
    def push(self, x: int) -> None:
        while len(self.s1) != 0:
            self.s2.append(self.s1[-1])
            self.s1.pop()
        self.s1.append(x)
        while len(self.s2) != 0:
            self.s1.append(self.s2[-1])
            self.s2.pop()
    def pop(self) -> int:
        x = self.s1[-1]
        self.s1.pop()
        return x
    def peek(self) -> int:
        return self.s1[-1]
    def empty(self) -> bool:
        if self.s1 == []:
            return True
        else:
            return False