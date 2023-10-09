def Problem004():
   
    largest = 0
    for num1 in range(999, 500, -1):
        for num2 in range(999, 500, -1):
            prod = num1*num2
            if str(prod) == str(prod)[::-1]:
                if prod > largest:
                    largest = prod
                   
    return largest


print(Problem004()) # 906609
    
    
