class Solution:
    def climbStairs(self, n):
        if n <= 2:
            return n
        
        prev_1 = 1
        prev_2 = 2
        
        for _ in range(3, n + 1):
            current = prev_1 + prev_2
            prev_1 = prev_2
            prev_2 = current
        
        return prev_2


# Example usage
n = 3

solution = Solution()
result = solution.climbStairs(n)

print("Number of distinct ways to climb to the top:", result)