
class Solution5:
    def ReverseTriangle(self,N):
        for i in range(1,N+1):
            for j in range(N-i+1):
                print('*',end=' ')
            print()

solution5=Solution5()
solution5.ReverseTriangle(5)