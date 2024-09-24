'''
Arquivo de Modulos
2024.08.13
Caio Mario Zachesky Junior
'''

# --> bibliotecas
from random import choice # usado para randomizar a lista
from time import sleep
# --> Constantes, Variaveis e Listas
TAM = 50 # Tamanho da tela 
CAR = choice(['-','>','~','*']) # lista com caracter utilizado para desenho da tela
MAR = 4 # Tamanho da margem

# --> Funções
def clrScreen(): # Função para limpar a tela
  print('\n'*TAM) # Mostra na tela \n == linha * TAM 

def displayline(): # Função para mostra uma linha caracteres
  print(CAR*TAM) # mostra caracteres

def displayMsg(msg): # função para mostra uma msg a esquerda 
  print(f'{CAR} {msg:<{TAM-MAR}} {CAR}') # mostra msg na esquerda

def displayMsgCentro(msg): # função para centralizar msg
  print(f'{CAR} {msg:^{TAM-MAR}} {CAR}') # mostra msg no meio

def displayHeader(msgs): # função para o cabeçalho
  displayline() # Famando a função da linha
  for item in msgs: # repeter até os itens acabar
    displayMsgCentro(item) #famando a 
  displayline()
def displayHeaderT(msgs): # função para o cabeçalho
  displayline() # Famando a função da linha
  for item in msgs: # repeter até os itens acabar
    displayMsgCentro(item)#famando a
    sleep(1)
  displayline()
def getUserOption(msg):
  option = input(f'{CAR} {msg}: ').strip()
  return option

def validateUserOption(option, listOptions):
  if option in listOptions:
    return True
  else:
    msgsErro = ['Opção Inválida!', 'Escolha Novamente...']
    displayHeader(msgsErro)
    return False
# --> main