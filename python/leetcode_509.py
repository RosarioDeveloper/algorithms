class Solution:
    def fib(self, n: int) -> int:
        fib = [0, 1]
        for i in range(2, n):
            fib.append(fib[i - 1] + fib[i - 2])

        return fib


result = Solution().fib(5)
print(result)

