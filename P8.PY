"""
class Solution8:
    def ReverseTree(n):
        for i in range(1,n+1):
            print(" "*((n-i//2)),end=" ")
            for j in range(0,n+1,2):
                print("*"*(j))
            print()
Solution8.ReverseTree(7)



class Solution8:
    @staticmethod
    def ReverseTree(n):
        for i in range(n, 0, -1):  # Start from n and go to 1 (reverse order)
            print(" " * (n - i) + "* " * i)  # Print stars with proper spacing

# Call the static method directly without creating an instance
Solution8.ReverseTree(7)

"""

class Solution8:
    def ReverseTree(n):
        for i in range(n, 0, -1):  # Start from n and go to 1 (reverse order)
            print(" " * (n - i) + "* " * i)  # Print stars with proper spacing

# Call the static method directly without creating an instance
Solution8.ReverseTree(7)
                      
class Solution8:
    def ReverseTree(self,n):
        for i in range(n,0,-2):
            print("-"*((n-i)//2)+"*"*i + "-"*((n-i)//2))

solution8=Solution8()
solution8.ReverseTree(15)