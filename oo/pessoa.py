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

Classes, Objetos, Métodos e Atributos

* As Classes são tipos de dados definidos pelo desenvolvedor que atuam como um modelo para objetos. 
Pra não esquecer mais: Classes são fôrmas de bolo e bolos são objetos.

* Objetos são instâncias de uma Classe. Objetos podem modelar entidades do mundo real (Carro, Pessoa, Usuário) 
ou entidades abstratas (Temperatura, Umidade, Medição, Configuração).

* Métodos são funções definidas dentro de uma classe que descreve os comportamentos de um objeto. 
Em Python, o primeiro parâmetro dos métodos é sempre uma referência ao próprio objeto.

* Os Atributos são definidos na Classe e representam o estado de um objeto. Os objetos terão dados armazenados nos campos de atributos. 
Também existe o conceito de atributos de classe.

Herança Python

* A herança nos permite definir uma classe que herda todos os métodos e propriedades de outra classe.

* A classe pai é a classe da qual está sendo herdada, também chamada de classe base.

* A classe filha é a classe que herda de outra classe, também chamada de classe derivada. 

Adicione a função __init __ ()

* Até agora, criamos uma classe filha que herda as propriedades e métodos de seu pai.

* Queremos adicionar o __init__()função para a classe filha (em vez do pass palavra-chave).

* Nota: o __init__() A função é chamada automaticamente sempre que a classe está sendo usada para criar(contrutor) um novo objeto.

* Adicionamos com sucesso a função __init __ () e mantivemos o herança da classe pai, e estamos prontos para adicionar 
funcionalidade no __init__()função. 

Atributos Dinâmicos em Python

* Na hora que um objeto é instanciado é possível declarar além de atributos que já existam,
conforme a estrutura classe, também outros atributos podem ser declarados com seu valor.

* O atributo especial __dict__, em um objeto, é um dicionário que é usado para guardar atributos 
e seus respectivos valores

Atributos Gerais de Classe

* Podemos criar milhões de objetos, fácil e rapidamente.
E cada um deles terá seus métodos e atributos próprios e únicos.

* Porém, muitas vezes é interessante ter informações gerais, ou seja, um mesmo dado, um mesmo atributo 
presente em todos os objetos.

* Veja bem: uma única variável, presente e passível de ser acessada e modificada por todos os objetos. 
Não é cada objeto ter sua variável, isso já sabemos como fazer.

Atributos de Classe

* Atributos de classes são aquelas variáveis que são únicas, só tem ela, e ela está presente em todos 
os objetos.

Métodos estáticos

* Nem todas as funções de uma classe precisam receber uma referência de um objeto para lê-lo ou alterá-lo, 
muitas vezes uma função pode fazer o seu papel apenas com os dados passados como argumento.

* É possível colocar essa função dentro da classe e informar que ela não receberá o argumento self com o 
decorador @staticmethod:

* Dessa forma, essa função pode ser chamada diretamente de um objeto pessoa, ou até mesmo diretamente da classe, 
sem precisar criar um objeto primeiro:


Métodos de classes 

* Entretanto algumas funções podem precisar de um meio termo, necessitar acessar o contexto da classe, porém sem necessitar de um objeto. 
Isso é feito através do decorador @classmethod, onde a função decorada com ele, em vez de receber um objeto como primeiro argumento, 
recebe a própria classe.

* Função Isinstance
* A função isinstance() retorna Truese o objeto especificado for do tipo especificado, caso contrário False. 

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
    
    for filho in tarcisio.filhos: #Laço for 
        print(filho.nome)


tarcisio.sobrenome = 'Souza' # Atributos dinamicos 
print(tarcisio.sobrenome)
del tarcisio.filhos # apagando atributo dinamicamente
tarcisio.olhos = 1 
del tarcisio.olhos # Apagando atributo dinamicamente
print(tarcisio.__dict__) # Atributo especial dict
print(lucca.__dict__)