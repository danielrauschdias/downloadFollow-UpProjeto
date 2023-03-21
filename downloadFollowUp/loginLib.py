import pywintypes
import win32security

from cryptography.fernet import Fernet

def __gerarChaveCriptografica():
    chave = Fernet.generate_key()
    chaveLogin = open("chaveLogin.key", "wb")
    chaveLogin.write(chave)
    chaveLogin.close()

def __criptografarDados(texto):
    chaveLogin = open("chaveLogin.key", "rb")
    chave = chaveLogin.read()
    chaveLogin.close()
    f = Fernet(chave)
    return f.encrypt(texto.encode())

def __descriptografarDados(texto):
    chaveLogin = open("chaveLogin.key", "rb")
    chave = chaveLogin.read()
    chaveLogin.close()
    f = Fernet(chave)
    return (f.decrypt(texto).decode())

def __armazenarLogin(usuario, senha):
    dadosLogin = open("dadosLogin.txt", "wb")
    dadosLogin.write(__criptografarDados(usuario + "\n" + senha))
    dadosLogin.close()

def __descriptografarLogin():
    dadosLogin = open("dadosLogin.txt", "rb")
    login = __descriptografarDados(dadosLogin.read()).split("\n")
    dadosLogin.close()
    return login

def __autenticaLogin(usuario, senha):
    try:
        win32security.LogonUser(usuario, "LIDER", senha, win32security.LOGON32_LOGON_NETWORK, win32security.LOGON32_PROVIDER_DEFAULT)
    except pywintypes.error as e:
        erro = str(e).replace("(","").replace(")","").replace(" '", "").replace("'", "").split(",")
        return (erro[2])
    else:
        return "Login autenticado com sucesso!"







