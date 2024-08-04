import getpass #biblioteca para solicitar senha ao usuário sem armazena-la
import telnetlib

HOST = "localhost" #entra com ip adress do roteador
user = input("Enter your remote account: ")
password = getpass.getpass() #solicita ao usuário para entrar com senha

tn = telnetlib.Telnet(HOST)

tn.read_until(b"login: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"ls\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))