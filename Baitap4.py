#Bai1
def Max_Of_Two(a,b):
  if(a>b):return a
  return b

a,b=map(int,input().split())
print(Max_Of_Two(a,b))

#Bai2
def swap(a,b):
  return b,a

a,b=map(int,input().split())
a,b=swap(a,b)
print(a,b)

#Bai3
def prime(a):
  if(a<2):return False
  for i in range(2,a):
    if(a%i==0):return False
  return True

a=int(input())
print(prime(a))

#Bai4
def perfect(n):
  s=0
  for i in range(1,n**0.5):
    if(n%i==0):s=s+i+n/i
    if(i*i==n)s-=i
  return s==n

n=int(input())
print(perfect(n))

#Bai5
a=list(map(int,input().split()))
k=int(input())
vt=-1
for i in range(len(a)):
  if(a[i]==k):
    vt=i
    break
print(vt)

#Bai6
def factor(n):
  s=1
  for i in range(1,n+1):
    s*=i
  return s

n=int(input())
print(factor(n))

#Bai7
def comp(a,b,op):
  if(op=='+'):return round(a+b,2)
  if(op=='-'):return round(a-b,2)
  if(op=='*'):return round(a*b,2)
  if(op=='/'):
    if(b==0):return "invalid"
    return round(a/b,2)

a,b=map(float,input().split())
op=input()
print(comp(a,b,op))

#Bai8
def bit_trans(a):
  str s
  while(a!=0):
    a//=2
    s+=str(a%2)
  return s

a,b=map(int,input().split())
dem=0
sa=bit_trans(a)
sb=bit_trans(b)
if(len(sa)<len(sb))swap(sa,sb)
for i in range(len(sb)):
  if(sa[i]==sb[i]):dem+=1
for i in range(len(sb),len(sa)):
  if(sa[i]=='0'):dem+=1


#Bai9
def sumdigit(n):
  s=0
  while(n>0):
    s+=n%10
    n//=10
  return s

n=int(input())
print(sumdigit(n))

#Bai10
def anhxa(a,b):
  for i in range(len(a)):
    if((ord(a[i])+ord(b[i]))/2!=219/2):return False
  return True

a=input()
b=input()
print(anhxa(a,b))

#Bai11
def is_product_divisible_by_10(a,b):
  return (a*b)%10==0

a,b=map(int,input().split())
print(is_product_divisible_by_10(a,b))

#Bai12
def divide_with_remainder(dividend,divisor):
  q=abs(dividend)//abs(divisor)
  if(dividend*divisor<0):q=-q
  r=dividend-divisor*q
  return q,r

a,b=map(int,input().split())
print(divide_with_remainder(a,b))

#Bai13
def max_of_two(a,b):
  if(a>b):return a
  return b

a,b=map(int,input().split())
print(max_of_two(a,b))

#Bai14
def comp(a,b,op):
  if(op=='+'):return round(a+b,2)
  if(op=='-'):return round(a-b,2)
  if(op=='*'):return round(a*b,2)
  if(op=='/'):
    if(b==0):return "invalid"
    return round(a/b,2)

a,b=map(float,input().split())
op=input()
print(comp(a,b,op))


#Bai15
def is_right_triangle(a,b,c):
  if(a<=0 or b<=0 or c<=0):return False
  if(a+b<=c or a+c<=b or b+c<=a):return False
  x=sorted([a,b,c])
  return x[0]**2+x[1]**2==x[2]**2
#
a,b,c=map(int,input().split())
print(is_right_triangle(a,b,c))
