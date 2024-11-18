class Solution:
    def swap(self, nums, i, j):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp

    def partition(self, nums, low, high):
        # choose the right most index as pivot element
        pivot = nums[high]
        
        # i keeps track of the boudndary of the elements that are smaller
        # than the pivot. When we find a new element that is smaller than the 
        # pivot, we will swap that element to i+1 because i+1 is the first element
        # that may be greater than or equal to the pivot
        i = low - 1
        
        for j in range(low, high):
            if nums[j] < pivot:
                i += 1
                self.swap(nums, i, j)
        
        # at this point everything from low to i should be smaller
        # than the pivot so we just need to swap pivot to the i+1
        # position. now everything to the left of pivot is smaller than it
        # and everything to the right of pivot is greater than or equal to pivot
        self.swap(nums, i + 1, high)
        return i + 1
            

    def quickSort(self, nums, low, high):
        if low < high:
            # partition the array around a pivot index
            pivot_index = self.partition(nums, low, high)
            
            # the pivot element is now in its final sorted position
            # we recursively sort everything to the left of the pivot
            # index and everything to the right of the pivot index
            self.quickSort(nums, low, pivot_index - 1)
            self.quickSort(nums, pivot_index + 1, high)

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.quickSort(nums, 0, len(nums) - 1)
