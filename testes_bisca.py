# Programa para testar a função de escolhe_carta_para_jogar
# do SmartPlayer

#import tensorflow as tf
#from tensorflow import keras
import classes_base_para_treino as cb
import comandando_treino_do_smart_player as treinador
#import numpy as np

s1 = cb.SmartPlayer(nome='s1')

s1.adicionar_carta_na_mao(cb.Carta(naipe='ESPADAS', numero='A', pontos=11))
#s1.adicionar_carta_na_mao(cb.Carta(naipe='OUROS', numero='7', pontos=10))
#s1.adicionar_carta_na_mao(cb.Carta(naipe='PAUS', numero='4', pontos=0))

mesa = cb.Carta(naipe='COPAS', numero='2', pontos=0)

cartas_jogadas = []

escolha = s1.escolhe_carta_para_jogar(carta_da_mesa=mesa, cartas_jogadas_na_mesa=cartas_jogadas)

print(escolha)

###########################

# Testando gera_novo_individuo

s2 = cb.SmartPlayer(nome='s2')

pesos_s1 = s1.get_pesos_da_rede_neural()
pesos_s2 = s2.get_pesos_da_rede_neural()

pos_aux = 4

print('pesos do s1 em [{}][{}]'.format(pos_aux,pos_aux))
print(pesos_s1[pos_aux][pos_aux])

print('pesos do s2 em [{}][{}]'.format(pos_aux,pos_aux))
print(pesos_s2[pos_aux][pos_aux])

pesos_s3 = treinador.gera_novo_individuo(pesos_s1, pesos_s2, [7,3,2,1])

print('pesos do s3 em [{}][{}]'.format(pos_aux,pos_aux))
print(pesos_s3[pos_aux][pos_aux])

print('pesos do s1 em [{}][{}]'.format(pos_aux,pos_aux))
print(pesos_s1[pos_aux][pos_aux])

print('pesos do s2 em [{}][{}]'.format(pos_aux,pos_aux))
print(pesos_s2[pos_aux][pos_aux])

pesos_s4 = treinador.gera_novo_individuo(pesos_s2, pesos_s1, [7,3,2,1])

print('pesos do s4 em [{}][{}]'.format(pos_aux,pos_aux))
print(pesos_s4[pos_aux][pos_aux])

s3 = cb.SmartPlayer(nome='s3')

pesos_s3_antigos = s3.get_pesos_da_rede_neural()

s3.set_pesos_da_rede_neural(pesos_s3)

pesos_s3_novos = s3.get_pesos_da_rede_neural()

print('\npesos s3 antigos')
print(pesos_s3_antigos[pos_aux][pos_aux])
print('\npesos s3 novos')
print(pesos_s3_novos[pos_aux][pos_aux])

##################

# Testando gera_nova_geracao

geracao_antiga = []

# Que coisa feia...
#np.append(geracao_antiga, s1.get_pesos_da_rede_neural, axis=0)
geracao_antiga.append(s1.get_pesos_da_rede_neural())
geracao_antiga.append(s2.get_pesos_da_rede_neural())
geracao_antiga.append(s3.get_pesos_da_rede_neural())

nova_geracao = treinador.gera_nova_geracao(geracao_antiga)

print('\nProgenitor 0')
print(geracao_antiga[0][pos_aux][pos_aux])
print('\nProgenitor 1')
print(geracao_antiga[1][pos_aux][pos_aux])
print('\nProgenitor 2')
print(geracao_antiga[2][pos_aux][pos_aux])

print('\nFilho 0-1')
print(nova_geracao[0][pos_aux][pos_aux])
print('Filho 1-0')
print(nova_geracao[1][pos_aux][pos_aux])
print('Filho 1-2')
print(nova_geracao[2][pos_aux][pos_aux])
print('Filho 2-1')
print(nova_geracao[3][pos_aux][pos_aux])
print('Filho 2-0')
print(nova_geracao[4][pos_aux][pos_aux])
print('Filho 0-2')
print(nova_geracao[5][pos_aux][pos_aux])