'''
55. Jump Game
Solved
Medium
Topics
Companies

You are given an integer array nums. You are initially positioned at the array's first index,
 and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.


Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what.
 Its maximum jump length is 0, which makes it impossible to reach the last index.

Constraints:

    1 <= nums.length <= 104
    0 <= nums[i] <= 105

Seen this question in a real interview before?
1/4
Yes
No
Accepted
1.7M
Submissions
4.3M
Acceptance Rate
38.6%
Topics
Array
Dynamic Programming
Greedy
'''
#we are doing greedy approach
class Solution(object):
    def canJump(self, nums):
        goal_post=len(nums)-1 #setting the goal post
        #instead of jumping from front we are going in reverse for greedy solution
        for i in range(len(nums)-1,-1,-1): #moving the goal post 1 by 1 and going in reverse to see whether we can reach the front ie(1 in case of nums)or index 0
            if i +nums[i]>=goal_post:
                goal_post=i
        return True if goal_post==0 else False #if we can reach index 0 it means we can reach the end

nums = [2,3,1,1,4]
nums1 = [3,2,1,0,4]
soln=Solution()
print(soln.canJump(nums))
print(soln.canJump(nums1))

'''Approaching problems like the "Jump Game" involves leveraging a specific strategy often used in algorithmic problem-solving called "Greedy" or "Optimization" strategy. Here's a breakdown of steps to help think in that direction:
1. Understand the Problem:

    Problem Description: Understand the problem statement thoroughly, especially the constraints, input format, and the specific goal.

2. Identify Key Insights:

    Patterns or Requirements: Look for patterns in the problem that might hint at a specific approach. In the "Jump Game," the goal is to reach the end using the maximum possible jumps.

3. Break Down the Approach:

    Goal-Oriented Analysis: In this case, reaching the last index is the goal. Consider working backward or forward based on the problem requirements.

4. Formulate a Strategy:

    Greedy Strategy: For optimization problems, try to maximize or minimize something. In this case, maximizing the jump range to cover more ground is essential.

5. Iterate and Optimize:

    Looping Approach: Iterate through the elements or positions, making decisions to optimize towards the goal.

6. Implement and Verify:

    Code Step-by-Step: Translate the strategy into code, checking at each step if it aligns with the problem's objective.

7. Validate and Adjust:

    Test Cases: Run test cases to verify correctness and efficiency. Adjust the approach if needed based on edge cases or unexpected outcomes.

8. Refine and Optimize:

    Efficiency Improvements: Evaluate if there are ways to optimize the code or algorithm for better performance without sacrificing correctness.

9. Practice and Learn:

    Problem Solving Practice: Regularly practice solving different types of problems to strengthen this approach. Analyze and understand solutions from others.

Example for "Jump Game":

    Insight: Realize that from each position, you want to jump to the position that brings you closer to the last index.

    Greedy Approach: At each step, choose the maximum jump that gets you closer to the goal.

    Code Strategy: Use a loop to iterate backward, checking if, from the current position, a jump can reach the goal or surpass it.

By breaking down the problem and following these strategies, it's possible to approach problems with a more systematic and optimized mindset, which often leads to efficient solutions like the one in the "Jump Game."
'''