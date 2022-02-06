a=[]
size=int(input('e nter size of your list'))
i=1
while i<=(size):
    value=int(input('enter value'))
    a.append(value)
    i+=1
print('original list',a)
print('length',(len(a)))
print('max no.',(max(a)))
print('min no.',(min(a)))
b=a
print('list a',a)
print('list b',b)
count=int(input('enter value count'))
y=a.count(count)
print(count,'appear in list',y ,'times')
n=int(input('enter the value whose index you want to know'))
index=a.index(n)
print(n,'found at',index,'index')
value=int(input('enter the value to insert'))
ind=int(input('enter index'))
a.insert(ind,value)
print(a)
print('original list',a)
a.reverse()
print('reverse list',a)
print(a)
a.sort()
print('sort list',a)
a.pop()
print("last element pop",a)

#ALL FUNCTION IN ONE CODE
