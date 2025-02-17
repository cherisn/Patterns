class Solution:
    def printTriangle(self,N):
        for i in range(N+1):
            for j in range(1,i+1):
                print(i,end=' ')
            print()

solution=Solution()
solution.printTriangle(9)

class Solution:
    def printTriangle(self, N):
        for i in range(1, N + 1):  # Start from 1 to N
            for j in range(i):  # Print i times
                print(i, end=" ")  # Print i instead of j
            print()  # Move to the next line

# Example Usage
solution = Solution()
solution.printTriangle(9)


class Solution4:
    def printTriangle(self, N):
        for i in range(1, N + 1):  # Start from 1
            for j in range(1, i + 1):  # Loop correctly
                print(i, end=" ")  # Print i
            print()  # Move to next line

# Example Usage
solution4 = Solution4()
solution4.printTriangle(9)