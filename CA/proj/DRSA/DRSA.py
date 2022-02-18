import math 

def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)


class random_RSA:

    def get_d(self):
        return pow(self.e, -1, lcm(self.p-1,self.q-1))

    def __init__(self, p, q):
        

        self.p = p
        self.q = q

        self.N = self.p*self.q
        
        
        self.e = 2**16 + 1

        
        self.d = self.get_d()
