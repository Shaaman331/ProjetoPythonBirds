'''
Você deve criar uma classe carro que vai possuir dois atributos
compostos por outras duas classes 

1) Motor 
2) Direção 

O motor terá a resposabilidade de controlar a velocidade.
Ele oferece os seguintes atributos:

1) Atributo de dado Velocidade
2) Método acelerar, que deverá incrementar a velocidade de uma unidade 
3) Método frear que deverá decrementar a velocidade em duas unidades 

A direção terá a responsabilidade de controlar a direção. 
Ela oferece os seguintes atributos:

1) Valor de direção com valores possíveis: Norte, Sul, Leste, Oeste.
2) Método Girar a direita

  N
O   L
  S


    Exemplo:
    #Testando motor
    >>> motor = Motor() 
    >>> motor.velocidade() 
    0
    >>> motor.acelerar() 
    >>> motor.velocidade
    1
    >>> motor.acelerar() 
    >>> motor.velocidade
    2
    >>> motor.acelerar() 
    >>> motor.velocidade
    3
    >>> motor.frear() 
    >>> motor.velocidade
    1
    >>> motor.frear() 
    >>> motor.velocidade
    0

    >>> #Testando a direção
    >>> direcao = Direcao()
    >>> direcao.valor
    'Norte'
    >>> direcao = Direcao()
    >>> direcao.valor
    'Leste'
    >>> direcao = Direcao()
    >>> direcao.valor
    'Sul'
    >>> direcao = Direcao()
    >>> direcao.valor
    'Oeste'
    >>> direcao = Direcao()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Norte'
    >>> carro = Carro(direcao, motor)
    >>> carro.calcular_velocidade()
    0
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    1
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    2
    >>> carro.frear()
    >>> carro.calcular_velocidade()
    0
    >>> carro.calcular_a_direcao()
    'Norte
   >>> carro.girar_a_direita()
   >>> carro.calculr_direcao()
   'Leste'
   >>> carro.girar_a_esquerda()
   >>> carro.calculr_direcao()
   'Norte'
   >>> carro.girar_a_esquerda()
   >>> carro.calculr_direcao()
   'Oeste'
   '''     
   class Direcao:
    rotacao_a_direta_dct={
        NORTE:LESTE, LESTE:SUL, SUL : OESTE, OESTE : NORTE
    }
    
    rotacao_a_esquerda_dct={
        NORTE:OESTE, LESTE:NORTE, SUL : OESTE, LESTE : SUL
    }

    def __init__(self):
        self.valor = NORTE

    def girar_a_direita(self):
        self.valor = self.rotacao_a_direita_dct[self.valor]
    
    def girar_a_esquerda(self):
        self.valor = self.rotacao_a_esquerda_dct[self.valor]

class Motor:
    def __init__(self):
        self.velocidade = 0
    
    def acelar(self):
        self.velocidade += 1
    
    def frear(self):
        self.velocidade -= 2
        self.velocidade = max(0, self.velocidade)