#QUESTION NO.1

a=[1,2,3]
b=len(a)
if b==0:
    print("empty")
else:
    print("not empty")

#QUESTION NO.2

num=int(input("enter the number"))
i=1
b=[]
while i<=num:
    j=1
    c=[]
    while j<=10:
        c.append(i*j)
        j=j+1
    b.append(c)
    i=i+1
print(b)

#QUESTION NO.3

a=list(input("enter the first list"))
b=list(input("enter the second list"))
a.sort()
b.sort()
print(a)
print(b)
if a==b:
    print("same")
else:
    print("not same")


#QUESTION NO.4

a=[1,2,3,4,5,6]
i=0 
even=[]
odd=[]
while i<len(a):
    if a[i]%2==0:
        even.append(a[i])
    else:
        odd.append(a[i])
    i=i+1
print(even)
print(odd)


#QUESTION NO.5


a=[9,2,7,2,3,4]
i=0
sum=0
b=[]
s=[]
while i<len(a):
	j=-1
	while j>=-len(a):
		if a[i]:
			sum=a[i]+a[j]
			b.append(sum)
			if b[i] not in s:
				s.append(b[i])
		j-=1
		i+=1
print(s)