import tkinter.messagebox
from pathlib import Path
from tkinter import *
from loginLib import __armazenarLogin as armazenarLogin
from loginLib import __autenticaLogin as autenticaLogin
import linecache
import main

class Application:
    def __init__(self, master=None):

        caminhoAcessos = Path("acessos.txt")

        if caminhoAcessos.is_file():
            if int(linecache.getline("acessos.txt", 1)) >= 1:
                self.fontePadrao = ("Arial", "10")

                self.c1 = Frame(master)
                self.c1["pady"] = 10
                self.c1.pack()

                self.c2 = Frame(master)
                self.c2["padx"] = 20
                self.c2.pack()

                self.c3 = Frame(master)
                self.c3["padx"] = 20
                self.c3.pack()

                self.titulo = Label(self.c1, text="Download Follow-Up")
                self.titulo["font"] = ("Arial", "10", "bold")
                self.titulo.pack()

                self.labelLogoff = Label(self.c3, text="Logoff")
                self.labelLogoff["font"] = self.fontePadrao
                self.labelLogoff.place(relx=1, rely=1, anchor="ne")

                self.btnEntrar = Button(self.c2, font=self.fontePadrao, width=15, height=2, text="Baixar")
                self.btnEntrar.config(command=main)
                self.btnEntrar.pack()

        else:
            self.fontePadrao = ("Arial", "10")

            self.c1 = Frame(master)
            self.c1["pady"] = 10
            self.c1.pack()

            self.c2 = Frame(master)
            self.c2["padx"] = 20
            self.c2.pack()

            self.c3 = Frame(master)
            self.c3["padx"] = 20
            self.c3.pack()

            self.c4 = Frame(master)
            self.c4["pady"] = 20
            self.c4.pack()

            self.titulo = Label(self.c1, text="Dados do usuário")
            self.titulo["font"] = ("Arial", "10", "bold")
            self.titulo.pack()

            self.labelUsuario = Label(self.c2, text="Usuário:", font=self.fontePadrao)
            self.labelUsuario.pack(side=LEFT)

            self.entryUsuario = Entry(self.c2, font=self.fontePadrao, width=30)
            self.entryUsuario.pack(side=LEFT, pady=10)

            self.labelSenha = Label(self.c3, text="Senha:", font=self.fontePadrao)
            self.labelSenha.pack(side=LEFT, padx=3)

            self.entrySenha = Entry(self.c3, font=self.fontePadrao, width=30, show="*")
            self.entrySenha.pack(side=LEFT)

            self.btnEntrar = Button(self.c4, font=self.fontePadrao, width=15, height=2, text="Armazenar login")
            self.btnEntrar.config(command=self.registraLogin)
            self.btnEntrar.pack()



    def registraLogin(self):
        usuario = self.entryUsuario.get()
        senha = self.entrySenha.get()
        resAutenticacao = autenticaLogin(usuario, senha)
        if resAutenticacao == "Login autenticado com sucesso!":
            armazenarLogin(usuario, senha)
            self.entryUsuario.delete(0, END)
            self.entrySenha.delete(0, END)
            tkinter.messagebox.showinfo(title="Informação", message="Login armazenado com sucesso!")
        elif resAutenticacao == "Nome de usuário ou senha incorretos.":
            tkinter.messagebox.showinfo(title="Alerta!", message="Usuário ou senha incorretos, favor inserir os dados novamente.")
        else:
            tkinter.messagebox.showinfo(title="Alerta!", message="Ocorreu um erro inesperado, favor tentar novamente mais tarde.")
root = Tk()
root.geometry("600x250")
root.eval("tk::PlaceWindow . center")
Application(root)
root.mainloop()