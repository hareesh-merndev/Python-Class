# from typing import List

# class Solution:
#     def generate(self, numRows: int) -> List[List[int]]:
#         triangle = []  
#         for i in range(numRows):
#             row = [1] * (i + 1)
#             for j in range(1, i):
#                 row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

#             triangle.append(row)

#         return triangle
# if __name__ == "__main__":
#     numRows = 5
#     sol = Solution()
#     result = sol.generate(numRows)
#     print(result)


# from typing import List

# class Solution:
#     def getRow(self, rowIndex: int) -> List[int]:
#         row = [1]  
#         for i in range(1, rowIndex + 1):
#             new_row = [1] * (i + 1)
#             for j in range(1, i):
#                 new_row[j] = row[j - 1] + row[j]
#             row = new_row
#         return row
# if __name__ == "__main__":
#     rowIndex = 3
#     sol = Solution()
#     result = sol.getRow(rowIndex)
#     print(result)


# from typing import List

# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         insert_pos = 0
#         for num in nums:
#             if num != 0:
#                 nums[insert_pos] = num
#                 insert_pos += 1
#         while insert_pos < len(nums):
#             nums[insert_pos] = 0
#             insert_pos += 1
# if __name__ == "__main__":
#     sol = Solution()
#     nums = [0, 1, 0, 3, 12]
#     sol.moveZeroes(nums)
#     print(f"Modified array: {nums}")


# class Solution:
#     def isPowerOfFour(self, n: int) -> bool:
#         if n <= 0:
#             return False
        
#         while n % 4 == 0:
#           n //= 4
        
#         return n == 1

# n = int(input("Enter an integer: "))

# solution = Solution()
# if solution.isPowerOfFour(n):
#         print("Output: True")
#         print(f"Explanation: {n} is a power of 4.")
# else:
#         print("Output: False")
#         print(f"Explanation: {n} is not a power of 4.")

# from typing import List

# class Solution:
#     def maximumProduct(self, nums: List[int]) -> int:
#         nums.sort()
#         product1 = nums[-1] * nums[-2] * nums[-3]
#         product2 = nums[0] * nums[1] * nums[-1]
#         return max(product1, product2)
# if __name__ == "__main__":
#     sol = Solution()
#     nums = [1, 2, 3, 4]
#     print("Input:", nums)
#     print("Maximum Product of 3 Numbers:", sol.maximumProduct(nums))
#     arr = list(map(int, input("\nEnter numbers separated by space: ").split()))
#     print("Result:", sol.maximumProduct(arr))


# class Solution:
#     def romanToInt(self, s: str) -> int:
#         roman_map = {
#             'I': 1,
#             'V': 5,
#             'X': 10,
#             'L': 50,
#             'C': 100,
#             'D': 500,
#             'M': 1000
#         }

#         total = 0 
#         for i in range(len(s)):
#             if i + 1 < len(s) and roman_map[s[i]] < roman_map[s[i + 1]]:
#                 total -= roman_map[s[i]]
#             else:
#                 total += roman_map[s[i]]

#         return total


# if __name__ == "__main__":
#     sol = Solution()

#     test_cases = ["III", "IV", "IX", "LVIII", "MCMXCIV"]

#     for s in test_cases:
#         print(f"Input: {s} Output: {sol.romanToInt(s)}")

#     s = input("\nEnter a Roman numeral: ").upper()
#     print("Integer value:", sol.romanToInt(s))


from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        k = 0  
        for i in range(1, len(nums)):
            if nums[i] != nums[k]:
                k += 1
                nums[k] = nums[i]
                return k + 1
if __name__ == "__main__":
    sol = Solution()
    nums = [1, 1, 2]
    k = sol.removeDuplicates(nums)
    print("Unique count (k):", k)
    print("Modified array:", nums[:k]) 
    arr = list(map(int, input("\nEnter sorted numbers separated by space: ").split()))
    k = sol.removeDuplicates(arr)
    print(f"Unique count: {k}")
    print(f"Array after removing duplicates: {arr[:k]}")