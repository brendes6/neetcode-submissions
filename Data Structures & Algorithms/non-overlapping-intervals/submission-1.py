class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """ Classic intervals problem. The intuition is to sort all intervals
        obviously, but the real catch is that we need to sort by the second value in the 
        intervals. by sorting by end, we are able to pick ones that save the most room for future intervals.
        Since the criteria for picking is that the new start is >= old end, we want the new end
        to be as small as possible to save room.

        """
        if len(intervals) == 1:
            return 0


        intervals = sorted(intervals, key=lambda x: x[1]) # sort by end time

        cur_start, cur_end = intervals[0][0], intervals[0][1]
        replacements = 0

        for s, e in intervals[1:]:
            if s >= cur_end:
                cur_start, cur_end = s, e
            else:
                # if they do overlap, add a replacement
                replacements += 1

        return replacements