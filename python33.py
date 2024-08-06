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

tn.write(b"en\n")
tn.write(b"cisco\n") #apenas por questão de teste foi implantada esta linha, futuras atualizações removarão senhas e usuários do script
tn.write(b"conf t\n")

for n in range (2,101):
    tn.write(b"vlan " + str(n).encode('ascii') + b"\n")
    tn.write(b"name Python_VLAN_" + str(n).encode('ascii') + b"\n")

tn.write(b"end\n")
tn.write(b"wr\n") #para salvar a configuração do switch
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))