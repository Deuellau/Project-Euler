def Problem010():
    
    n = 2_000_000
    is_Prime = [True] * (n + 1)
    is_Prime[0] = is_Prime[1] = False
    
    for i in range(0, int(n**0.5)):
        if is_Prime[i]:
            for j in range(i*i, n, i):
                is_Prime[j] = False
                
    primes = []
    for i in range(0, n+1):
        if is_Prime[i]:
            primes.append(i)
    
    return sum(primes)

 
print(Problem010()) # 142915828922