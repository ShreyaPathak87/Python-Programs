"""A=[1,23,4,5,6]
A.append(90)
print(A)

B=[5,6,7]
A.extend(B)
print(A)

A.sort()
print(A)
A.sort(reverse=True)
print(A)

A={'name':'Shreya','rollno':18,}
A['name']='pratiksha'
print(A['name'])
print(A)


class person:
 def greet():
    print("hello")
a=person
a.greet()

A=lambda x:x**2

print(A(9))

A=lambda a,b:a+b
print(A(3,5))



a=int(input("Enter number"))
b=int(input("Enter number"))
c=int(input("Enter number"))

if a>b and a>c:
    print("a is largest")
elif b>a and b >c:
    print("b is largest")
else:
    print("c is largest")"""

temp=int(input("Enter temp"))
unit=input("Enter C for celcius , F for fahrenheit ")
C=0
F=0
if unit=="C":
    C+=temp
    print("converting c to f")
    F=(C*9/5)+32
    print("Fahrenheit:",F)
elif unit=="F":
    F+=temp
    C=(F-32)*9/5
    print("celcius:",C)
