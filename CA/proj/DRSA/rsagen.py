import DRSA
import json
from sympy import *


def get_primes_until(x):
    primes = [3]
    while(1):
        tmp = nextprime(primes[-1])
        if tmp >x:
            break
        else:
            primes.append(tmp)
    
    return primes

def has_small_prime_factors(n, primes):
    if(n<max(primes)):
        return True
    for i in primes:

        if(n%i == 0):
            return True
    return False
        




while(True):
    try:
        p = int.from_bytes(bytes(input()[:20],'ascii'), "little", signed=False)
        break
    except:
        continue

while(True):
    try:
        q = int.from_bytes(bytes(input()[:20], 'ascii'), "little", signed=False)
        break
    except:
        continue

PRIMES = get_primes_until(100)

while(1):

    #sometimes input stalls when it comes to the random generator, so instead of relying on it forever, we only need 2 numbers from it!
    
    if(p==q):
        q = nextprime(p+q)
    p_1 = p - 1
    q_1 = q - 1
    if(not has_small_prime_factors(p_1, PRIMES) and not has_small_prime_factors(q_1, PRIMES)):
        break
    p = nextprime(p)
    q = nextprime(q)

print("p and q have been generated")

drsa = DRSA.random_RSA(p,q)


public = {
    'N' : str(drsa.N),
    'e' : str(drsa.e)
}


private = {
    'N' : str(drsa.N),
    'd' : str(drsa.d)
}

json_object_public = json.dumps(public, indent=4)

with open("public.json", "w") as outfile:
    outfile.write(json_object_public)

json_object_private = json.dumps(private, indent=4)

with open("private.json", "w") as outfile:
    outfile.write(json_object_private)

print("Files have been created!")