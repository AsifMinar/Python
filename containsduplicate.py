class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dup = False  # Rename 'dup' to 'has_duplicate' for clarity
        for i in range(len(nums)): # Use 'nums' (the input list) instead of 'arr'
            for j in range(len(nums) - i - 1): # Use 'nums' here too
                if nums[i] == nums[i + j + 1]: # Compare elements of 'nums'
                    dup = True # Set 'dup' to True if duplicate is found
                    break # Exit inner loop
            if dup: # Exit outer loop if duplicate is found
                break

        return dup # Return the boolean value 'dup' (True or False)
