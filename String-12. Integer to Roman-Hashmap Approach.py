class Solution(object):
    def intToRoman(self, num):
        res=""
        roman_list=[["I",1],["IV",4],["V",5],["IX",9],["X",10],["XL",40],["L",50],["XC",90],["C",100],["CD",400],["D",500],["CM",900],["M",1000]]
        #y storing in list? bcos we need to iterate in reverse orderly so we use list here
        for l,n in reversed(roman_list):#y going in reverse bcos we need values to go from highest to lowest
            if num//n: #if it is 0 then skip to lesser number in reverse in roman list
                count=num//n
                res+=(l*count) #eg if 2000 comes means count =2 ,l=m-from roman_list so l*m=2000
                num=num%n
        return res


num=3
num1=58
num2=1994
num3=9
soln=Solution()
print(soln.intToRoman(num))
print(soln.intToRoman(num1))
print(soln.intToRoman(num2))
print(soln.intToRoman(num3))