def Problem002():
   
    n = 13195
    
    is_Prime = [True] * (n+1)
    is_Prime[0] = is_Prime[1] = False

    for i in range(2, int(n**0.5)):
        if is_Prime[i]:
            for j in range(i*i, n, i):
                is_Prime[j] = False

    primes = []
    for i in range(0, n):
        if is_Prime[i]:
            primes.append(i)
            
    return primes


print(Problem002()) # 4613732
    
    
