#coding: utf-8
'''
class Complex:
     def __init__(self, real, imag):
        self.r = real
        self.i = imag

# instantiation 类的实例
x = Complex(2.0, -4.5)
## 创建了一个新的obj，同时调用__init__初始化

print x.r
print x.i
'''
class Dog():

    def __init__(self, name):
        self.name = name
        self.tricks = []

    def add_trick(self, trick):
        self.tricks.append(trick)

fido = Dog('Fido')
tim = Dog('Tim')

fido.add_trick("play dead")
tim.add_trick("roll over")

print fido.tricks
