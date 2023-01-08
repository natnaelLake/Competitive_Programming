class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        result, n = [], len(A)
        for i in range(n, 0, -1):
            pos = A.index(i)
            if pos == i - 1:
                continue
            if pos != 0:
                result.append(pos + 1)
                A[: pos + 1] = A[: pos + 1][::-1]
            result.append(i)
            A[:i] = A[:i][::-1]
        return result