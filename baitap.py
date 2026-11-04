#Bai2
s =input()
print("hello",s)

# Bai3
a,b= map(int ,input().split())
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
print(f"{a/b:.2f}")

# Bai4
a1,b1,c1,a2,b2,a3 = map(int ,input().split())
print(f"{((a1+b1+c1)+(a2+b2)*2+a3*3)/10:.1f}")

# Bai5
a,b= map(int ,input().split())
print(a**b)

# Bai6
s=input()
print(ord(s))
print(upper(s))

# Bai7
print(((13**2)*3)+5)
print(13**2*3+5)

# Bai8
a=float(input())
print(f"{9/5*a+32:.2f}")

# Bai9
x=float(input())
print(f"{x*0,3+x*0,1+10+x:.2f}")

# Bai10
s=input("nhapten ")
s_split=s.split(sep=" ")
print("hello",s_split[2],s_split[1],s_split[0]) 

# Bai11
a,b= map(int ,input().split())
print(a*60*60+b*60)

# Bai12
a = int(input())
print(a*a*6)

# Bai13
a,b= map(int ,input().split())
print((a%10*b%10)%10)

# Bai14
a,b=map(int ,input().split())
c=a
a=b
b=c
print (a,b)

# Bai15
n= int(input())
print(6*n*(n-1)+1)

# Bai16
print("Spring")
print("Summer")
print("Auttum")
print("Winter")

# Bai17
print("*")
print("**")
print("***")

# Bai18
print("###","##  ","###","###")
print(" # ","# # "," # "," # ")
print(" # ","#  #"," # "," # ")
print(" # ","# # "," # "," # ")
print(" # ","##  "," # "," # ")

# Bai19
print("Monday")
print("Tuesday")
print("Wednesday")
print("Thursday")
print("Friday")
print("Saturday")
print("Sunday")

# Bai20
print("January")
print("February")
print("March")
print("April")
print("May")
print("June")
print("July")
print("August")
print("September")
print("October")
print("November")
print("December")

# Bai21
n=int(input())
for i in range (1,n):
    print("hello world")