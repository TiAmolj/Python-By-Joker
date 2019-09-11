# 1.
# import math
# # a,b,c = map(float,input('Enter a,b,c:').split(','))
# a,b,c = eval(input('Enter a,b,c:'))
# sum=b*b-4*a*c
# if sum >0:
#     r1=(-b+math.sqrt(sum))/2*a
#     r2=(-b-math.sqrt(sum))/2*a
#     print('The roots are %.2f and %.2f'%(r1,r2)) 
# elif sum == 0:
#     r1=r2=(-b+math.sqrt(sum))/2*a
#     print('The root is %.2f'%r1)
# else:
#     print('The equation has no real roots')




# 2.
# import random
# num1 = random.randint(0,100)
# num2 = random.randint(0,100)
# print(num1,num2)
# sum == num1+num2
# sum1 = input('请输入结果：')
# if sum1 == sum:
#     print('结果为真')
# else:
#     print('结果为假')




# 3.
# today = int(input('Enter today is day:'))
# num1 = int(input('Enter the number of days elapsed since today: '))
# week = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
# week1=(today+num1)%7
# print("Today is %s and the future day is %s"%(week[today],week[week1]))


# 4.1
# num1,num2,num3 = eval(input('输入三个数:'))
# if num1 > num2 :
#     if num1 > num3:
#         if num2 > num3:
#             print(num3,num2,num1)
#         else:
#             print(num2,num3,num1)
#     else:
#         print(num2,num1,num3)
# else:
#     if num1 > num3:
#         print(num3,num1,num2)
#     elif num2 > num3:
#         print(num1,num3,num2)
#     else:
#         print(num1,num2,num3)
        
        





# 5.
# w1,p1 = eval(input('Enter weight and price for package 1:'))
# w2,p2 = eval(input('Enter weight and price for package 2:'))
# if p1%w1 < p2% w2:
#     print('Package 1 has the better price.')
# else:
#     print('Package 2 has the better price.')



# 6.
# m,y = eval (input('请输入月份，年份：'))
# if m in (1,3,5,7,8,10,12):
#     print('%s年%s月的天数为31天'%(y,m))
# elif m in (4, 6 ,9,11):
#     print('%s年%s月的天数为30天'%(y,m))
# if m == 2:
#     if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
#         print('%s年2月的天数为29天'%y)
#     else:
#         print('%s年2月的天数为28天'%y)



# 7.
# import numpy as np
# np1 = input('请猜测硬币是正面或是反面：')
# np2 = np.random.choice(['正面' ,'反面'])
# print(np2)
# if np1 == np2:
#     print('恭喜你，答对了！😊')
# else:
#     print('很遗憾，错了呢！😔')



# 8.
# import random
# user = int(input('请选择：scissor(0),rock(1),paper(2):'))
# computer = random.randint(0,2)   #用于生成一个指定范围内的整数
# if user == 0 and computer == 1:
#     print('The computer is rock,You are scissor. You lost.')
# elif user == 0 and computer == 2:
#     print('The computer is paper,You are scissor. You won.')
# elif user == 0 and computer == 0:
#     print('The computer is scissor,You are scissor. It is a draw. ')
# elif user == 1 and computer == 0:
#     print('The computer is scissor,You are rock.You won. ')
# elif user == 1 and computer == 2:
#     print('The computer is paper,You are rock.You lost. ')
# elif user == 1 and computer == 1:
#     print('The computer is rock,You are rock.It is a draw. ')
# elif user == 2 and computer == 0:
#     print('The computer is scissor,You are paper.You lost. ')
# elif user == 2 and computer == 1:
#     print('The computer is rock,You are paper.You won. ')
# elif user == 2 and computer == 2:
#     print('The computer is paper,You are paper.It is a draw.')



9#
# y = int(input('Enter year:'))
# m = int(input('Ether month:1-12:'))
# q = int(input('Ether the day of the month:1-31:'))
# a = ['Saturday' ,'Sunday','Monday','Tuesday','Wednesday','Thurday','Firday']
# if m == 1:
#     m = 13
#     y = y-1
# elif m == 2:
#     m = 14
#     y = y-1
# h = (q + ((26 * (m + 1) // 10)) + (y % 100) + ((y % 100) // 4) + ((y // 100) // 4) + (5 * y // 100)) % 7
# # '//'只输出整数，即只输出小数点前的：'/'输出完整运算结果，即会输出小数点后的：
# D=a[h]
# print('Day of the week is %s'%D)



#10.
# import numpy as np
# np1 = np.random.choice(['Ace',2,3,4,5,6,7,8,9,10,'Jack','Queen','King'])
# np2 = np.random.choice(['梅花' , '红桃' ,'黑桃' ,'方块'])
# print('The card you picked is the %s of %s'%(np1,np2))



# 11.
# num = input('Enter a three-digit integer：')
# if num == num [::-1]:
#     print('%s is a palindrome'%num)
# else:
#     print('%s is not a palindrome'%num)

# 12.
# a,b,c = eval(input('Enter three edges :'))
# if a+b>c and a-b<c:
#     d=a+b+c
#     print('The perimter is:%.0f'%d)


# 1.


#2.
money = 10000
sum = 0 
for i in range(14):
    money = money + money * 0.05
    if i == 9:
        print('十年后的大学的学费是：%.2f'%money)
else:
    print('十年后的大学四年的总学费是：%.2f'%sum)
    



# 4.
# count = 0
# for i in range(100,1001):
#     if i >= 100 and i <= 1000:
#         if i % 5 == 0 and i % 6 == 0:
#             count += 1
#             print(i,"\t",end=' ')
#             if count % 10 == 0:
#                print(" ") 
   



# 5.
# n=1
# while n * n < 1200:
#     n=n+1
# print(n)
# while n * n * n >1200:
#     n=n-1
# print(n)

