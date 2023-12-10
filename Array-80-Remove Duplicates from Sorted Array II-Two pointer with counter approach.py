'''80. Remove Duplicates from Sorted Array II
Solved
Medium
Topics
Companies

Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}

If all assertions pass, then your solution will be accepted.



Example 1:

Input: nums = [1,1,1,2,2,3]
Output: 5, nums = [1,1,2,2,3,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

Example 2:

Input: nums = [0,0,1,1,1,1,2,3,3]
Output: 7, nums = [0,0,1,1,2,3,3,_,_]
Explanation: Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).



Constraints:

    1 <= nums.length <= 3 * 104
    -104 <= nums[i] <= 104
    nums is sorted in non-decreasing order.

Seen this question in a real interview before?
1/4
Yes
No
Accepted
735.8K
Submissions
1.3M
Acceptance Rate
56.0%
Topics
Array
Two Pointers'''
class Solution:
    def removeDuplicates(self,nums):
        l=0
        r=0
        while r<len(nums):
            count = 1#count should be initiliazed within while loop because while in 2nd iteration count will get resetted
            #count should be 0 but 1 initialiazed bcos of for loop used down
            while r+1 <len(nums) and nums[r]==nums[r+1]: #r+1 <len(nums)=>edge case to not go out of bounce
                r+=1
                count+=1
            for i in range(min(2,count)): #this min(2,count) is important to calculate how many 1 or 2 or 3
                # ie how many repetations are there and we have to allow only
                #numbers 2 times to be repeated so we use min(2,count)
                nums[l]=nums[r]
                l+=1
            r+=1
        return l,nums

nums = [1,1,1,2,2,3]
nums1 = [0,0,1,1,1,1,2,3,3]
soln=Solution()
print(soln.removeDuplicates(nums))
print(soln.removeDuplicates(nums1))