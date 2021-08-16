from pwn import *

print(b"0xdeadbeef")
print(p64(int(b"0xdeadbeef",16)))