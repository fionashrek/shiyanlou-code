i = 1
while i <= 100:
    if i%7==0 or i//10==7 or (i+3)%10==0:
        pass
    else:
        print(i)
    i+=1
