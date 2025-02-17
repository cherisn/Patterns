class Solution8:
    def ReverseTree(self,n):
        for i in range(n,0,-2):
            print(" "*((n-i)//2)+"*"*i + " "*((n-i)//2))

solution8=Solution8()
solution8.ReverseTree(15)