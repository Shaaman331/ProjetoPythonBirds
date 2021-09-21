'''
Classes e Objetos - Fundamentos

* A Programação Orientada a Objetos (POO) é ​​um paradigma de programação baseado no conceito de Classes e Objetos.

Classes podem conter dados e código:

    Dados na forma de campos (também chamamos de atributos ou propriedades); e
    Código, na forma de procedimentos (frequentemente conhecido como métodos).

* Uma importante característica dos objetos é que seus próprios métodos podem acessar e frequentemente modificar seus campos 
de dados: objetos mantém uma referência para si mesmo, o atributo self no Python.

* Na programação orientada à objetos o foco é na criação de objetos que contem tanto os dados quanto as funcionalidades. 
Em geral, a definição de cada objeto corresponde a algum objeto ou conceito no mundo real e as funções que operam sobre tal 
objeto correspondem as formas que os objetos reais interagem


'''
class Pessoa: #Classe Pessoa
    def __init__(self,*filhos, nome = None, idade = 31): # Atributos de instância, objetos (Herança)
        self.nome = nome # self.nome (Atributo de objetos), idade (variavel
        self.idade= idade # self.idade (Atribulto de objetos), idade (variavel)
        self.filhos = list(filhos) # Self.filhos(atributo complexo)
        
    def cumprimentar(self): # Método cumprimentar
        return f'Olá {id(self)}'

if __name__ == '__main__':
    lucca = Pessoa(nome ='Lucca') # Objeto complexo, filho
    tarcisio = Pessoa(lucca, nome ="Tarcisio") # Objeto complexo, pai
    print(Pessoa.cumprimentar(tarcisio))
    print(id(tarcisio))
    print(tarcisio.cumprimentar())
    print(tarcisio.nome) #Atributo de objeto
    print(tarcisio.idade) #Atributo de onjeto
    
    for filho in tarcisio.filhos: # Laço for 
        print(filho.nome)