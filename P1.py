
class Solution:
    def printSquare(self, N):
        # Code here
        for i in range(1,N+1):
            for j in range(1,N+1):
                print ('*',end=' ')
            print()
solution = Solution()
solution.printSquare(9) 