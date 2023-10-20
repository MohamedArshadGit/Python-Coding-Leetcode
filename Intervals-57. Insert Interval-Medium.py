'''57. Insert Interval
Medium
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

Constraints:

    0 <= intervals.length <= 104
    intervals[i].length == 2
    0 <= starti <= endi <= 105
    intervals is sorted by starti in ascending order.
    newInterval.length == 2
    0 <= start <= end <= 105

'''
def insert(intervals,newInterval):
    res=[]
    for i in range(len(intervals)):
        if newInterval[1]<intervals[i][0]: #if new interval is before the intervals
            res.append(newInterval)
            return res+intervals[i:] #after putting new interval we can directly add all the interval values
        elif newInterval[0]>intervals[i][1]: #if new interval is next to intervals then we will add before new interval
            res.append(intervals[i])
        else: #if it is overlapping we need to take min and max of both interval and new intervals
            newInterval=[min(intervals[i][0],newInterval[0]),max(intervals[i][1],newInterval[1])]
    res.append(newInterval) #why we append at the end bcos there may be next overlapping intervals so we append at last
    return res

intervals = [[1, 3], [6, 9]]
newInterval = [2, 5]
a=insert(intervals,newInterval)
print(a)

intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]
a=insert(intervals,newInterval)
print(a)