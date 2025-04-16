def get_primes(n):
    primes = []
    sieve = [True] * (n+1)
    sieve[0] = sieve[1] = False

    for p in range(2, int(n**0.5) + 1):
        if sieve[p]:
            for i in range(p*p, n+1, p):
                sieve[i] = False

    for p in range(2, n+1):
        if sieve[p]:
            primes.append(p)

    return primes