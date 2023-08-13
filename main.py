#BIBLIOTECAS
import numpy as np
from random import randint
from time import sleep


#APOSTA


#FUNÇÕES e VARIÁVEIS

Fichas = 20
Aposta = 0
Sua_mão = []
Dealer_mão = []
secvar = 0

def embaralhar(m1, m2):
	global Sua_mão
	global Dealer_mão
	Sua_mão = [randint(1,10), randint(1,10)]
	Dealer_mão = [randint(1,10), randint(1,10)]
def linha(nl):
    print("\033[31m==\033[0m\033[30m==\033[0m" * nl)
def main():
	global Aposta
	print ("\033[31mVocê tem\033[0m", "\033[31m\033[1m",Fichas,"\033[0m", "\033[31mfichas.\033[0m")
	Aposta = int(input("Quanto você deseja apostar? \033[1mAposte no mínimo 5 fichas.  \033[0m"))
	if Aposta < 5:
		print ("\033[31m\033[1mAposte no mínimo 5 fichas!\033[0m\n")
		main()
	elif Aposta > Fichas:
		print ("\033[31m\033[1mFichas insuficientes!\033[0m\n")
		main()
	else:
		print("1")
		apostas()

def apostas():
	linha(40)
	global secvar
	secvar = 0
	print("\033[34m\nEstá é sua mão:           \033[0m", Sua_mão)
	#print("\033[35mEstá é a mão do sistema:  \033[0m", Dealer_mão)
	Puxar_carta = input("\nVocê deseja puxar mais uma carta? (1)Sim (Qualquer outro botão)Não\n").strip().upper()[0]
	if Puxar_carta == '1':
		Sua_mão.append(randint(1,11))
		results()
		print("2")
		apostas()
		#print("\033[35mMão do sistema:\033[0m", Dealer_mão)
	else:
		secvar += 1
		if sum(Sua_mão)<21 and sum(Dealer_mão)<21 and sum(Sua_mão)>sum(Dealer_mão):
			final()
		elif sum(Sua_mão)<21 and sum(Dealer_mão)<21 and sum(Sua_mão)<sum(Dealer_mão):
			final()
		mostrar()
		results()
def vence(l1):
	if sum(l1)==21:
		return True
	else:
		return False
def perde(l1):
	if sum(l1)>21:
		return True
	else: 
		return False
#EXECUÇÃO
##INTRODUÇÃO AS REGRAS
def puxada(l1):
	x = randint(1, 10)
	if x > 5 and sum(l1)< 18:
		l1.append(randint(1,11))
def mostrar():
	print("\n\033[34m\nEstá é sua mão:           \033[0m", Sua_mão)
	print("\n\033[35mEstá é a mão do sistema:  \033[0m", Dealer_mão)
def regras():
	print("{:^179}".format("\033[31m\033[40m\033[1m Bem-vindo ao Blackjack da Smile\033[0m"))
	sleep(1.2)
	print ("{:^180}".format("\033[40m\033[97m\033[1m Regras Blackjack Smile \033[0m "))
	sleep(1)
	print ("\033[97m\033[1m\n 1 -  \033[0m\033[32m Player Inicia com 20 fichas;")
	sleep(1)
	print ("\033[97m\033[1m 2 -  \033[0m\033[32m O Dealer (sistema), distribuirá as 2 cartas para o player, e para ele mesmo, mas com uma carta misteriosa (0);")
	sleep(4)
	print ("\033[97m\033[1m 3 -  \033[0m\033[32m Você começa jogando puxando as cartas, e ter a sorte de não ultrapassar de 21 pontos nelas, se ultrapassar você estoura e perde para o sistema;")
	sleep(5)
	print ("\033[97m\033[1m 4 -  \033[0m\033[32m Após de você ter escolhido puxar as cartas e não estourar e ter decidido parar, é a vez do sistema jogar, revelando primeiro sua carta mistério,\n       e se não for suficiente para ultrapassar você, ele pode puxar mais uma carta;")
	sleep(9)
	print ("\033[97m\033[1m 5 -  \033[0m\033[32m Se o sistema estourar, ele perde, e paga sua aposta, se ele ganhar ele pega suas fichas que você apostou.\n\033[0m")
	sleep(4.5)
def fichas(l1,l2):
	global Fichas
	if sum(l1)<sum(l2) and sum(l2)!=21 and perde(l2) or vence(l1) or secvar==1:
		Fichas = Fichas+Aposta
	elif sum(l2)<sum(l1) and sum(l1)>=21 or vence(l2):
		Fichas=Fichas-Aposta
def results():
	if vence(Sua_mão) or perde(Dealer_mão) or vence(Dealer_mão) or perde(Sua_mão):
			if vence(Sua_mão) and vence(Dealer_mão):
				print("\n\033[31m\033[1mNinguém venceu, temos um empate...\nSegue o jogo\033[0m")
			final()
	else: 
			print("\n\033[31m\033[1mNinguém venceu, temos um empate...\nSegue o jogo\033[0m")
def final():
	print("\n\033[31m\033[1mTemos um vencedor\033[0m")
	fichas(Sua_mão, Dealer_mão)
	mostrar()
	if int(input("Deseja jogar de novo? \n(1)Sim (Qualquer outro)Não\n"))==1:
		embaralhar(Sua_mão, Dealer_mão)
		main()
	else:
		linha(40)
		print("\033[32m\033[1mObrigado por jogar o Blackjack da Smile. Volte sempre!!!\033[0m")
linha(40)
#regras()
linha(40)
embaralhar(Sua_mão, Dealer_mão)
main()


'''
 #DISTRIBUIÇÃO DE CARTAS

Sua_mão = [randint(1, 10), randint(1, 10)]
Dealer_mão = [randint(1, 10), 0 ]
linha(40)
print("\033[34m\nEstá é sua mão:           \033[0m", Sua_mão)
print("\033[35mEstá é a mão do sistema:  \033[0m", Dealer_mão)
while True:
  Puxar_carta = input("\nVocê deseja puxar mais uma carta?\033[31m(Lembre-se! Não pode ultrapassar de 21)\033[0m [\033[32mS\033[0m/\033[31mN\033[0m]  ").strip().upper()[0]
  if Puxar_carta == 'S':
    Sua_mão.append(randint(1,11))
    print("\033[34m\nSua mão:       \033[0m", Sua_mão)
    print("\033[35mMão do sistema:\033[0m", Dealer_mão)
  else:
    break
    continue
Dealer_mão = [Dealer_mão[0], randint(1,11)]
soma_Dealer_mão = sum(Dealer_mão)
soma_Sua_mão = sum(Sua_mão)
 #Se a mão do jogador for maior que 21
if soma_Sua_mão > 21:
    print("\n\033[31m\033[1mVocê perdeu, infelizmente você estourou!\033[0m")
    print("\033[35m\nMão do Sistema:", Dealer_mão ,"= \033[0m",soma_Dealer_mão)
    print("\033[34mSua mão:       ", Sua_mão ,"= \033[0m",soma_Sua_mão)
    Fichas = Fichas - Aposta
    print("\n\033[31mSuas fichas:  \033[0m", "\033[31m\033[1m",Fichas,"\033[0m")
    dnv = input('\nVocê quer jogar novamente? [\033[32mS\033[0m/\033[31mN\033[0m]: ').strip().upper()[0]
    linha(40)
    continue
else:
     pass

while True:
   if sum(Sua_mão) >= sum(Dealer_mão):
      Dealer_mão.append(randint(1,11))
   else:
      break
soma_Dealer_mão = sum(Dealer_mão)
print ("\033[90m\033[1mSistema revelando sua carta e analisando o jogo...\033[0m")
sleep (1.7)
print("\033[34m\nSua mão:       ", Sua_mão ,"= \033[0m", soma_Sua_mão)
print("\033[35mMão do sistema:", Dealer_mão ,"= \033[0m", soma_Dealer_mão)
if soma_Sua_mão > 21:
    print("\n\033[31m\033[1mVocê perdeu, infelizmente você estourou!\033[0m")
    print("\033[35m\nMão do Sistema:", Dealer_mão ,"= \033[0m",soma_Dealer_mão)
    print("\033[34mSua mão:       ", Sua_mão ,"= \033[0m",soma_Sua_mão)
    Fichas = Fichas - Aposta
    print("\n\033[31mSuas fichas:  \033[0m", "\033[31m\033[1m", Fichas, "\033[0m")
elif soma_Dealer_mão > 21:
    print("\n\033[33m\033[1mVOCÊ GANHOU, parabéns!!\033[0m")
    print("\033[34m\nSua mão:       ", Sua_mão, "= \033[0m", soma_Sua_mão)
    print("\033[35mMão do Sistema:", Dealer_mão, "= \033[0m", soma_Dealer_mão)
    Fichas = Fichas + Aposta
    print("\n\033[31mSuas fichas:  \033[0m", "\033[31m\033[1m", Fichas, "\033[0m")
elif soma_Dealer_mão > soma_Sua_mão:
    print("\n\033[31m\033[1mVocê perdeu, Que tal testar a sorte novamente?!\033[0m")
    print("\033[35m\nMão do Sistema:", Dealer_mão, "= \033[0m", soma_Dealer_mão)
    print("\033[34mSua mão:       ", Sua_mão, "= \033[0m", soma_Sua_mão)
    Fichas = Fichas - Aposta
    print("\n\033[31mSuas fichas:  \033[0m", "\033[31m\033[1m",Fichas,"\033[0m")
elif soma_Sua_mão > soma_Dealer_mão:
    print("\n\033[33m\033[1mVOCÊ GANHOU, parabéns!!\033[0m")
    print("\033[34m\nSua mão:       ", Sua_mão, "= \033[0m", soma_Sua_mão)
    print("\033[35mMão do Sistema:", Dealer_mão, "= \033[0m", soma_Dealer_mão)
    Fichas = Fichas + Aposta
    print("\n\033[31mSuas fichas:  \033[0m", "\033[31m\033[1m",Fichas,"\033[0m")
elif soma_Dealer_mão == 21:
    print("\n\033[31m\033[1mVocê perdeu, Que tal testar a sorte novamente?!\033[0m")
    print("\033[35m\nMão do Sistema:", Dealer_mão, "= \033[0m", soma_Dealer_mão)
    print("\033[34mSua mão:       ", Sua_mão, "= \033[0m", soma_Sua_mão)
    Fichas = Fichas - Aposta
    print("\n\033[31mSuas fichas:  \033[0m", "\033[31m\033[1m",Fichas,"\033[0m")
elif soma_Sua_mão == 21:
    print("\n\033[33m\033[1mVOCÊ GANHOU, parabéns!!\033[0m")
    print("\033[34m\nSua mão:       ", Sua_mão, "= \033[0m", soma_Sua_mão)
    print("\033[35mMão do Sistema:", Dealer_mão, "= \033[0m", soma_Dealer_mão)
    Fichas = Fichas + Aposta
    print("\n\033[31mSuas fichas:  \033[0m", "\033[31m\033[1m",Fichas,"\033[0m")
else:
    print("\nVocês empataram")
    print("\033[34m\nSua mão:       ", Sua_mão, "= \033[0m", soma_Sua_mão)
    print("\033[35mMão do Sistema:", Dealer_mão, "= \033[0m", soma_Dealer_mão)
    print("\n\033[31mSuas fichas:  \033[0m", "\033[31m\033[1m",Fichas,"\033[0m")'''
	
'''dnv = input('\nVocê quer jogar novamente? [\033[32mS\033[0m/\033[31mN\033[0m]: ').strip().upper()[0]'''


'''dnv = 'S'
Fichas = 20
while dnv == 'S':
 while True:
    print ("\033[31mVocê tem\033[0m", "\033[31m\033[1m",Fichas,"\033[0m", "\033[31mfichas.\033[0m")
    Aposta = int(input("Quanto vovê deseja apostar? \033[1mAposte no mínimo 5 fichas.  \033[0m"))
    if Aposta < 5:
      print ("\033[31m\033[1mAposte no mínimo 5 fichas!\033[0m\n")
    elif Aposta > Fichas:
      print ("\033[31m\033[1mFichas insuficientes!\033[0m\n")
    else:
      break'''