'''Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.

Example 1:

Input: nums = [3,2,3]
Output: 3

Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2

Constraints:

    n == nums.length
    1 <= n <= 5 * 104
    -109 <= nums[i] <= 109


Follow-up: Could you solve the problem in linear time and in O(1) space?'''

def majority_element(nums):
    max_value=0
    max_count=0
    count={}
    for n in nums:
        count[n]=1+count.get(n,0)
        print(count)
        print(count[n])
        max_value=[n if count[n]>max_count else max_value]
        max_count=max(count[n],max_count)
    return max_value

nums=[2,2,1,1,1,2,2]
a=majority_element(nums)
print(a)















'''def majority_element(nums):
    count={}
    High_value,max_count=0,0

    for n in nums:
        count[n]=1+count.get(n,0)
        print(count[n])
        High_value= [n if count[n]>max_count else High_value]
        max_count=max(count[n],max_count)
    return High_value


nums=[2,2,1,1,1,2,2]
a=majority_element(nums)
print(a)'''






'''Certainly, let's go through the 5th and 6th points in more detail:

    count[n] = 1 + count.get(n, 0): This line is responsible for updating the count
     of the number n in the count dictionary.
      It uses the .get() method to retrieve the current count of n in the dictionary. 
      Here's a detailed breakdown:

        count[n]: This is the dictionary key used to access the count associated with the number n.
         If n is not already a key in the dictionary, this operation will raise a KeyError.
          That's where .get(n, 0) comes in.

        .get(n, 0): This method checks if the key n exists in the dictionary.
         If it does, it returns the associated value (which is the count of n). 
         If it doesn't exist, it returns the default value of 0. So, if n is not in the dictionary,
          it initializes the count to 0, and if it's already in the dictionary, 
          it retrieves the existing count.

        1 + count.get(n, 0): This part increments the count by 1.
         If n is already in the dictionary, it retrieves the existing count and adds 1 to it.
          If n is not in the dictionary, it starts with a count of 0 and adds 1 to it, 
          effectively initializing the count for n to 1.

    res = n if count[n] > max_count else res: This line is intended to update the res variable
     based on the count of the current number n. Let's break it down:

        count[n]: This part retrieves the count of the current number n from the count dictionary.
         It represents how many times n has been encountered in the input list nums.

        count[n] > max_count: This part compares the count of n with the current maximum count stored
         in the max_count variable. If the count of n is greater than the maximum count seen so far,
          it evaluates to True. Otherwise, it evaluates to False.

        n if count[n] > max_count else res: This is a conditional expression.
         If the count of n is greater than max_count,
          it assigns the value of n to the res variable.
           Otherwise, it assigns the current value of res to res.
            This effectively updates res to hold the number that has the highest count seen so far.

The purpose of these lines (5 and 6) is to keep track of the potential majority element
 in the input list nums. As the loop iterates through the list and encounters different numbers,
  it updates the count of each number and checks if the count of the current number is greater
   than the count of the previously seen potential majority element.
    If so, it updates res to the current number. At the end of the loop,
     res should contain the number with the highest count, which is the potential majority element.'''

