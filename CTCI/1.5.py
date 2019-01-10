# Q) Write a method to replace all spaces in a string with ‘%20’.
#code
str = input()
a = ''
for itm in str:
    if itm == ' ':
        a+='%20'
    else:
        a+=itm
print(a)