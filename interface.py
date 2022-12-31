from tkinter import *
from usuarios import Users


class Applicacao:
    def __init__(self, master=None):
        self.c1 = Frame(master)
        self.c1['padx'] = 15
        self.c1['pady'] = 5
        self.c1.pack()
        self.c2 = Frame(master)
        self.c2['pady'] = 5
        self.c2['padx'] = 15
        self.c2.pack()
        self.c3 = Frame(master)
        self.c3['pady'] = 5
        self.c3['padx'] = 15
        self.c3.pack()
        self.c4 = Frame(master)
        self.c4['pady'] = 5
        self.c4['padx'] = 15
        self.c4.pack()
        self.c5 = Frame(master)
        self.c5['pady'] = 5
        self.c5['padx'] = 15
        self.c5.pack()
        self.c6 = Frame(master)
        self.c6['pady'] = 5
        self.c6['padx'] = 15
        self.c6.pack()
        self.c7 = Frame(master)
        self.c7['pady'] = 5
        self.c7['padx'] = 15
        self.c7.pack()
        self.c8 = Frame(master)
        self.c8['pady'] = 5
        self.c8['padx'] = 15
        self.c8.pack()
        self.c9 = Frame(master)
        self.c9.pack()


        self.lbTitle = Label(self.c1, text='Insira os dados', font=('Verdana', 9, 'bold'))
        self.lbTitle.pack()

        self.lbId = Label(self.c2, text='Id: ')
        self.lbId.pack(side=LEFT)
        self.vId = Entry(self.c2, width=5)
        self.vId.pack(side=LEFT)
        self.bntId = Button(self.c2, text='ID', width=5)
        self.bntId['command'] = self.selecionarusuario
        self.bntId.pack(side=LEFT)

        self.lbNome = Label(self.c3, text='Nome: ')
        self.lbNome.pack(side=LEFT)
        self.vNome = Entry(self.c3)
        self.vNome.pack(side=LEFT)

        self.lbIdade = Label(self.c4, text='Idade: ')
        self.lbIdade.pack(side=LEFT)
        self.vIdade = Entry(self.c4)
        self.vIdade.pack(side=LEFT)

        self.lbCidade = Label(self.c5, text='Cidade: ')
        self.lbCidade.pack(side=LEFT)
        self.vCidade = Entry(self.c5)
        self.vCidade.pack(side=LEFT)

        self.lbtelefone = Label(self.c6, text='Telefone: ')
        self.lbtelefone.pack(side=LEFT)
        self.vTelefone = Entry(self.c6)
        self.vTelefone.pack(side=LEFT)

        self.lbEmail = Label(self.c7, text='E-mail: ')
        self.lbEmail.pack(side=LEFT)
        self.vEmail = Entry(self.c7)
        self.vEmail.pack(side=LEFT)

        self.btnIserir = Button(self.c8, text='INSERIR', width=12)
        self.btnIserir['command'] = self.inserirUsuarios
        self.btnIserir.pack(side=LEFT)
        self.btnAtualizar = Button(self.c8, text='ATUALIZAR', width=12)
        self.btnAtualizar['command'] = self.atualizarUsuario
        self.btnAtualizar.pack(side=LEFT)
        self.btnExcluir = Button(self.c8, text='EXCLUIR', width=12)
        self.btnExcluir['command'] = self.excluirUsuario
        self.btnExcluir.pack(side=LEFT)

        self.lbMessage = Label(self.c9, text='', font=('Arial', 12, 'bold'))
        self.lbMessage.pack()

    def inserirUsuarios(self):
        user = Users()
        user.nome = self.vNome.get()
        user.idade = self.vIdade.get()
        user.cidade = self.vCidade.get()
        user.telefone = self.vTelefone.get()
        user.email = self.vEmail.get()
        self.lbMessage['text'] = user.insertUser()

        self.vNome.delete(0, END)
        self.vIdade.delete(0, END)
        self.vCidade.delete(0, END)
        self.vTelefone.delete(0, END)
        self.vEmail.delete(0, END)

    def atualizarUsuario(self):
        user = Users()
        user.id = self.vId.get()
        user.nome = self.vNome.get()
        user.idade = self.vIdade.get()
        user.cidade = self.vCidade.get()
        user.telefone = self.vTelefone.get()
        user.email = self.vEmail.get()
        self.lbMessage['text'] = user.updateUser()

        self.vNome.delete(0, END)
        self.vIdade.delete(0, END)
        self.vCidade.delete(0, END)
        self.vTelefone.delete(0, END)
        self.vEmail.delete(0, END)

    def excluirUsuario(self):
        user = Users()
        user.id = self.vId.get()
        self.lbMessage['text'] = user.deleteUser()
        self.vId.delete(0, END)
        self.vNome.delete(0, END)
        self.vIdade.delete(0, END)
        self.vCidade.delete(0, END)
        self.vTelefone.delete(0, END)
        self.vEmail.delete(0, END)

    def selecionarusuario(self):
        user = Users()
        id = self.vId.get()
        self.lbMessage['text'] = user.selectUser(id)


        self.vId.delete(0, END)
        self.vId.insert(INSERT, user.id)
        self.vNome.delete(0, END)
        self.vNome.insert(INSERT, user.nome)
        self.vIdade.delete(0, END)
        self.vIdade.insert(INSERT, user.idade)
        self.vCidade.delete(0, END)
        self.vCidade.insert(INSERT, user.cidade)
        self.vTelefone.delete(0, END)
        self.vTelefone.insert(INSERT, user.telefone)
        self.vEmail.delete(0, END)
        self.vEmail.insert(INSERT, user.email)

app = Tk()
app.title('Cadastro Simples')
Applicacao(app)
app.mainloop()
