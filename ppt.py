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

#Funções
def startPPT():
  while(True):
    clrScreen()
    displayHeader(msgsInicio)
    playPPT()
    playAgain = getUserOption('Deseja jogar novamente [s/n]')
    while not validateUserOption(playAgain, ['s','n','S','N',]):
      playAgain = getUserOption('Deseja jogar novamente [s/n]')
    if playAgain.lower() != 's':
      break
def displayMenu():
  msgs = ['Esolha:','[0] --> pedra','[1] --> papel','[2] --> tesoura']
  displayline()
  for msg in msgs:
    displayMsg(msg)
  displayline()

def displayScore(typeScore, playerScore, computerScore):
  msgs= []
  msgs. append(typeScore)
  msgs. append(f'Player:{playerScore} --- PC: {computerScore}')
  displayHeaderT(msgs)
def determineWinner(playerChoice, computerChoice):
  play = ''
  result = ''
  choice = ['pedra','papel','tesoura']
  playerChoiceStr = choice[int(playerChoice)]
  computerChoiceStr = choice[int(computerChoice)]
  if playerChoice == computerChoice:
    result = 'Empate!'
  elif (playerChoice == '0' and computerChoice == '2') or  (playerChoice == '1' and computerChoice == '0') or  (playerChoice == '2' and computerChoice == '1'):
    play = f'{playerChoiceStr} vence {computerChoiceStr}'
    result = 'Você Ganhou'
  else:
    play = f'{computerChoiceStr} vence {playerChoiceStr}'
    result = 'Você perdeu'
  msgs = ['Jogada do Player :' + playerChoiceStr, 'Jogado do Pc:' + computerChoiceStr, play, result]
  displayHeaderT(msgs)
  return result
def playPPT():
  playerScore = 0
  computerScore = 0
  while playerScore < 2 and computerScore < 2:
    displayMenu()
    playerChoice = getUserOption('Sua Escolha')
    while not validateUserOption(playerChoice, ['0','1','2']):
      displayMenu()
      playerChoice = getUserOption('Sua Escolha')
    computerChoice = str(randint(0,2))
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