import getpass #biblioteca para solicitar senha ao usuário sem armazena-la
import telnetlib

HOST = "192.168.122.72" #entra com ip adress do roteador
user = input("Enter your remote account: ")
password = getpass.getpass() #solicita ao usuário para entrar com senha

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"enable\n")
tn.write(b"cisco\n") #apenas por questão de teste foi implantada esta linha, futuras atualizações removarão senhas e usuários do script
tn.write(b"conf t\n")
tn.write(b"int loop 0\n")
tn.write(b"ip address 1.1.1.1 255.255.255.255\n")
tn.write(b"int loop 1\n")
tn.write(b"ip address 2.2.2.2 255.255.255.255\n")
tn.write(b"router ospf 1\n")
tn.write(b"network 0.0.0.0 255.255.255.255 area 0\n")
tn.write(b"end\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))