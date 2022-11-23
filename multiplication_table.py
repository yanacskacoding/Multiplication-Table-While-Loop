
'''Instructions:
Write a program that prints out the multiplication table of the entered number by the user by using whileloop.

Example 1:
>>>
5
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50
'''
#code:

num = int(input())

i = 1
while i <= 10:
    num = num * 1
    print(num, "x", i, "=", num*i)
    i += 1
    