class Solution:
    def mySqrt(self, x):
        if x == 0:
            return 0
        
        left, right = 1, x
        
        while left <= right:
            mid = left + (right - left) // 2
            sqrt = x // mid  # Using integer division
            
            if sqrt == mid:
                return mid
            elif sqrt < mid:
                right = mid - 1
            else:
                left = mid + 1
        
        # If the exact square root is not found, return the floor value
        return right


# Example usage
x = 16

solution = Solution()
result = solution.mySqrt(x)

print("Square root of", x, "is:", result)