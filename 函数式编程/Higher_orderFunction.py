# encoding:utf-8
# 高阶函数

# 1.函数可以赋值给变量，相当于起了个别名
f = abs
print f(-10)
# 10

# 2.函数名本质上就是指向函数的变量

# 3.既然变量可以指向函数，函数的参数能接收变量，
# 那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数。
def add(x, y, f):
    return f(x) + f(y)

print add(-5,6,abs)
# 11