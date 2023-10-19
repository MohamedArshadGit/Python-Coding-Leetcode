'''228. Summary Ranges

You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

    "a->b" if a != b
    "a" if a == b

Example 1:

Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"

Example 2:

Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"

Constraints:

    0 <= nums.length <= 20
    -231 <= nums[i] <= 231 - 1
    All the values of nums are unique.
    nums is sorted in ascending order.

'''
def summaryRanges(nums):
    result=[]
    n=len(nums)
    if n==0:#if nums is empty return empty list
        return result
    a=nums[0]
    for i in range(n):
        #print(nums[i]+1,nums[i+1])
        if i==(n-1) or nums[i]+1!=nums[i+1] : #(out of error should not be thrown(THIS IS NORMALLY CALLED AS EDGE CASE) for i+1 so use i==(n-1)#this line
            # very important #this nums[i]+1 is to check whether next number is there eg 2+1 =3
            # is there +next number?no 4 is there instead of 3 so it stops
            # ,next number is 4 so sequence will stop and enter if  loop if not equal
            if nums[i]!=a:#this check for, from the first number if 2nd number sequence is not there it append that number only
                # it will just add 1 number.this is for single sequence number
               result.append(str(a)+"->"+str(nums[i]))
            else:
                result.append(str(a))
            if i!=(n-1):
                a=nums[i+1]
    return result

nums = [0,1,2,4,5,7]
#Output: ["0->2","4->5","7"]
a=summaryRanges(nums)
print(a)
nums = [0,2,3,4,6,8,9]
a=summaryRanges(nums)
print(a)