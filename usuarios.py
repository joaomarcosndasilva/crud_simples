from banco import Banco
from sqlite3 import Error

class Users(object):
    def __init__(self, id=0, nome='', idade='', cidade='', telefone='', email=''):
        self.info = {}
        self.id = id
        self.nome = nome
        self.idade = idade
        self.cidade = cidade
        self.telefone = telefone
        self.email = email

    def insertUser(self):
        banco = Banco()
        #self.nome = str(input('Nome: '))
        #self.idade = str(input('Idade: '))
        #self.cidade = str(input('Cidade: '))
        #self.telefone = str(input('Telefone: '))
        #self.email = str(input('E-mail: '))
        try:
            c = banco.conexao.cursor()
            c.execute("INSERT INTO usuarios(nome, idade, cidade, telefone, email) VALUES('"+self.nome+"','"+self.idade+"','"+self.cidade+"','"+self.telefone+"','"+self.email+"')")
            banco.conexao.commit()
            c.close()
            return 'Dados inseridos com sucesso'
        except Error as ex:
            print(ex)
            return 'Erro ao inserir'

    def updateUser(self):
        banco = Banco()
        #self.id = str(input('Id: '))
        #self.nome = str(input('Nome: '))
        #self.idade = str(input('Idade: '))
        #self.cidade = str(input('Cidade: '))
        #self.telefone = str(input('Telefone: '))
        #self.email = str(input('E-mail: '))
        try:
            c = banco.conexao.cursor()
            c.execute("UPDATE usuarios SET nome='"+self.nome+"', idade='"+self.idade+"', cidade='"+self.cidade+"', telefone='"+self.telefone+"', email='"+self.email+"' WHERE id='"+self.id+"'")
            banco.conexao.commit()
            c.close()
            return 'Dados atualizados com sucesso'
        except Error as ex:
            print(ex)
            return 'Erro ao atualizar'

    def deleteUser(self):
        banco = Banco()
        #self.id = str(input('ID: '))

        try:
            c = banco.conexao.cursor()
            c.execute("DELETE FROM usuarios WHERE id='"+self.id+"'")
            banco.conexao.commit()
            c.close()
            return 'Deletado com sucesso!'
        except Error as ex:
            print(ex)
            return 'Erro ao deletar'

    def selectUser(self, id):
        banco = Banco()
        try:
            c=banco.conexao.cursor()
            c.execute("SELECT * FROM usuarios WHERE id='"+str(id)+"' ")
            for linha in c:
                self.id = linha[0]
                self.nome = linha[1]
                self.idade = linha[2]
                self.cidade = linha[3]
                self.telefone = linha[4]
                self.email = linha[5]
            c.close()
            return 'Consulta feita com sucesso'
            #print(self.nome)
        except Error as ex:
            return 'Erro ao consultar'