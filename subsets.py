def subsets(numbers):
        
  def helper(nums):
      if not nums:
          return [[]]

      recur = helper(nums[1:])

      return recur + [r + [nums[0]] for r in recur]
  

  return helper(numbers)


if __name__ == "__main__":
  print(subsets([1,2,3]))
