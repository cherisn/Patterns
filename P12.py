"""
class Solution12:
    def Vnum(self,n):
        for i in range(1,n+1):
            for j in range(1,i+1):
                print(str(i)+"-"*((n-i)*2)+str(j))
solution12=Solution12()
solution12.Vnum(5)
"""

class Solution12:
    def Vnum(self, n):
        for i in range(1, n + 1):
            # Left side numbers
            for j in range(1, i + 1):
                print(j, end="")

            # Spaces in the middle
            spaces = (2 * (n - i))
            print(" " * spaces, end="")

            # Right side numbers
            for j in range(i, 0, -1):
                print(j, end="")

            # Move to the next line
            print()

# Example usage
solution12 = Solution12()
solution12.Vnum(5)