class Solution9:
    def Rhombus(self,n):
        for i in range(1,n+1,2):
            print(" "*((n-i)//2)+"*"*i+" "*((n-i)//2))
            
        for j in range(n-1,0,-2):
            print(" "*((n-j)//2)+"*"*j+" "*((n-j)//2))

solution9=Solution9()
solution9.Rhombus(10)