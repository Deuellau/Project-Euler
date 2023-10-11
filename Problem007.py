def Problem007():
    
    n = 10000     
    while True: 
        is_Prime = [True] * (n + 1)
        is_Prime[0] = is_Prime[1] = False
        
        for i in range(2, int(n**0.5)+1):
            if is_Prime[i]:
                for j in range(i*i, n, i):
                    is_Prime[j] = False
        
        primes = []
        for i in range(0, n+1):
            if is_Prime[i]:
                primes.append(i)
        
        if len(primes) > 10001:
            break
        else:
            n += 10000
        
    return primes[10001]


print(Problem007()) # 104759