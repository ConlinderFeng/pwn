from pwn import *
context(arch='i386',os='linux',log_level='debug')
io=process('./CGfsb')
elf=ELF('./CGfsb')
io.recvuntil('name:')

