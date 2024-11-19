from typing import List

class Solution:
  def permute(self, nums: List[int]) -> List[List[int]]:
      result = []

      def backtrack(current, idx):
          if idx == len(nums):
              result.append(current)
              return

          # the current number is nums[idx]
          # we must consider placing it at each possible index
          # however we cannot "overwrite" any idex which has already been filled...
          for pos in range(len(nums)):
              if current[pos] is None:
                  cpy = current.copy()
                  cpy[pos] = nums[idx]
                  backtrack(cpy, idx+1)


      backtrack([None]*len(nums), 0)
      return result
