class Solution:
    def lengthOfLastWord(self, nums):
        
        for i in range (len(nums)):
          if nums[i] == " ":
            n = 0
          else:
            n += 1
            f = n 

        return f 

# Example usage
nums = "  full moon  "


solution = Solution()
position = solution.lengthOfLastWord(nums)

print("Position:", position)