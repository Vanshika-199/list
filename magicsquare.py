a=[[8,3,4],[1,5,9],[6,7,2]]
i=0
r1=0
r2=0
r3=0
c1=0
c2=0
c3=0
d1=0
while i<len(a):
    r1=r1+a[0][i]
    r2=r2+a[1][i]
    r3=r3+a[2][i]
    c1=c1+a[i][0]
    c2=c2+a[i][1]
    c3=c3+a[i][2]
    d1=d1+a[i][i]
    d2=d2+a[i][i-i]
    i=i+1
if r1==r2 and r2==r3 and r1==c1 and c1==c2 and c2==c3 and c1==d1 and d1==d2:
    print("a is a magic square")
else:
    print("a is not a magic square")



#MAGIC SQUARE