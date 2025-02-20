'''class Solution:
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
        
        
        
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums) - 1): 
            if nums[i] == nums[i + 1]:  
                return True  
        return False





arr = []
for i in range(3):
  inp = input()
  con = int(inp)
  arr.append(con)

dup = False 

for i in range(len(arr)):
  for j in range(len(arr)-i-1):
    if arr[i] == arr[j+i+1]:
      dup = True 
      break
if dup == True:
  print("Duplicate found")
else:
  print("No duplicate found")
  
  
  '''
  