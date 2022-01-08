from pwn import *

for i in range(50):
	p = process("./prog_1")
	p.recvuntil(b':\n')
	p.sendline(b'A'*i)
	r=p.recvline()
	p.close()
	print(i,r)
	print("---")