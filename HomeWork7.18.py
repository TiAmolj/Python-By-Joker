# 1
import math
r = float(input('输入五边形顶点到中心的距离：'))
s = 2*r*(math.sin(math.pi/5))
Area = 5*s*s/(4*math.tan(math.pi/5))
print('The area of the pentagon is %.2f'%Area)