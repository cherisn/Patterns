

class Solution7:
    def PrintTree(self, n):
        for i in range(1, n + 1,2):
            
            print(" " *((n-i)//2)+"*"*(i)+" "*((n-i)//2))

solution7 = Solution7()
solution7.PrintTree(10)
