"""Jogo da adivinhação: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 10 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. 
O programa deverá escrever na tela se o usuário venceu ou perdeu."""
import random as rd

sorteio = rd.randint(0,10)
palpite = int(input("Qual seu palpite?\n"))

if sorteio == palpite:
  print("Parabéns! Você acertou!")
else:
  print("ERROU!")
