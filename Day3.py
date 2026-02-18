# fibonacci series
# a, b = 0, 1
# while a < 10:
#     print(a, end=' ')
#     a, b = b, a + b
# # for leet
# class Solution:
#     def fib(self, n: int) -> int:
#         if n == 0:
#             return 0
#         if n == 1:
#             return 1
        
#         a, b = 0, 1
#         for _ in range(2, n + 1):
#             a, b = b, a + b
        
#         return b

        
a, b, c = 0, 1, 1
while a < 30:
    print(a, end=' ')

    a, b, c = b, c, a + b + c
# for leeet
class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        
        a, b, c = 0, 1, 1
        
        for _ in range(3, n + 1):
            a, b, c = b, c, a + b + c
        
        return c
