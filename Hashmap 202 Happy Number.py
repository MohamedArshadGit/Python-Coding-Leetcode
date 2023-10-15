'''202. Happy Number

Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

    Starting with any positive integer, replace the number by the sum of the squares of its digits.
    Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
    Those numbers for which this process ends in 1 are happy.

Return true if n is a happy number, and false if not.

Example 1:

Input: n = 19
Output: true
Explanation:
12(square 1 square) + 92 = 82 1^2 +9^2=82
82 + 22 = 68 #same for all
62 + 82 = 100
12 + 02 + 02 = 1

Example 2:

Input: n = 2
Output: false

Constraints:
    1 <= n <= 231 - 1
'''


class Solution(object):
    def isHappy(self, n):
        repeat = set()  # create set to see if number is repeated ,if repeated means we will return False
        while n not in repeat:  # if it is in our repeat set we can return False immediately,if not we will add to repeat set
            repeat.add(n)
            n = self.sumofSquares(n)  # create a function to calculate sum of square and to calculate next number
            # eg 1+9 =82 then store in repeat set then 8+2 square=68
            if n == 1:  # if it is 1 return true
                return True
        return False

    def sumofSquares(self, n):
        output = 0
        while n:
            digit = n % 10  # i already did that in easy sums but this is very important look into this how to do
            # modulo and division properly
            # digit=digit**2
            output = output + digit ** 2
            n = n // 10
        return output


n=19
#n = 2
solution = Solution()
result = solution.isHappy(n)
print(result)
