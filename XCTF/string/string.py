from pwn import *
context(arch='amd64',os='linux',log_level='debug')
io=remote('111.200.241.243',60102)
io.recvuntil('secret[0] is')
v4_addr=io.recvuntil('\n')
print(v4_addr)
io.interactive()

