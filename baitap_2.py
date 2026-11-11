
#BAI 1
n=int(input())
if 100<=n<=999:
while n!=0:
    print(n%10)
    n=n//10
else:
print("Khong xu ly")

#BAI2
a,b=map(int,input().split())
a=a^b
b=a^b
a=a^b
print(a,b)

#BAI3
n=int(input())
if n>0 and (n&(n-1))==0:
    print("Yes")
else:
    print("No")

#BAI4
a,b=map(float,input().split())
print(round(a/b+0.4,2))

#BAI5
a,b=map(float,input().split())
print(round(a/b-0.5,2))

#BAI6
x=int(input())
if x%2==0:
    print("Even")
else:
    print("Odd")

#BAI7
a,b=map(int,input().split())
if a<0 and b<0:
    print("Yes")
else:
    print("No")

#BAI8
a=input()
b=input()
if len(a)>len(b):
    print("True")
else:
    print("False")

#BAI9
a,b,c=map(int,input().split())
if a>0 and b>0 and c>0 and a+b>c and a+c>b and b+c>a:
    print("Yes")
else:
    print("No")

#BAI10
a,b,c,d=map(int,input().split())
max=a
if b>max:
    max=b
if c>max:
    max=c
if d>max:
    max=d
print(max)

#Bai11
a,b,c=map(int,input().split())
if a>=0 or b>=0 or c>=0 or a+b>=c or a+c>=b or b+c>=a:
    print("Tam giac thuong")
elif a==b and b==c:
    print("Tam giac deu")
elif a==b or a==c or b==c:
    print("Tam giac can")
else:
    print("Khong phai tam giac")

#BAI12
n=int(input())
if (n%4==0 and n%100!=0) or n%400==0:
    print("Yes")
else:
    print("No")

#BAI13
a,b=map(float,input().split())
if a==0 and b==0:
        print("Vo so nghiem")
elif b==0:
        print("Vo nghiem")
else:
    print(f"{-b/a:.2f}")
