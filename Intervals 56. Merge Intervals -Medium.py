'''56. Merge Intervals
Solved
Medium
Topics
Companies

Given an array of intervals where intervals[i] = [starti, endi],
 =>important-merge all overlapping intervals, and return an array of the non-overlapping intervals
  that cover all the intervals in the input.

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

Constraints:

    1 <= intervals.length <= 104
    intervals[i].length == 2
    0 <= starti <= endi <= 104

'''

def merge(intervals):
    intervals.sort(key=lambda i:i[0]) #we need to sort sublist of each ,here already sorted so no issue ,
    # but if it is sorted luke [[2,6],[1,3]] output will become like [[1,3],[2,6]]
    #[[1,3],[2,6],[8,10],[15,18]]
    output=[intervals[0]]

    for start,end in intervals[1:]: #we already stored 1st sublist in output so start from 1st index
        lastend=output[-1][1] #this is very very very important we are storing end value of oth index in sublist

        if start<=lastend: #if 1st index sublist start value less tan last end means its OVERLAPPING SO ADD IT
            output[-1][1]=max(lastend,end)
        else:
            output.append([start,end]) #else add it as it is
    return output

intervals = [[1,3],[2,6],[8,10],[15,18]]
#Output: [[1,6],[8,10],[15,18]]
a=merge(intervals)
print(a)
print()
intervals = [[1,4],[4,5]]
a=merge(intervals)
print(a)