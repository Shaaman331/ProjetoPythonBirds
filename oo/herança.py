''' Programa em Python para demonstrar herança de classes'''
    
 #Super classe, note a classe "object" entre parênteses.
 #"object" é a super classe de todas as classes.
 #No Python 3.x "class Pessoa" é equivalente a "class Pessoa(object)" 
class Pessoa(object):
        
    # Construtor do objeto Pessoa
    def __init__(self, nome):
        self.nome = nome
    
    # Função para obter o nome de Pessoa
    def getNome(self):
        return self.nome
    
    # Função para verificar se Pessoa é um funcionário ou não
    def verificaFuncionario(self):
        return False

#Classe filha ou Subclasse
#Desta vez a classe Pessoa está entre parênteses
class Funcionario(Pessoa):
    
# Aqui a função é sobrescrita, alterando o seu comportamento
    def verificaFuncionario(self):
        return True
    
print('Instacia de pessoas')
p = Pessoa("João")  # Uma instância de Pessoa
print(p.getNome(), p.verificaFuncionario())
print()
print('Instacia de funcionaio')
p = Funcionario("João")  # Uma instância de Funcionario
print(p.getNome(), p.verificaFuncionario())

# Código em Python 3 para demonstrar como os construtores das classes pai
# são chamados.
   
# Classe Pai
class Pessoa( object ):   
   
        # __init__ é o construtor da classe
        # self é a própria classe
        def __init__(self, nome, numeroid):  
                self.nome = nome
                self.numeroid = numeroid
        def display(self):
                print(self.nome)
                print(self.numeroid)

# Classe Filha
class Funcionario( Pessoa):          
        def __init__(self, nome, numeroid, salario, cargo):
                self.salario = salario
                self.cargo = cargo
   
                # invocando o construtor da classe pai
                Pessoa.__init__(self, nome, numeroid)
   
print()
print('Instacioamento de um objeto do tipo funcionário')
# instanciando um objeto do tipo funcionário
func = Funcionario("José", 21081898, 2000, "Estagiário")   
   
# chamando uma função da classe Pessoa em um objeto do tipo Funcionário
func.display() 

# Programa em Python3 de exemplo de herança múltipla
class Base1(object):
    def __init__(self):
        self.str1 = "Exemplo1"
        print("Base1")
   
class Base2(object):
    def __init__(self):
        self.str2 = "Exemplo2"       
        print("Base2")
   
class Derivada(Base1, Base2):
    def __init__(self):
           
        # invocando construtores de Base1 e Base2
        Base1.__init__(self)
        Base2.__init__(self)
        print("Derivada")
           
    def printStrs(self):
        print(self.str1, self.str2)

print() 
print('Exemplo de herança multiplas')
ob = Derivada()
ob.printStrs()

