class Solution1:
    def PrintStar(self,N):
        print("\nPattern 1\n")
        for i in range(1,N+1):
            for j in range(1,N+1):
                print('*',end=' ')
            print()
        print("\nPattern 2\n")
soluiton1=Solution1()
soluiton1.PrintStar(15)

class Solution2:
    def PrintTriangle(self,N):
        for i in range(1,N+1):
            for j in range(1,i+1):
                print('*',end=" ")
            print()
        print("\nPattern 3\n")
solution2=Solution2()
solution2.PrintTriangle(15)

class Solution3:
    def TriangleNums(self,N):
        for i in range(1,N+1):
            for j in range(1,i+1):
                print(j,end=" ")
            print()
        print("\nPattern 4\n")
solution3=Solution3()
solution3.TriangleNums(15)

class Solution4:
    def TriangleSame(self,N):
        for i in range(1,N+1):
            for j in range(1,i+1):
                print(i,end=" ")
            print()
        print("\nPattern 5\n")
solution4=Solution4()
solution4.TriangleSame(15)

class Solution5:
    def ReverseTriangleStar(self,n):
        for i in range(1,n+1):
            for j in range(n-i+1):
                print("*",end=" ")
            print()
        print("\nPattern 6\n")
soluiton5=Solution5()
soluiton5.ReverseTriangleStar(15)

class Solution6:
    def ReverseTriangleNum(self,n):
        for i in range(n,0,-1):
            for j in range(1,i+1):
                print(j,end=" ")
            print()
        print("\nPattern 7\n")
soluiton6=Solution6()
soluiton6.ReverseTriangleNum(15)

class Solution7:
    def PrintTree(n):
        for i in range(1,n+1,2):
            print(" "*((n-i)//2)+("*"*i)+" "*((n-i)//2))
        print()
        print("\nPattern 8\n")
Solution7.PrintTree(15)

class Solution8:
    def ReverseTree(self,n):
        for i in range(n,0,-2):
            print(" "*((n-i)//2)+ "*"*i+" "*((n-i)//2))
       # print()
        print("\nPattern 9\n")
soluiton8=Solution8()
soluiton8.ReverseTree(15)

class Solution9:
    def Rhombus(self,n):
        for i in range(1,n+1,2):
            print(" "*((n-i)//2)+"*"*i+" "*((n-i)//2))
        for j in range(n,0,-2):
            print(" "*((n-j)//2)+"*"*j+" "*((n-j)//2))
        print("\nPattern 10\n")
soluiton9=Solution9()
soluiton9.Rhombus(15)

class Solution10:
    def sideTriangle(self,n):
        for i in range(1,n+1):
            print("*"*i+" "*(n-i))
        for j in range(n-1,0,-1):
            print("*"*j+" "*(n-j))
        print("\nPattern 11\n")
solution10=Solution10()
solution10.sideTriangle(15)

class Solution11:
    def BinNum(self,n):
        for i in range(1,n+1):
            for j in range(i):
                if j%2==0:
                    print("1",end="")
                else:
                    print("0",end="")
               # print("1" if j % 2 == 0 else "0", end="")
            print()
        print("\nPattern 12\n")
solution11=Solution11()
solution11.BinNum(15)
        
