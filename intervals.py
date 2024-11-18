class Solution:
    def insert(self, intervals, newInterval):
        if not intervals:
            return [newInterval]

        if intervals[0][0] > newInterval[1]:
            # if the first interval starts before new interval ends, 
            # simply append newInterval to the start
            return [newInterval] + intervals

        if intervals[-1][1] < newInterval[0]:
            # if the newInterval starts after the last interval ends,
            # simply append in to the end
            return intervals + [newInterval]

        result = []
        merged_interval = newInterval
        merging = False

        for interval in intervals:
            if not merging and interval[0] <= newInterval[0] <= interval[1] or newInterval[0] <= interval[0] <= newInterval[1]:
                # start of current interval overlaps with newInterval OR start of newInterval overlaps
                # with current interval
                merged_interval[0] = min(interval[0], newInterval[0])
                merging = True
            elif merging and interval[0] <= newInterval[1] <= interval[1] or newInterval[0] <= interval[1] <= newInterval[1]:
                # end of current interval overlaps with newInterval OR end of newInterval overlaps
                # with current interval
                merged_interval[1] = max(interval[1], newInterval[1])
                result.append(merged_interval)
                merging = False
            elif merging and interval[0] > newInterval[1]:
                result.append(merged_interval)
                result.append(interval)
                merging = False
            elif not merging:
                result.append(interval)

        return result 



if __name__ == "__main__":
  solution = Solution()

  print(solution.insert([[1,3],[6,9]], [3,6]))
