class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def rotate(self, A):
        def rotateMatrix(A):
            rotatedA = [[0]*len(A) for i in range(len(A))]
            for i in range(len(A)):
                for j in range(len(A[i])):
                    rotatedA[j][len(A) - i - 1] = A[i][j]
            return rotatedA
            
        rotatedA = rotateMatrix(A)
        return rotatedA