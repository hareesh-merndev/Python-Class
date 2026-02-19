# class Solution:
#     def singleNumber(self, nums: list[int]) -> int:
#         result = 0
#         for num in nums:
#             result ^= num
#         return result


# if __name__ == "__main__":
#     nums = list(map(int, input("Enter numbers separated by space: ").split()))
#     sol = Solution()
#     print("Single number is:", sol.singleNumber(nums))
# # anagram

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = {}
        for char in s:
            count[char] = count.get(char, 0) + 1
        for char in t:
            if char not in count or count[char] == 0:
                return False
            count[char] -= 1
        return True

    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        first, second = 1, 2
        for _ in range(3, n + 1):
            first, second = second, first + second
        return second

# --- Run examples ---
if __name__ == "__main__":
    sol = Solution()
    
    # Anagram check
    s = input("Enter first string: ")
    t = input("Enter second string: ")
    if sol.isAnagram(s, t):
        print(f'"{t}" is an anagram of "{s}"')
    else:
        print(f'"{t}" is NOT an anagram of "{s}"')

    # Climbing stairs examples
    n1 = 2
    n2 = 5
    print(f"Ways to climb {n1} steps: {sol.climbStairs(n1)}")
    print(f"Ways to climb {n2} steps: {sol.climbStairs(n2)}")








