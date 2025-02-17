"""
class Solution6:
    def ReverseNum(self,N):
        for i in range(1,N+1):
            print(i)
            for j in range(1,N+1):
                print("i=",i,end='\n')
                print("j=",j,end='\n')
                print("Val of J=",j,end=' ')
            print()
solution6=Solution6
solution6.ReverseNum(5)



12345
1234
123
12
1

"""
class Solution6:
    def ReverseNum(self,N):
        for i in range(N,0,-1):
            for j in range(1,i+1):
                print(j,end=' ')
            print()
solution6=Solution6()
solution6.ReverseNum(5)


class Solution:
    def reverseNum(self,N):
        for i in range(N,0,-1):
            for j in range(i,0,-1):
                print(j,end=' ')
            print()
solution=Solution()
solution.reverseNum(5)


class Solution:
    def ReverseTriangle(self, N):
        for i in range(N, 0, -1):  # Start from N down to 1
            spaces = "  " * (N - i)  # Add spaces for right alignment
            print(spaces, end="")  # Print spaces without new line
            for j in range(i, 0, -1):  # Print numbers from i down to 1
                print(j, end=" ")
            print()  # Move to the next line

# Example Usage
solution = Solution()
solution.ReverseTriangle(5)