a=int(input('enter no.'))
i=1
while i<a:
    j=1
    b=[]
    while j<=10:
        if i%j==0:
            print(j)
            b.append(j)
        j+=1
    i+=1