'''
Jogo de Pedra-papel-tesoure
2024.08.13
Caio Mario Zachesky Junior
'''

#bibliotecas 
from modules import clrScreen, displayHeader, getUserOption, validateUserOption, displayline, displayMsg, displayMsgCentro, displayHeaderT
from random import randint
from time import sleep

#constantes,variaveis e listas
msgsInicio = ['Seja bem vindo ao', 'Jogo do pedra-papel-tesoura','feito: Caio MZJR']

msgs = []

playAgain = ''

playerScore = 0

computerScore = 0

computerJogada = 0

playerJogada = 0
#Funções
def startParImpar():
  while(True):
    clrScreen()
    displayHeader(msgsInicio)
    playParImpar()
    playAgain = getUserOption('Deseja jogar novamente [s/n]')
    while not validateUserOption(playAgain, ['s','n','S','N',]):
      playAgain = getUserOption('Deseja jogar novamente [s/n]')
    if playAgain.lower() != 's':
      break
      
def displayMenu():
  msgs = ['Esolha:','[0] --> par','[1] --> impar']
  displayline()
  for msg in msgs:
    displayMsg(msg)
  displayline()

def displayScore(typeScore, playerScore, computerScore):
  msgs = []
  msgs. append(typeScore)
  msgs. append(f'Player:{playerScore} --- PC: {computerScore}')
  displayHeaderT(msgs)
  
def determineWinner(playerChoice, computerChoice):
  computerJogada = int(randint(0,9))
  playerJogada = int(input())
  play = ''
  result = ''
  choice = ['Par','Impar']
  playerChoiceStr = choice[int(playerChoice)]
  computerChoiceStr = choice[int(computerChoice)]
  total = playerJogada + computerJogada
  if total %2 == int(playerChoice):
    result = 'Você Ganhou'
  else:
    play = f'{computerChoiceStr} vence {playerChoiceStr}'
    result = 'Você perdeu'
  msgs = ['Jogada do Player :' + playerChoiceStr, 'Jogado do Pc:' + computerChoiceStr, play, result]
  displayHeaderT(msgs)
  return result


def playParImpar():
  playerScore = 0
  computerScore = 0
  while playerScore < 2 and computerScore < 2:
    displayMenu()
    playerChoice = getUserOption('Sua Escolha')
    while not validateUserOption(playerChoice, ['0','1',]):
      displayMenu()
      playerChoice = getUserOption('Sua Escolha')
    computerChoice = str(randint(0,1))
    result = determineWinner(playerChoice, computerChoice)
    if 'Ganhou'in result:
      playerScore += 1
    elif 'perdeu' in result:
      computerScore += 1
    if playerScore < 2 and computerScore < 2:
      displayScore('PLACAR', playerScore, computerScore)
    sleep(1)
  displayScore('PLACAR FINAL', playerScore, computerScore)
  if playerScore > computerScore:
    displayHeader(['PArebéns','YOU WIM '])
  else:
    displayHeader(['PAREBÈNS','LOSER'])

#Main