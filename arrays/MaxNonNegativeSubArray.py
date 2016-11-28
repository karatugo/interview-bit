class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
        def getSA(A, i):
            SA = []
            while(i < len(A)):
                if(A[i] >= 0):
                    SA.append(A[i])
                    i += 1
                else:
                    return SA
            return SA

        def getSAs(A):
            SAs = []
            i=0
            while (i < len(A)):
                SA = getSA(A, i)
                if(len(SA) > 0):
                    SAs.append(SA)        
                    i +=len(SA)
                else:
                    i += 1
            return SAs

        def Sum(A) :
            sum = 0
            for a in A:
                sum += a
            return sum

        def getMaxSA(SAs):
            if(len(SAs) == 0):
                return []
            
            MaxSA = SAs[0]
            for i in range(len(SAs)):
                if(Sum(SAs[i]) > Sum(MaxSA)):
                    MaxSA = SAs[i]
                elif (Sum(SAs[i]) == Sum(MaxSA)):
                    if(len(MaxSA) == len(SAs[i])):
                        MaxSA = MaxSA if MaxSA[0] < SAs[i][0] else SAs[i]
                    else:
                        MaxSA = MaxSA if len(MaxSA) > len(SAs[i]) else SAs[i]
            return MaxSA

        SAs = getSAs(A)
        MaxSA = getMaxSA(SAs)
        return MaxSA