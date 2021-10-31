# Avalia a eficiência da rede treinada frente ao Dummy Player

import bisca_para_treino_da_rede_neural as bisca
import classes_base_para_teste as cb

# Quantidade máxima de mesas jogadas
NUMERO_MAXIMO_DE_RODADAS = 1000

def main():

    # Marca a quantidade de vezes que a equipe A venceu
    qtde_vezes_smart_venceu = 0
    # Marca a quantidade de vezes que a equipe B venceu
    qtde_vezes_dummy_venceu = 0

    '''
    Uma dupla de SmartPlayer (A) enfrentará uma de DummyPlayer (B).
    Toda vez que A vencer, qtde_vezes_smart_venceu aumenta em 1.
    Toda vez que B vencer, qtde_vezes_dummy_venceu aumenta em 1.
    Se eles empatarem, nenhum aumenta.

    Ao final, teremos a porcentagem de jogos vencidos pelo Smart
    dada por (qtde_vezes_smart_venceu * 100)/NUMERO_MAXIMO_DE_RODADAS    
    '''

    print('\n')
    print('INICIANDO AVALIAÇÃO DE EFICIÊNCIA DO TREINO')
    print('\n')
    rodada_atual = 0
    while (rodada_atual < NUMERO_MAXIMO_DE_RODADAS):

        jogadores = ['S1', 'D1', 'S2', 'D2']
        # por enquanto esses nomes são fixos
        mesa = cb.MesaDeBisca(4)
        aux = 0
        for jogador in jogadores:
            mesa.adicionar_jogador(jogador, aux)
            aux += 1
        
        equipe_vencedora = bisca.main(mesa)

        if equipe_vencedora == 'A':
            qtde_vezes_smart_venceu += 1
        elif equipe_vencedora == 'B':
            qtde_vezes_dummy_venceu += 1

        print('Rodada {:6d} de {:6d}'.format(rodada_atual+1,NUMERO_MAXIMO_DE_RODADAS))

        rodada_atual += 1
    
    print('\n')
    print(40*'-')
    print('Equipe de SmartPlayer venceu {:3.2f} % das partidas'.format(
        (qtde_vezes_smart_venceu*100)/NUMERO_MAXIMO_DE_RODADAS)
    )
    print('\n')
    print('Equipe de DummyPlayer venceu {:3.2f} % das partidas'.format(
        (qtde_vezes_dummy_venceu*100)/NUMERO_MAXIMO_DE_RODADAS)
    )
    print(40*'-')
    print('\n')


if (__name__ == "__main__"):
    main()
        