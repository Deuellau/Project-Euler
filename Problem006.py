def Problem006():
    
    sumsquare = 0
    sumnums = 0
    for num in range(1, 101):
        sumsquare += num**2
        sumnums += num
    
    return sumnums**2 - sumsquare
 

print(Problem006()) # 25164150