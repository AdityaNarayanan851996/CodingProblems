# Q1) Implement an algorithm to determine if a string has all unique characters. What if you can not use additional data structures?

#code
a = input()
a = a.lower()
a = sorted(a)
l = []
flag = 0 
st = a[0]
print(a)
for i in range(1,len(a)):
    if a[i] in l:
        flag = 1
        break
    else:
        l.append(a[i])

if flag == 1:
    print(False)
else:
    print(True)
    