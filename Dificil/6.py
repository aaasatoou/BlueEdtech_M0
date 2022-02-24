"""Jogo de dados: Crie um programa onde jogadores joguem um dado e tenham resultados aleatórios.
O programa tem que:
Perguntar quantas rodadas você quer fazer;
Perguntar quantos jogadores vão jogar;
Criar um objeto pra cada jogador com nome e número tirado;
Guarda todos os objetos em uma lista;
Ordenar esses objetos, sabendo que o vencedor tirou o maior número no dado.
Mostrar no final qual jogador ganhou mais rodadas e foi o grande campeão."""

import random

dic = {"Jogadores":[],
       "Placar":[]        
}

rodadas = int(input("Quantas rodadas irão ser jogadas? \n"))
numJ = int(input("Quantos jogadores irão jogar? \n"))

for n in range(0,numJ):
  dic["Jogadores"].append(input(f"Nome do jogador na posição {n+1}: ").strip().capitalize())
  dic["Placar"].append(0)

for i in range (0,rodadas):
  dic[f"Rodada {i+1}"] = []
  for n in range (0,numJ):
    dic[f"Rodada {i+1}"].append(random.randint(1,6))

  print(f"\n{dic[f'Rodada {i+1}']}")
  
  if dic[f"Rodada {i+1}"].count(max(dic[f"Rodada {i+1}"])) > 1:
    print(f"Rodada {i+1} desconsiderada devido ao empate!")
  else:
    print(f"Rodada {i+1} é valida!")
    dic["Placar"][dic[f"Rodada {i+1}"].index(max(dic[f"Rodada {i+1}"]))] += 1



print(f"\n\nO placar final é: {dic['Placar']}")

if dic["Placar"].count(max(dic["Placar"])) > 1:

  print("Empate!")
  vencedores = []

  for x in range(len(dic["Placar"])):
    if dic["Placar"][x] == max(dic["Placar"]):
      vencedores.append(x)
      print(f"Parabéns {dic['Jogadores'][x]}")

else:
  print(f"Parabéns {dic['Jogadores'][dic['Placar'].index(max(dic['Placar']))]}, você venceu!")
