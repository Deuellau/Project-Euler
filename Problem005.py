def Problem005():
    
    results = []
    div = 2
    
    for num in range(2, 21):
        factors = []
        while div <= num:
            if num % div == 0:
                factors.append(div)
                num /= div
            else:
                div += 1
        div = 2
        results.append(factors)
            
            
    counts = {}
    for numfactors in results:
        for num in numfactors:
            if num not in counts or numfactors.count(num) > counts[num]:
                counts[num] = numfactors.count(num)
                
                
    output = 1
    for key, values in counts.items():
        output *= key**values


    return output


print(Problem005()) # 232792560