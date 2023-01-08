class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ['+','-','/','*']
        Stack = []
        count = 0
        for i in range(len(tokens)):
            # print(tokens[i])
            if tokens[i] in operators:
                count = count+1
                firstPop = Stack.pop()
                secondPop = Stack.pop()
                if tokens[i] is '+':
                    result = int(secondPop) + int(firstPop)
                if tokens[i] is '/':
                    result = int(secondPop) / int(firstPop)
                if tokens[i] is '*':
                    result = int(secondPop) * int(firstPop)
                if tokens[i] is '-':
                    result = int(secondPop) - int(firstPop)               
                Stack.append(result)
            else:
                Stack.append(tokens[i]) 
        if len(Stack)== 1:
            result = Stack.pop()
            return result               