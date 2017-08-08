from pwn import *
file=open('rev50_dict','r').read()#strings rev50 > rev50_dict
dict=file.splitlines()
found=0
for word in dict:
    p=process(['./rev50',word])
    if "Good" in p.recv():
        print word
        break
    
