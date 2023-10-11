def Problem007():
    
    with open('problem007.txt', 'r') as file:
        number_str = file.read().strip()

        number = ''.join(number_str.splitlines())

    n = 13
    largest = 0
    for i in range(0, len(number)-n):
        product = 1
        for j in range(i, i+n):
            product *= int(number[j])
        
        if product > largest:
            largest = product
            
    return largest
    

print(Problem007()) # 23514624000