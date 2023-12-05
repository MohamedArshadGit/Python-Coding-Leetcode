'''1089. Duplicate Zeros
Easy
Topics
Companies
Hint

Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written. Do the above modifications to the input array in place and do not return anything.



Example 1:

Input: arr = [1,0,2,3,0,4,5,0]
Output: [1,0,0,2,3,0,0,4]
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]

Example 2:

Input: arr = [1,2,3]
Output: [1,2,3]
Explanation: After calling your function, the input array is modified to: [1,2,3]


Constraints:

    1 <= arr.length <= 104
    0 <= arr[i] <= 9

'''
class Solution:
    def duplicateZeros(self,arr):
        zeros=arr.count(0)
        max_len=len(arr)
        for i in range(max_len-1,-1,-1):
            if (i+zeros)<max_len:
                arr[i+zeros]=arr[i] #move the elements to the right considering the number of zeros
            if arr[i]==0: #if we reach 0
                zeros-=1 #decrement the zeros by 1
                if i+zeros < max_len:
                    arr[i+zeros]=0 # Insert 0 at the new position after shifting elements
        print(arr)

arr = [1,0,2,3,0,4,5,0]
arr1 = [1,2,3]
soln=Solution()
soln.duplicateZeros(arr)
soln.duplicateZeros(arr1)