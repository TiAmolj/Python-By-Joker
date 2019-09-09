""" 1.
c=float(input('请输入一个摄氏度：'))
f=c*1.8+32
print('%.1f摄氏温度转换为华氏温度%.1f'%(c,f)) """   # 注释：shift+alt+a


# 2.
# import math
# r=float(input('输入圆柱的半径：'))
# h=float(input('输入圆柱的高：'))
# area=float(r*r*math.pi)
# volume=float(area*h)
# print('the area is %.4f'%area)
# print('the volume is %.1f'%volume)

#3.
# feet=float(input('输入一个英尺数：'))
# meters=float(feet*0.305)
# print('%.1f feet is %.4f meters '%(feet,meters))

#4.
# M=float(input('请输入以千克计算的水量：'))
# IT=float(input('请输入水的初始温度：'))
# FT=float(input('请输入水的最终温度：'))
# Q=float(M*(FT-IT)*4184)
# print('所需的能量为：%.1f'%Q)

#5.
# balance,rate = eval(input('Enter balance,  rate :'))
# interest=float(balance*(rate/1200))
# print('The interest is %.5f'%interest)

#6.
# v0,v1,t = eval(input('Enter v0, v1 and t：'))
# a=(v1-v0)/t
# print('the avergea acceleration is %.4f'%a)

#7.
#方法一：
# money = float(input('Enter the monthly saving amount :')) 
# sum=0
# for i in range(6):
#     sum = (sum+money)*(1+0.00417)
# print ('After the sixth month, the account value is %.2f'%sum)
#方法二：
# saving = float(input("Enter the monthly saving amount:"))
# num=0
# while num < 6:
#     account = saving * (1 + 0.00417)
#     saving = account
#     saving += 100
#     num += 1
# print("After the sixth month, the account value is %f "%account)


#8.
# num = int(input('请输入1-1000之间的整数：'))
# baiwei=num//100
# shiwei=num%10
# gewei=num//10%10
# sum=baiwei+shiwei+gewei
# print('各位数之和： ',sum)


#9.水仙花数
# num = input('请输入一个数：')
# baiwei = int(num[0])
# shiwei = int(num[1])
# gewei = int(num[2])
# sum = baiwei**3 + shiwei**3 + gewei**3
# if sum==int(num):
#     print('这个数是水仙花数')
# else:
#     print('这个数是水仙花数')

#10.输入一个年份，判断是否是闰年
# y=int(input('输入年份：'))
# if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
#     print('是闰年')
# else:
#     print('不是闰年')




#输入一个月份计算有几天
# a = eval(input('请输入月份：'))
# while not(isinstance(a, int) and 0<a<13):
#     a = eval(input('请输入正确的月份：'))
# da = [1,3,5,7,10,12]
# xiao = [4,6,8,9,11]
# if (a in da):
#     print(a,'月有31天')
# elif (a in xiao):
#     print(a,'月有30天')
# else:
#     n=eval(input('请输入月所在年：'))
#     if  n%400==0 or (n%4==0 and n%100!=0):
#         print(n,'年为闰年',a,'月有29天')
#     else:
#         print(n,'年为平年',a,'月有28天')




        

#11.#输入一个月判断有多少天
# mouth=int(input('输入月份：'))



#12#华氏温度转化为摄氏温度
# F = float(input('请输入华氏度：'))
# C=(F-32)/1.8
# print('%.2f华氏温度转为摄氏温度为 %.2f' %(F,C))


# 13.将字符串转换为列表
# a = "[[1,2], [3,4], [5,6], [7,8], [9,0]]"
# print(type(a))
# b = eval(a)
# print(type(b))
# print(b)


# 14.字符串转化为字典
# a = "{1:'a',2:'b'}"
# print(type(a))
# b = eval(a)
# print(type(b))
# print(b)


# 15.字符串转换成元组
# a = "([1,2], [3,4], [5,6], [7,8], [9,0])"
# print(type(a))
# b = eval(a)
# print(type(b))
# print(b)


#16.提取出每一个数
# email='123@qq.com'
# for e in email:
#     print(e)


#17.转换成二进制-3
# email='123@qq.com'
# for e in email:
#     o=ord(e)-3
#     print(o)   



# 将字母转换为数字
# a='b'
# print(ord(a))



a=100.0
b=str(a)
print(b,type(b))




#18.转换成ASCII码之后在将ASCII转换成字符串
# email='123@qq.com'
# for e in email:
#     o=ord(e)
#     print(chr(o))



# 19.输入一个数的积
# num1=int (input ('请输入一个数字'))
# num2=int(input('请输入另一个数字'))
# ji=num1*num2
# print ('%d*%d=%d'%(num1,num2,(num1*num2)))


#20.取字符串

# a='joker is a good man'
# print(a[18])  #print(a[-1]) length-1 取出最后一个字符n
# print(a[0:4]) #切片是一个前闭后开的区间
# print(a[-8:-4])
# print(a[11:15]) #[start:end:step)
# print(a[::-1])  #取反，倒序
# print(a[0:5:2]) #步长为2
# print('ok' not in a)  # in是判断在容器中（可迭代对象）有没有这个东西
# print('ok' in a)
# print('jk' in a)



# md5加密
# import hashlib
# m=hashlib.md5()
# a=input('请输入字符串：')
# m.update(bytes(a,encoding='utf8'))
# m.update(b'123')
# print(m.hexdigest())





#21.
# a=True
# b=False
# print(a is not b)



# 22.


#21.输入一个数字判断是奇数还是偶数
# num = int(input('输入一个数字:' ))
# if (num % 2 == 0):
#     print('偶数')
# else:
#     print('奇数')



#22.如果今天是星期六，那么10天以后是星期几？提示：每个星期的第0天是星期天
# s = int(input('请输入今天是星期几：'))
# w = (s+10)%7
# print('十天以后是星期：%d'%w)



#23.输入一个秒数，写一个程序将其转换成分和秒：例如500秒等于8分20秒
# num=int(input('请输入一个秒数：'))
# minute=int(num/60)
# s=int(num%60)
# print('%d秒等于%d分%d秒'%(num,minute,s))



# 24.
