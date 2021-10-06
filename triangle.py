a = int(input("andaze zele 1 ra vared konid: "))
b = int(input("andaze zele 2 ra vared konid: "))
c = int(input("andaze zele 3 ra vared konid: "))
sum1 = b+c
sum2 = a+c
sum3 = a+b
if (a<=sum1 and b<=sum2 and c<=sum3):
    print('You can make a triangle')
else:
    print('You can\'t make a triangle')