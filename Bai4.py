# Bai tap tuan 4
# Bai1
n=int(input())
sum=0
for i in range(1,n+1):
    sum+=i
print(sum)

#Bai2
def prime(a):
  if(a<2):return False
  for i in range(2,a):
     if(a%i==0):return False
  return True

a=int(input())
while(a<0):
  a=int(input())
print(prime(a)) 

#Bai3
n=int(input())
sum=0
for i in range(1,n+1):
    sum*=i
print(sum)

#Bai4
n=int(input())
cnt=0
if(n==0):dem=1
while(n>1 or n<-1):
  cnt+=1
  n/=10
print(cnt)

#Bai5
n=int(input())
for i in range(n):
  a=int(input())
  if(a==42):
    print("I've found the meaning of life!")
    break
else:
  print("It's a joke!")

#Bai6
def prime(a):
  if(a<2):return False
  for i in range(2,a):
    if(a%i==0):return False
  return True

while True:
  try:
    a,b=map(int,input().split())
    s=0
    for i in range(a,b+1):
      if(prime(i)):s+=i
    print(s)
  except:
    break

#Bai7
n=int(input())
i=2
while(i*i<=n):
  while(n%i==0):
    n//=i
  i+=1
print(n)

#Bai8
def reverse(n):
  sum=0
  while(n>0):
    sum=sum*10+n%10
    n//=10
  return sum

n=int(input())
dem=0
while(n!=reverse(n)):
  n+=reverse(n)
  dem+=1

print(dem)
print(n)

#Bai9
n=int(input())
for i in range(1,n**0.5+1):
  x=i*i
  if(len(set(str(x)))==len(str(x))):
    print(x,end=" ")
    break
else:
  print("(no number)")

#Bai10
n=int(input())
max=0
res=1
for i in range(1,n+1):
  x=i
  dem=1
  while(x!=1):
    if(x%2==0):
      x//=2
    else:
      x=3*x+1
    dem+=1
  if(dem>max):
    max=dem
    res=i

print(res,max)

#Bai11
n=int(input())
dem=0
for i in range(2,n+1,2):
  if(n%i==0):dem+=1
print(dem)

#Bai12
x,n=map(int,input().split())
s=x
for i in range(n):
  s*=1.007
print(int(s))

#Bai13
def sumdiv(n):
  s=0
  for i in range(1,n):
    if(n%i==0):s+=i
  return s

a,b=map(int,input().split())
if(sumdiv(a)==b and sumdiv(b)==a):
  print("true")
else:
  print("false")

#Bai14
def gcd(m,n):
  while(n!=0):
    m=n
    n=m%n
  return m

m,n=map(int,input().split())
print(gcd(m,n))

#Bai15
n,m=map(int,input().split())
for ga in range(n+1):
  cho=n-ga
  if(2*ga+4*cho==m):
    print(ga,cho)
    break
else :
  print("invalid")
