'''
Este código só serve para treinar a rede neural e nada mais

'''

import classes_base as cb

def jogador_da_vez(quem_comeca, vez, qtde_de_jogadores):
    # função para executar uma conta 'em ciclo'.
    # supondo que quem_comeca seja o jogador 3 de 4 e que a vez esteja em 2
    # neste caso, precisaria devolver 1 para recomeçar o ciclo.
    # Esta é a ideia desta função.
    # quem_comeca -> posição do primeiro jogador a jogar (int)
    # vez -> posição do jogador a jogar em relação a quem_comeca (int)

    jogador_da_vez = quem_comeca + vez
    
    if jogador_da_vez >= qtde_de_jogadores:
        jogador_da_vez -= qtde_de_jogadores
    
    return jogador_da_vez

def main(mesa_de_bisca=None):

    mesa = mesa_de_bisca

    # preenchi os jogadores
    mesa.dividir_equipes()
    mesa.prepara_a_mesa()
    quem_comeca = 0
    # um identificador para saber quem começa a rodada

    while(not mesa.acabou_jogo()):
        vez = 0
        while vez < len(mesa.jogadores):
            carta_escolhida = mesa.jogadores[jogador_da_vez(quem_comeca,vez,len(mesa.jogadores))].\
                escolhe_carta_para_jogar(mesa.carta_da_mesa, mesa.cartas_jogadas)

            mesa.atualiza_cartas_jogadas\
                (mesa.jogadores[jogador_da_vez(quem_comeca,vez,len(mesa.jogadores))],
                mesa.jogadores[jogador_da_vez(quem_comeca,vez,len(mesa.jogadores))].\
                    retirar_carta_da_mao(carta_escolhida),vez)

        
            vez += 1

        quem_comeca = mesa.jogadores.index(mesa.encerra_rodada())
        #atualiza o id do jogador que vai começar a próxima rodada com base em quem levou a mesa
        ## Descomentar a linha seguinte quando for jogar!
        #mesa.imprimir_pontos()
        if (len(mesa) != 0):
            # Ainda não acabou as cartas do baralho
            for pos in range(len(mesa.jogadores)):
                mesa.puxar_uma_carta(jogador_da_vez(quem_comeca, pos,len(mesa.jogadores)))
                # para que os jogadores comprem na ordem.
    
    if mesa._equipe_A[0]._pilha_de_pontos.contar_pontos() > 60:

        return 'A'
    elif mesa._equipe_B[0]._pilha_de_pontos.contar_pontos() > 60:

        return 'B'
    else:

        return 'E'



if (__name__ == "__main__"):
    main()