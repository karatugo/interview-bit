# Given numRows, generate the first numRows of Pascal's triangle.

# Pascal's triangle : To generate A[C] in row R, sum up A'[C] and A'[C-1] from previous row R - 1. 

# **Example:**

# Given numRows = 5,

# Return

# ```
# [
#      [1],
#      [1,1],
#      [1,2,1],
#      [1,3,3,1],
#      [1,4,6,4,1]
# ]
# ```

class Solution:
    def createNewRow(self, row):
        newRow = []
        for i in range(len(row)):
            if(i==0):
                newRow.append(row[i])
            else:
                newRow.append(row[i-1] + row[i])
        return newRow + [1]
    

    def generate(self, A):
        if(A<1):
            return []
            
        triangle = [[1]]
        if (A==1):
            return triangle

        for i in range(0,A-1):
            triangle.append(self.createNewRow(triangle[i]))

        return triangle




