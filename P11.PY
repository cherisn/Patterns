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
solution11=Solution11()
solution11.BinNum(9)
        