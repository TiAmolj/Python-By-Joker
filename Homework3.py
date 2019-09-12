# 1.
# def getPentagonalNumber(n):
#     count = 0
#     for i in range(1,n+1):
#         sum = int(i * (3 * i - 1) / 2)
#         print(sum,'\t',end=" ")
#         count += 1
#         if count % 10 ==0:
#             print("")
# getPentagonalNumber(100)


# 2.
# def sumDigits(n):
#     a = n // 100
#     b = n // 10 % 10
#     c = n % 10
#     sum = a + b + c
#     print(sum)
# sumDigits(234)

# 3.
# def displaySortedNumbers(num1,num2,num3):
#     num1,num2,num3 = map(float,input('请输入三个整数：').split(','))
#     x = [num1,num2,num3]
#     x.sort()
#     print('The sorted number are ',x)
# displaySortedNumbers(5, 12.5 , 9)

# 4.
# import math
# def faulterInvestmentValue(investmentAmount,mouthlyInterestRate,year):
#     # invest_A = input('The amount invested:')
#     # rate = input('Annual interest rate:')
#     # year = input('输入年：')
#     year_rate = mouthlyInterestRate * 12 
#     for i in range(1,year+1):
#         sum = investmentAmount * (1+year_rate)
#     # for i int range(1,year+1):
#     print(sum)
# faulterInvestmentValue(10000,0.05,50)    



#  5.
# count = 0
# def printChars(ch1,ch2,numberPerLine):
#     global count
#     for i in range(49,91):
#         print(chr(i),end = '')
#         count += 1
#         if count % numberPerLine == 0:
#             print()
# printChars(49,91,10)



# 6.
# def number0fDaysInAYear():
#     for year in range(2010,2021):
#         if year % 4 ==0 and year % 100 != 0 or year % 400 == 0:
#             print('%d年有366天'%year)
#         else:
#             print('%d年有365天'%year)
# number0fDaysInAYear()


# 7.
# def distance(x1,y1,x2,y2):
#     d=((x1 - x2) ** 2 + (y1 - y2) ** 2) * 0.5
#     print('%.2f'%d)
# distance(3,3,5,5)


# 8.
# def ms():
#     for i in range(2,32):
#         for j in range(2,i):
#             if i % j == 0:
#                 break
#         else:
#             for p in range(i+1):
#                 if(2**p) -1 == i:
#                     print('%d %d'%(p,i))
# ms()


# 11.
import random
num1 = random.randint(1,6)
num2 = random.randint(1,6)
sum = num1+num2
if sum in (2,3,12):
    print('You rolled %d + %d = %d'%(num1,num2,sum))
    print('You lose!') 
elif sum in (7,11):
    print('You rolled %d + %d = %d'%(num1,num2,sum))
    print('You win!') 
else:
    sum1=num1+num2
    if sum == sum1:
        print('You rolled %d ' %(sum),'You win!',end='\n')
        print('Point is ',sum1)
    else:
        print('You rolled %d ' %(sum),'You lose!',end='\n')    
        print('Point is ',sum1)








