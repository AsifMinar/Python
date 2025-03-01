'''
n = [1,2]
n.sort()

def missing_number(n):
  for i in range(len(n)):
    if i != n[i]:
      if n[0] == 1:
        f = i
        break
      f = i
      break
    else:
      f = i+1
  return f

print(missing_number(n))

'''

#from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int: # type: ignore
        nums.sort()
        for i in range(len(nums)):
            if i != nums[i]:
                if nums[0] == 1:
                    f = i
                    break
                f = i
                break
            else:
                f = i+1
        return f


