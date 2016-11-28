class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def setZeroes(self, A):
        m = len(A)
        n = len(A[0])
        R = [1] * m
        C = [1] * n

        for i in range(m):
            for j in range (n):
                if A[i][j] == 0:
                    R[i] = 0
                    C[j] = 0       
        for i in range(m):
            for j in range (n):    
                if R[i]*C[j] == 0:
                    A[i][j] = 0
        return A