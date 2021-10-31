# Programa para comandar o treino da rede neural do NPC Smart

# a ideia é realizar um treino por seleção natural

import bisca_para_treino_da_rede_neural as bisca
import classes_base_para_treino as cb
#import numpy as np
import copy as cp
import random


'''

Quando pegamos os pesos da rede neural, eles vêm numa ordem e formato.
Para entende-lo, devemos lembrar que a rede construída tem a seguinte forma:

14 entradas --> 14-7-4-3 --> 3 saídas

Para cada layer, considerando um equacionamento do tipo wi*f(x) + bi,
a ordem dos pesos será primeiro dos wi's e, logo em seguida, dos bi's.

Tomando a primeira camada como exemplo, ao chamarmos o get_weights, teremos
na posição [0] um array de arrays com comprimento de 14 e, em cada elemento, 
outro array com 14 itens referentes a wi's.
Na posição [1], teremos um array com 14 itens simples referentes a bi's.
Na posição [2], referente a entrada da segunda camada, teremos um array de arrays
com comprimento de 14, mas que em cada elemento teremos um array com 7 itens.
E assim sucessivamente.

'''

# Quantidade de vezes que o código se manterá em loop de treino
QUANTIDADE_MAXIMA_DE_GERACOES = 2000

# Um loop de treino consiste em NUMERO_DE_RODADAS rodadas de bisca
NUMERO_MAXIMO_DE_RODADAS = 10

# Média para a distribuição gaussiana de probabilidades
MEDIA = 0.5

# Desvio padrão para a distribuição gaussiana de probabilidades
STD = 0.2

def adiciona_variabilidade_aleatoria(pesos=None, taxa_de_mutacao=0.05):
    '''
    A evolução biológica só acontece porque existem formas de se
    introduzir variabilidade genética nos novos indivíduos.
    Dividí-los em dois sexos fornece grande variabilidade, mas
    não é o único meio.
    Outro fator muito importante são os erros aleatórios, no
    qual o gene é transcrito com alguma diferença (mutação)
    em relação ao progenitor. Essa mudança pode trazer uma
    vantagem para a sobrevivência do indivíduo ou não.
    Assim, buscando imitar essa forma de mutação,
    esta função irá receber os pesos de um indivíduo
    e fazer um teste de chance de erro, dependendo da
    taxa: se não cair dentro dessa chance de erro, a
    função devolve os mesmos pesos que recebeu. Caso
    contrário, alguns dos pesos serão modificados
    aleatóriamente.

    Entrada:
        pesos --> um array com os pesos de uma rede neural
        taxa --> chance de haver mutação. Por padrão, é
                 utilizado o valor de 0.05 (5%).

    Saída: devolve um array de mesmo formato que o da entrada,
           com mutação nos pesos ou não.
    '''
    # uma pequena segurança na entrada
    if pesos == None:
        raise

    # Defini-se uma porcentagem de quantos pesos devem
    # ser alterados caso o indivíduo caia dentro da
    # taxa_de_mutacao
    porcentagem_pesos_alterados = 0.1

    #novos_pesos = cp.deepcopy(pesos)
    # Testa a sorte
    # Gera um número pseudo-aleatório no intervalo [0,100[
    # com passos de 1 em 1
    chance_de_nao_mutacionar = random.randrange(0,100,1)

    # Verifica se ficou dentro da taxa de erros
    if chance_de_nao_mutacionar > 100*taxa_de_mutacao:
        # O indivíduo não mutaciona e os pesos devolvidos
        # pela função são os mesmos da entrada
        return pesos

    # O caso contrário é o de haver uma alteração nos pesos

    '''
    Estratégia

    Vou ir de peso em peso, varrendo o array inteiro, para
    calcular a chance individual de cada um mutacionar.
    Isto é feito calculando novamente a chance_de_nao_mutacionar
    para cada peso. Se for para ser mudado, gero um número
    pseudo-aleatório flutuante no intervalo [0,1[
    para colocar no lugar.
    '''

    # Primeiro para os wi's
    for layer in range(0,8,2):
        # Bastante dependente do formato da rede
        aux = 0
        while (aux < len(pesos[layer])):
            for indice in range(0,len(pesos[layer][aux])):
                chance_de_nao_mutacionar = random.randrange(0,100,1)
                if chance_de_nao_mutacionar < 100*porcentagem_pesos_alterados:
                    # O peso atual deve ser alterado
                    # Escolhi uma probabilidade gaussiana do novo
                    # valor do peso
                    # média = 0.5
                    # desvio-padrão = 0.2
                    pesos[layer][aux][indice] = random.gauss(MEDIA, STD)
                    # Tratando casos fora do intervalo permitido
                    if pesos[layer][aux][indice] < 0:
                        pesos[layer][aux][indice] = 0.0

                    if pesos[layer][aux][indice] >= 1.0:
                        # Só não quero que seja 1.0
                        pesos[layer][aux][indice] = 0.99
    
    # Agora para os bi's
    for layer in range(1,8,2):
        for indice in range(0,len(pesos[layer])):
            chance_de_nao_mutacionar = random.randrange(0,100,1)
            if chance_de_nao_mutacionar < 100*porcentagem_pesos_alterados:
                # O peso atual deve ser alterado
                # Escolhi uma probabilidade gaussiana do novo
                # valor do peso
                # média = 0.5
                # desvio-padrão = 0.2
                pesos[layer][indice] = random.gauss(MEDIA, STD)
                # Tratando casos fora do intervalo permitido
                if pesos[layer][indice] < 0:
                    pesos[layer][indice] = 0.0

                if pesos[layer][indice] >= 1.0:
                    # Só não quero que seja 1.0
                    pesos[layer][indice] = 0.99

    return pesos

def gera_novo_individuo(pai, mae, posicao_dos_divisores):
    '''
    Esta função vai devolver os pesos de uma rede filha a partir
    dos pesos passados pelos pais.
    Vai utilizar a posicao_dos_divisores (uma lista de inteiros) 
    para separar os pesos em cada camada.
    '''
    #filho = np.copy(pai)
    filho = cp.deepcopy(pai)

    # Trocando os pesos wi's.

    pos = 0
    for layer in range(0,8,2):
        aux = 0
        while (aux < len(filho[layer])):
#            filho[layer][aux][0:posicao_dos_divisores[pos]] = (
#                pai[layer][aux][0:posicao_dos_divisores[pos]]
#            )
            filho[layer][aux][posicao_dos_divisores[pos]:len(filho[layer][0])] = (
                mae[layer][aux][posicao_dos_divisores[pos]:len(filho[layer][0])]
            )

            aux += 1
        pos += 1
    
    # Trocando os pesos bi's
    pos = 0
    for layer in range(1,8,2):
#        filho[layer][0:posicao_dos_divisores[pos]] = (
#            pai[layer][0:posicao_dos_divisores[pos]]
#        )
        filho[layer][posicao_dos_divisores[pos]:len(filho[layer])] = (
            mae[layer][posicao_dos_divisores[pos]:len(filho[layer])]
        )
        pos += 1
    
    # Adicionando variabilidade nos pesos
    #filho = adiciona_variabilidade_aleatoria(
    #    filho, taxa=0.05
    #)

    return filho


def gera_nova_geracao(geracao_antiga=[]):
    '''
    Função central para o algoritmo genético, ela vai embaralhar
    os genes (pesos) dos pais vencedores para criar os filhos
    Este processo vai se repetindo de geração em geração
    até produzir herdeiros que saibam jogar bisca.

    Teremos 20 pais ao fim de uma rodada. Cada um deles vai ter dois
    filhos com o parceiro imediatamente atrás e a frente:
    1-2, 2-3, 3-4, ... , 18-19, 19-20, 20-1


    entrada: uma lista com 20 tensores cujo o conteúdo são os pesos
             das redes neuras vencedoras
    saída: uma lista com 40 tensores cujo o conteúdo são os pesos
           das novas redes neurais
    '''

    if len(geracao_antiga) < 2:
        # Se não há ao menos um casal, não tem como gerar uma nova geração
        print('Quantidade insuficiente de progenitores!')
        raise

    divisores = [7,3,2,1]
    nova_geracao = []

    nova_geracao.append(gera_novo_individuo(
        geracao_antiga[0], geracao_antiga[1], divisores
    ))

    for aux in range(1,len(geracao_antiga)-1):
        nova_geracao.append(gera_novo_individuo(
            geracao_antiga[aux], geracao_antiga[aux-1], divisores
        ))
        nova_geracao.append(gera_novo_individuo(
            geracao_antiga[aux], geracao_antiga[aux+1], divisores
        ))

    nova_geracao.append(gera_novo_individuo(
        geracao_antiga[len(geracao_antiga) - 1], geracao_antiga[len(geracao_antiga) - 2], divisores
    ))
    
    nova_geracao.append(gera_novo_individuo(
        geracao_antiga[len(geracao_antiga) - 1], geracao_antiga[0], divisores
    ))

    nova_geracao.append(gera_novo_individuo(
        geracao_antiga[0], geracao_antiga[len(geracao_antiga) - 1], divisores
    ))

    return nova_geracao

def main():
    # QUANTIDADE_MAXIMA_DE_GERACOES se refere à
    # quantidade de vezes que o código se manterá em loop de treino
    
    # Lista de tensores com os pesos das 20 melhores redes
    # A ideia é ir salvando a cada iteração os pesos das redes vencedoras na lista
    lista_de_pesos_vencedores_na_rodada = []

    # Lista de tensores com pesos gerados a partir dos 20 melhores da rodada
    # Trata-se da base deste algoritmo genético de aprendizado

    lista_de_novos_pesos = []

    # Iniciando loop de treinamento

    epoca_atual = 0
    rodada_atual = 0
    pos_aux_para_lista_novos_pesos = 0 # Vai até 19

    print('\n')
    print(10*'#', end='')
    print(" TREINAMENTO DO SMART PLAYER ", end='')
    print(10*'#')
    print('\nQuantidade máxima de gerações: {:6d}'.format(QUANTIDADE_MAXIMA_DE_GERACOES))
    print('Número máximo de rodadas: {:6d}\n'.format(NUMERO_MAXIMO_DE_RODADAS))
    print(49*'#')

    print('\n')
    print(10*'.', end='')
    print('   INICIANDO O TREINAMENTO   ', end='')
    print(10*'.')
    print('\n')

    while (epoca_atual < QUANTIDADE_MAXIMA_DE_GERACOES):
        # Reiniciando variáveis
        rodada_atual = 0
        pos_aux_para_lista_novos_pesos = 0
        lista_de_pesos_vencedores_na_rodada = []

        print('Geração {:6d} em andamento'.format(epoca_atual+1), end=' ')
        # Iniciando as rodadas
        while (rodada_atual < NUMERO_MAXIMO_DE_RODADAS):
            #Transcrevendo um trecho do bisca.main() para permitir um controle
            # dos parâmetros da rede dos jogadores
            
            jogadores = ['Jog.1', 'Jog.2', 'Jog.3', 'Jog.4']
            # por enquanto esses nomes são fixos
            mesa = cb.MesaDeBisca(4)
            for jogador in jogadores:
                mesa.adicionar_jogador(jogador)

            # Se ao menos uma rodada já ocorreu, então temos pesos já selecionados
            # Neste caso, devo atualizar a rede neural antes do jogo

            if epoca_atual > 0:
                # atualiza os pesos da rede neural dos jogadores de
                # mesa.jogadores
                # Os filhos n e n+10 jogam contra o n+1 e n+11
                #limite_faixa_quatro_jogadores = pos_aux_para_lista_novos_pesos + 2
                #ind_jogadores = 0

                # Configurando novos pesos para as redes neurais dos jogadores
                # Condição antiga: pos_aux_para_lista_novos_pesos < limite_faixa_quatro_jogadores
                #while (ind_jogadores < 4):
                mesa.jogadores[0].set_pesos_da_rede_neural(
                    lista_de_novos_pesos[pos_aux_para_lista_novos_pesos]
                )
                mesa.jogadores[1].set_pesos_da_rede_neural(
                    lista_de_novos_pesos[pos_aux_para_lista_novos_pesos+1]
                )
                mesa.jogadores[2].set_pesos_da_rede_neural(
                    lista_de_novos_pesos[pos_aux_para_lista_novos_pesos+10]
                )
                mesa.jogadores[3].set_pesos_da_rede_neural(
                    lista_de_novos_pesos[pos_aux_para_lista_novos_pesos+11]
                )
                #ind_jogadores += 2
                pos_aux_para_lista_novos_pesos += 2

           
            # O código adaptado de bisca.py para o treinamento
            # devolve 'A' se a equipe_A venceu, 'B' se for a equipe_B
            # e 'E' se houver empate
            equipe_vencedora = bisca.main(mesa)

            if equipe_vencedora == 'A':
                for jogador in mesa.equipe_A:
                    lista_de_pesos_vencedores_na_rodada.append(
                        jogador.get_pesos_da_rede_neural()
                    )
            elif equipe_vencedora == 'B':
                for jogador in mesa.equipe_B:
                    lista_de_pesos_vencedores_na_rodada.append(
                        jogador.get_pesos_da_rede_neural()
                    )
            else:
                # Se deu empate, vou salvar o peso do primeiro de cada equipe
                lista_de_pesos_vencedores_na_rodada.append(
                    mesa.equipe_A[0].get_pesos_da_rede_neural()
                )
                lista_de_pesos_vencedores_na_rodada.append(
                    mesa.equipe_B[0].get_pesos_da_rede_neural()
                )
            
            rodada_atual += 1
            print('.', end='')
        
        epoca_atual += 1
        
        # Gera os novos pesos
        lista_de_novos_pesos = gera_nova_geracao(lista_de_pesos_vencedores_na_rodada)

        # Imprimindo o sinalizador de fim da época
        print(' concluída!')

    print('\n')
    print(10*'.', end='')
    print('          CONCLUÍDO          ',end='')
    print(10*'.')
    print('\n')

    print('Salvando os pesos da rede ...\n')

    # SALVA OS PESOS TREINADOS
    # Por simplicidade, vai salvar o primeiro elemento de lista_de_pesos_vencedores_na_rodada
    salvando_pesos = cb.SmartPlayer()
    salvando_pesos.set_pesos_da_rede_neural(
        lista_de_pesos_vencedores_na_rodada[0]
    )
    salvando_pesos.salvar_pesos_da_rede('pesos_da_rede_neural_treinada_para_smart_player')
    #############################

    print('\n')
    print(10*'#', end='')
    print('     FIM DO TREINAMENTO      ',end='')
    print(10*'#')
    print(49*'#')
    print('\n')


if (__name__ == "__main__"):
    main()