import sys
from saes import saes

key = ""
sk = ""

if(len(sys.argv)==2):
    key=sys.argv[1]
    sk=None

elif len(sys.argv) == 3:
    key = sys.argv[1]
    sk = sys.argv[2]
else:   
    print("USAGE: python3 decrypt.py KEY [SHUFFLING KEY]")
    exit()

if(len(key)<16):
    print("Key "+str(key)+" is too short! Make sure it has 16 characters.")
    exit()
elif(len(key)>16):
    print("Key "+str(key)+" is too long! Therefore, the key used will be "+key[:16])

if(sk!= None and len(sk)<16):
    print("Shuffling key "+str(sk)+" is too short! Make sure it has 16 characters.")
    exit()
elif(sk!= None and len(sk)>16):
    print("Shuffling key "+str(sk)+" is too long! Therefore, the shuffling key used will be "+sk[:16])

if(sk!=None):
    s=saes(key, sk)
else:
    s=saes(key)

text = input("Insert the text you wish to decrypt: \n")
if(len(text)%16 != 0):
    print("ATTENTION: your input isn't compatible with the cipher, are you sure this is valid?")
    exit()
print("Plaintext as characters: ")
print(s.decrypt(text))
print("Plaintext as an integer list")
print(s.result)
