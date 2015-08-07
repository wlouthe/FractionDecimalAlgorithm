def FractionCalc(x,y,z=50):
    print("Calculating for",x,"/",y)
    answer = x/y
    #print(answer,"is the answer")
    fraction = (1-y/x)*100
    #print(fraction,"is the percent used")
    total = 0
    #print("Calculating approximate answer based")
    for j in range(1,z+1):
        val = fraction**j/100**(j)
        #print(val)
        total=total+val
        #print("Current total at iteration",j,":",total)
    total = total+1
    print("Original   Total:",answer)
    print("Calculated Total:",total)
        

