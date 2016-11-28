# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @param new_interval, a Interval
    # @return a list of Interval
    def insert(self, intervals, new_interval):
        def isIntersectionEmpty(i1, i2):
            if(i1.end < i2.start or i2.end < i1.start):
                return 1
            else:
                return 0
                
        mergedIntervals = []
        for interval in intervals:
            if(isIntersectionEmpty(interval, new_interval)):
                mergedIntervals.append(interval)
            else:
                aList = [interval.start, interval.end, new_interval.start, new_interval.end]
                new_interval = Interval(min(aList), max(aList))
                
        mergedIntervals.append(new_interval)
        return sorted(mergedIntervals, key=lambda interval: interval.start)
        