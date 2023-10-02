'''11. Container With Most Water
Medium

There will be a Graph it doesn't copy

You are given an integer array height of length n.
There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Example 1:

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example 2:

Input: height = [1,1]
Output: 1

Constraints:

    n == height.length
    2 <= n <= 105
    0 <= height[i] <= 104

'''

#BRUTE FORCE O(n^2) -Does not works in Leetcode
def maxArea(height):
    res=0
    for l in range(len(height)): #left pointer
        for r in range(l+1,len(height)): #right pointer atleast needs to be 1 step away
            area=(r-l)*min(height[l],height[r]) #formula for finding area rectangle=length*width length[(r-l)]*width
            res=max(res,area)
            #print(res)
    return res

height = [1,8,6,2,5,4,8,3,7]
a=maxArea(height)
print(a)

#Linear Solution O(n)-Two Pointer Technique -Works in leetcode
def maxarea(height):
    l=0
    r=len(height)-1
    res=0
    while l<r:
        area=(r-l)*min(height[l],height[r])
        #print(area)
        res=max(res,area)
        #print(res)
        if height[l]<height[r]:
            l+=1 #moving left pointer to right coz small
        elif height[r]<height[l]:
            r-=1 #moving right pointer to left coz small
        else:
            r-=1 #if both the values are same like in diagram 8 at index 1 and  8 at index 6
    return res

b=maxarea(height)
print(b)