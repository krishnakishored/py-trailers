# noprimes = [j for i in range(2, 8) for j in range(i*2, 100, i)]
# primes = [x for x in range(2,100) if x not in noprimes]

# print(noprimes)
# print(primes)


from math import sqrt

n = 100
sqrt_n = int(sqrt(n))


#the sieve of Eratosthenes
no_primes = [j for i in range(2, sqrt_n+1) for j in range(i*2, n, i)]
primes = [x for x in range(2,n) if x not in no_primes]
print(no_primes)# lots of double entries - use set comprehension to resolve

no_primes_set = {j for i in range(2, sqrt_n+1) for j in range(i*2, n, i)}
print(no_primes_set)
print(primes)

# Recursive Function to Calculate the Primes
def primes(n):
    if n==0:
        return []
    elif n==1:
        return []
    else:
        p = primes(int(sqrt(n))) # it is enough to examine the multiples of the prime numbers up to the square root of n
        no_p = {j for i in p for j in range(i*2, n+1, i) }
        p = {x for x in range(2, n + 1) if x not in no_p}
    return p


for i in range(1,20):
    print(i, primes(i))