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
tn.write(b"vlan 2\n")
tn.write(b"name Python_VLAN_2\n")
tn.write(b"vlan 3\n")
tn.write(b"name Python_VLAN_3\n")
tn.write(b"vlan 4\n")
tn.write(b"name Python_VLAN_4\n")
tn.write(b"vlan 5\n")
tn.write(b"name Python_VLAN_5\n")
tn.write(b"vlan 6\n")
tn.write(b"name Python_VLAN_6\n")
tn.write(b"vlan 7\n")
tn.write(b"name Python_VLAN_7\n")
tn.write(b"vlan 8\n")
tn.write(b"name Python_VLAN_8\n")
tn.write(b"end\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))