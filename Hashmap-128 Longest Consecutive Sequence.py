'''128. Longest Consecutive Sequence
Medium

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Constraints:

    0 <= nums.length <= 105
    -109 <= nums[i] <= 109

'''
def longestconsecutive(nums):
    hashmap=set(nums) #copying nums to our hashmap set
    longest=0
    for n in nums:
        if n-1 not in hashmap: #it means this is the start of the sequence
            length=0
            while (n+length) in hashmap: #if start of sequence found then go for each number by number to check for longest sequences
                length+=1
            longest=max(longest,length)
    return longest

nums = [100,4,200,1,3,2]
a=longestconsecutive(nums)
print(a)

nums = [0,3,7,2,5,8,4,6,0,1]
a=longestconsecutive(nums)
print(a)

