binary=[1,0,0,1,1,0,1,1]
answer=0
currentdigit=0
currentpower=len(binary)-1
while currentpower>=0:
    place=binary[currentdigit]
    answer=answer+place*2**currentpower
    currentdigit=currentdigit+1
    currentpower=currentpower-1
print(answer)



#BINARY NUMBER