class Solution10:
    def sideTriangle(self,n):
        for i in range(1,n+1):
            print("*"*i+" "*((n-i)//2))
        for j in range(n-1,0,-1):
            print("*"*j+" "*(n-j))
solution10=Solution10()
solution10.sideTriangle(5)
