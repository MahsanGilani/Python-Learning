# x = int(input("Enter a number: "))
# y = x // 100
# t = (x % 100) // 10
# z = x % 10

# print(x , y , t , z, sep='\n')

# *******************************************************************
# مثال بالارو بصورت زیر هم میشه حلش کرد:
# x = int(input("Enter a number: "))
# temp = x % 10
# print(temp)
# x = x // 10
# temp = x % 10
# print(temp)
# x = x // 10
# temp = x % 10
# print(temp)

# *******************************************************************
"""
    برنامه ای بنویسید که شعاع دایره را از کاربر گرفته و محیط و
    مساحت دایره را حساب کند. 
"""
import math
r = int(input("Enter Shoa: "))
masahat = math.pi * r * r
mohit = 2 * r * math.pi
print(f"Mohit dayereh barabar ast ba: {round(mohit,2)}\nmasahat barabar ast ba: {round(masahat,2)}")