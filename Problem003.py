def Problem003():
    num = 600851475143
    div = 2
    largest = 0
    
    while num >= div:
        if num % div == 0:
            if div > largest:
                largest = div
            num /= div
        
        else:
            div += 1
            
    return largest
        
    
    

print(Problem003()) # 4613732
    
    
