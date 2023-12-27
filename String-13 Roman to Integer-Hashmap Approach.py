class Solution(object):
    def romanToInt(self, s):
        roman={
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        res=0
        for i in range(len(s)):
            if i+1<len(s) and roman[s[i]] < roman[s[i+1]]:
                res=res-roman[s[i]] #if previous values is less than next value we should minus it refer my note
            else:
                res=res+roman[s[i]]
        return res


s = "III"
s1 = "LVIII"
s2 = "MCMXCIV"
soln=Solution()
print(soln.romanToInt(s))
print(soln.romanToInt(s1))
print(soln.romanToInt(s2))
