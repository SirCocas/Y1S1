import base64
import os
from Crypto.Cipher import AES
import secrets
import time
import random
import string

from saes import saes



timeaes=None
timesaes=None


for i in range(100000):
    key = secrets.token_urlsafe(16)[:16]
    
    aes = AES.new(key, AES.MODE_ECB)
    s = saes(key, secrets.token_urlsafe(16))

    toCipher = [''.join(random.choices(string.ascii_letters+string.digits,k=16)) for i in range(256)]
    start = time.time()
    for l in range(256):
        s.decrypt(s.encrypt(toCipher[l]))
    end=time.time()
    tmp = end-start
    
    if (timesaes == None or tmp<timesaes):
        timesaes = tmp

    start = time.time()
    for l in range(256):
        aes.decrypt(aes.encrypt(toCipher[l]))
        
    end=time.time()
    tmp = end-start
    
    if (timeaes == None or tmp<timeaes):
        timeaes = tmp
    
print("Least time used with SAES: "+ str(timesaes))
print("Least time used with AES: "+ str(timeaes))
