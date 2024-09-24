'''
projeto jogo pedra-papel-tesoura
2024.08.13
Caio Mario Zachesky Junior
'''

# --> bibliotecas

from modules import clrScreen, displayline, displayMsg, displayMsgCentro, displayHeader, getUserOption, validateUserOption, displayHeaderT # Importa a funções do arquivo modules.py
from ppt import startPPT # Importa a função do arquivo ppt.py
from parimpar import startParImpar
# --> Constantes, Variaveis e Listas

# --> Funções

# --> Main
msgs = ['Seja bem vindo aos jogos', 'pedra-papel-tesoura','par ou impar']
displayHeader(msgs)
msgs = ['Digite 0 --> sair', 'Digite 1 -->Pedra-Papel-Tesoura', 'Digite 2 --> Par ou Ímpar']
displayHeaderT(msgs)
opUser = getUserOption('Sua escolha')
while not validateUserOption(opUser,['0','1','2']):
  opUser = getUserOption('Sua escolha')
if(opUser == '1'):
  startPPT() # chamando a função startPPt
elif(opUser == '2'):
  startParImpar()
else:
  displaymsg('Até a proxima...')
  