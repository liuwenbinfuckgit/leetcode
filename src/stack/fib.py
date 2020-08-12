class Solution(object):
    def fib(self,n):
        a,b = 0,1
        if n <2:
            return n
        for i in range(n):
            if i >=2:
                temp = a
                a =b
                b= temp+b
        return  (a+b)%1000000007
if __name__ == '__main__':
    solution = Solution()
    print(solution.fib(51))