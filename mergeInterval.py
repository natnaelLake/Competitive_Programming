def mergeIntervals(intervals):
    intervals.sort()
    stack = []
    stack.append(intervals[0])
    for i in intervals[1:]:
        if stack[-1][0] <= i[0] <= stack[-1][-1]:
            stack[-1][-1] = max(stack[-1][-1], i[-1])
        else:
            stack.append(i)
 
    print("The Merged Intervals are :", end=" ")
    for i in range(len(stack)):
        print(stack[i], end=" ")
arr = [[6, 8], [1, 9], [2, 4], [4, 7]]
mergeIntervals(arr)