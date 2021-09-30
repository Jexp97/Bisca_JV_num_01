###################################################
# Arquivo base para jogos que usem cartas e baralho.
# Autor: João Vitor da Costa Leal
# Ano: 2021
###################################################

from random import shuffle

class Carta:
    # Uma classe para definir o que é uma carta.
    def __init__(self, naipe, numero, pontos=0):
        # naipe: PAUS; OUROS; COPAS; ESPADAS
        # numero: A(1),2,3,...,J,Q,K
        #pontos: depende do jogo. Por padrão, todos vão receber 0.
        self.__naipe = naipe # Do tipo string
        self.__numero = numero # Do tipo string
        self.__pontos = pontos # Do tipo integer

    @property
    def naipe(self):
        # retorna o naipe da carta
        return self.__naipe

    @property
    def numero(self):
        # retorna o numero da carta
        return self.__numero

    @property
    def pontos(self):
        # retorna a quantidade de pontos da carta
        return self.__pontos

    def __str__(self):
        # retorna o número e o naipe da carta. Por exemplo, 3.OUROS
        # lembrando que tanto _numero quanto _naipe são strings.
        return self.__numero + '.' + self.__naipe



class Baralho:
    # Um baralho é composto por cartas. Aqui, a base é o baralho francês.
    # Esta classe usa a classe Carta e servirá como base para outras classes a herdarem.

    def __init__(self):
        # O atributo cartas_no_baralho guarda a sequência de cartas que compõem o baralho.
        self._cartas_no_baralho = []
        self._naipes = ("ESPADAS", "PAUS", "COPAS", "OUROS")
        self._numeros = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "Joker")

    def embaralhar(self):
        #Esta função embaralha a sequência do atributo cartas_no_baralho. É necessário importar o módulo random do python.
        shuffle(self._cartas_no_baralho)

    def tirar_uma_carta(self, posicao=None):
        # Esta função tira a carta do topo do baralho na posição indicada e o devolve.
        if (posicao != None):
            return self._cartas_no_baralho.pop(posicao)
        else:
            return self._cartas_no_baralho.pop()
    
    def __len__(self):
        # Vai devolver o comprimento de __cartas_no_baralho.
        return len(self._cartas_no_baralho)
    
    def __str__(self):
        # Vai devolver o conteúdo do baralho
        conteudo_do_baralho = ""
        for carta in self._cartas_no_baralho:
            conteudo_do_baralho = (carta.__str__() + "\n") + conteudo_do_baralho

        return conteudo_do_baralho

    def contar_pontos(self):
        # somar a quantidade de pontos no baralho
        pontos = 0
        for carta in self._cartas_no_baralho:
            pontos += carta.pontos

        return pontos

    def adicionar_carta(self, carta):
        # adicionando uma carta à pilha
        self._cartas_no_baralho.append(carta)


class BaralhoDeBisca(Baralho):
    def __init__(self, n_par_de_jogadores = True):
        # Um baralho de bisca contém 40 cartas (baralho sujo) e, caso o número de jogadores
        # seja ímpar, as cartas de 2 devem ser retiradas.
        super().__init__()
        self._numeros = ["A", "2", "3", "4", "5", "6", "7", "J", "Q", "K"]
        self._pontos = {"A": 11, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 10, "J": 3, "Q": 2, "K": 4}

        #criando o baralho
        if (not n_par_de_jogadores):
            # removendo '2' dos _numeros
            self._numeros.remove('2')
            
        for naipe in self._naipes:
            for numero in self._numeros:
                self._cartas_no_baralho.append(Carta(naipe,numero,self._pontos[numero]))
        
        
class Jogador:
    # Classe base para jogadores
    def __init__(self, nome):
        self._nome = nome
        self._pontos = 0

    @property
    def nome(self):
        return self._nome

    @property
    def pontos(self):
        return self._pontos

    @pontos.setter
    def pontos(self, novos_pontos):
        self._pontos = novos_pontos

    def somar_pontos(self, novos_pontos):
        # novos_pontos pode ser tanto positivo quanto negativo!!
        soma = self._pontos + novos_pontos
        if (soma > 0):
            self._pontos = soma
        else:
            self.pontos = 0


class JogadorDeBisca(Jogador):
    # Classe a ser usada para o jogador de bisca
    tamanho_max_mao = 3

    def __init__(self, nome):
        super().__init__(nome)
        # Lista vai guardar o conteúdo da mão
        self._mao = []
        # Variável do tipo Baralho vai guardar a pilha de pontos (cartas)
        self._pilha_de_pontos = Baralho() 
        
    def adicionar_carta_na_mao(self, carta):
        # carta deve ser do tipo Carta
        self._mao.append(carta)

    def retirar_carta_da_mao(self, posicao):
        # vai retirar a carta da mão na posição marcada pelo parâmetro posicao
        return self._mao.pop(int(posicao) - 1)
    
    def __str__(self):
        # Vai devolver uma string com o conteúdo da mão em um formato adequado.
        conteudo_da_mao = ""
        for carta in self._mao:
            conteudo_da_mao = conteudo_da_mao + (carta.__str__() + " ")

        return conteudo_da_mao

    @property
    def pilha_de_pontos(self):
        return self._pilha_de_pontos

    def adicionar_carta_na_pilha (self, carta):
        # adiciona uma carta na pilha de pontos
        self._pilha_de_pontos.adicionar_carta(carta)

    def __len__(self):
        # devolve o comprimento da lista _mao
        return len(self._mao)


class MesaDeBisca():
    # Classe a ser usada como base ao jogo de bisca
    def __init__(self, numero_de_jogadores):
        self._baralho = None #BaralhoDeBisca()
        self._numero_de_jogadores = numero_de_jogadores
        self._jogadores = []
        self._cartas_jogadas = ['' for p in range(numero_de_jogadores)]
        self._quem_jogou_as_cartas = ['' for p in range(numero_de_jogadores)]
        #A ideia é que o nome do jogador apareça em _quem_jogou_as_cartas
        #A partir de sua posição, pegar a carta jogada
        self._carta_da_mesa = None
        # A ideia é usar o parâmetro do número de jogadores para o jogo saber quando pode começar
        # _jogadores deve ser uma lista com _numero_de_jogadores JogadorDeBisca
        self._equipe_A = []
        self._pontos_A = 0
        self._equipe_B = []
        self._pontos_B = 0
        # Após completar a lista _jogadores, as listas _equipe_? vão ser preenchidas

    def adicionar_jogador(self, nome):
        # função a ser chamada para preencher a lista de jogadores
        if (len(self._jogadores) < self._numero_de_jogadores):
            self._jogadores.append(JogadorDeBisca(nome))
        else:
            print("Não é possível adicionar mais jogadores!")


    def dividir_equipes(self):
        # função a ser chamada para preencher as listas de equipes
        if (len(self._jogadores) == self._numero_de_jogadores):
            # adiciona na equipe A os jogadores que estiverem em uma ordem PAR na lista de jogadores
            self._equipe_A = \
                [player for player in self._jogadores if ((self._jogadores.index(player)% 2) == 0)]
            # adiciona na equipe B os jogadores que estiverem em uma ordem ÍMPAR na lista de jogadores
            self._equipe_B = \
                [player for player in self._jogadores if ((self._jogadores.index(player)% 2) != 0)]
        else:
            print("A lista de jogadores precisa estar completa!")
    
    @property
    def jogadores(self):
        return self._jogadores

    def __len__(self):
        return self._baralho.__len__()


    def puxar_uma_carta(self, index_do_jogador):
        # função para tirar uma carta do baralho (ou da mesa) e passar para o jogador
        # preciso passar a posição do jogador na lista de jogadores
        
        if (len(self._baralho) > 0):
            # ainda há cartas no baralho
            carta = self._baralho.tirar_uma_carta()
            self._jogadores[index_do_jogador].adicionar_carta_na_mao(carta)
        else:
            # crio uma cópia da carta da mesa e dou ao jogador
            # esta condição só deve ocorrer uma única vez!!!
            carta = Carta(self._carta_da_mesa.naipe, self._carta_da_mesa.numero)
            self._jogadores[index_do_jogador].adicionar_carta_na_mao(carta) 
    
    def mostrar_carta_do_jogador(self, index_do_jogador):
        # mostra as cartas do jogador identificado por index_do_jogador (posição da lista de jogadores)
        print(self._jogadores[index_do_jogador].nome)
        print(self._jogadores[index_do_jogador])

    def prepara_a_mesa(self):
        # função para gerar o baralho, preencher a carta da mesa e dar 3 cartas iniciais aos jogadores
        self._baralho = BaralhoDeBisca(self._numero_de_jogadores % 2 == 0)
        self._baralho.embaralhar()
        self._carta_da_mesa = self._baralho.tirar_uma_carta()

        for player in self._jogadores:
            while (len(player) < JogadorDeBisca.tamanho_max_mao):
                # vai dando cartas ao jogador até preencher 3 na mão
                self.puxar_uma_carta(self._jogadores.index(player))
    
    
    def atualiza_cartas_jogadas(self, player, carta_jogada, vez):
        # adiciona na lista de jogadas um elemento do tipo [jogador, carta_jogada]
        # vez indica a posição nas listas. Vai de 0 a numero_de_jogadores-1
        if (vez < self._numero_de_jogadores):
            self._quem_jogou_as_cartas[vez] = player
            self._cartas_jogadas[vez] = carta_jogada
        else:
            print("Erro! O número excedeu a quantidade de jogadores!")

    
    def encerra_rodada (self):

        # identifica quem jogou a carta mais forte e retorna o nome para que o jogo saiba quem começa depois
        pos = 0 #qual a posição em cartas_jogadas
        jogador_mais_forte = None
        carta_mais_forte = self._cartas_jogadas[pos] # qual a carta para efeito de comparação
        for jogada in self._cartas_jogadas: #tá preenchendo errado o cartas_jogadas
            if jogada.naipe == carta_mais_forte.naipe:
                # se o naipe for igual, quem define a mais forte é a pontuação
                if jogada.pontos >= carta_mais_forte.pontos:
                    carta_mais_forte = jogada
                    jogador_mais_forte = self._quem_jogou_as_cartas[pos] #jogador
            else: #naipes diferentes
                # se o naipe é diferente, preciso verificar se a nova carta verificada é da mesa
                if jogada.naipe == self._carta_da_mesa.naipe:
                    carta_mais_forte = jogada
                    jogador_mais_forte = self._quem_jogou_as_cartas[pos] #jogador
            pos += 1

        if jogador_mais_forte in self._equipe_A:
            # se o jogador da carta mais forte da rodada está na equipe A
            for carta in self._cartas_jogadas:
                # adicionar cada carta das jogadas na pilha de pontos dos jogadores da equipe A
                for jogador in self._equipe_A:
                    jogador.adicionar_carta_na_pilha(carta)
        else:
            # se o jogador da carta mais forte da rodada está na equipe B
            for carta in self._cartas_jogadas:
                # adicionar cada carta das jogadas na pilha de pontos dos jogadores da equipe B
                for jogador in self._equipe_B:
                    jogador.adicionar_carta_na_pilha(carta)   

        self._cartas_jogadas = ['' for p in range(self._numero_de_jogadores)] 
        # esvaziar a lista de cartas jogadas
        self._quem_jogou_as_cartas = ['' for p in range(self._numero_de_jogadores)] 
        # esvaziar a lista de quem jogou as cartas

        return jogador_mais_forte 
    
    def acabou_jogo(self):
        # verifica se a mão de todos os jogadores esvaziou. Se sim, retorna True.
        # Caso contrário, retorna False.
        acabou_jogo = True
        for jogador in self._jogadores:
            if (len(jogador) != 0):
                acabou_jogo = False
                break
        
        return acabou_jogo

    def imprimir_mesa(self):
        # método para imprimir o conteúdo da mesa
        if self._numero_de_jogadores == 2:
            print (self._jogadores[0].nome) # nome do jogador
            print (self._cartas_jogadas\
                [self._quem_jogou_as_cartas.index(self._jogadores[0].nome)]\
                    .__str__()) # tipo Carta !!!!
            print ('\n\n')
            print('Mesa: {}'.format(self._carta_da_mesa.__str__()))
            print ('\n\n')
            print (self._jogadores[1].nome) # nome do jogador
            print (self._cartas_jogadas\
                [self._quem_jogou_as_cartas.index(self._jogadores[1].nome)]\
                    .__str__()) # tipo Carta
        
        elif self._numero_de_jogadores == 3:
            print (self._jogadores[0].nome) # nome do jogador
            print (self._cartas_jogadas\
                [self._quem_jogou_as_cartas.index(self._jogadores[0].nome)]\
                    .__str__()) # tipo Carta
            print ('\n\n')
            print('Mesa: {}'.format(self._carta_da_mesa.__str__()))
            print ('\n\n')
            print ('{} || {}'.format
            (self._jogadores[1].nome, self._jogadores[2].nome)) 
            # nome do jogador
            print ('{} || {}'.format
            (self._cartas_jogadas[self._quem_jogou_as_cartas.index(self._jogadores[1].nome)]\
                .__str__(), self._cartas_jogadas\
                    [self._quem_jogou_as_cartas.index(self._jogadores[2].nome)].__str__()))
             # tipo Carta
        
        elif self._numero_de_jogadores == 4:
            print ('\n{} || {}'.format
            (self._jogadores[0].nome, self._jogadores[1].nome)) 
            # nome do jogador fixado
            try:
                print('{} || '.format(self._cartas_jogadas\
                    [self._quem_jogou_as_cartas.index(self._jogadores[0])].__str__()), end='')
            except:
                print('   || ', end='')
            
            try:
                print('{}'.format(self._cartas_jogadas\
                    [self._quem_jogou_as_cartas.index(self._jogadores[1])].__str__()))
            except:
                print('   ')

            print ('\n\n')
            print('Mesa: {} ({})'.format(self._carta_da_mesa.__str__(), len(self._baralho)))
            print ('\n\n')
            print ('{} || {}'.format
            (self._jogadores[3].nome, self._jogadores[2].nome)) # invertido!!
            # nome do jogador
            try:
                print('{} || '.format(self._cartas_jogadas\
                    [self._quem_jogou_as_cartas.index(self._jogadores[3])].__str__()), end='')
            except:
                print('   || ', end='')
            
            try:
                print('{}'.format(self._cartas_jogadas\
                    [self._quem_jogou_as_cartas.index(self._jogadores[2])].__str__()))
            except:
                print('   ')
            print ('\n\n')

        # Pode ter mais, porém vou parar em 4 por enquanto
    
    def imprimir_pontos(self):
        # método para exibir os pontos em formato de tabela
        print('\n.----------------------------------------.')
        print('|------------TABELA DE PONTOS------------|')
        print('|----------------------------------------|')
        print('|                                        |')
        print('|  EQUIPE A             {:03d} pontos       |'.format\
            (self._equipe_A[0]._pilha_de_pontos.contar_pontos()))
        print('|                                        |')
        print('|  EQUIPE B             {:03d} pontos       |'.format\
            (self._equipe_B[0]._pilha_de_pontos.contar_pontos()))
        print('.----------------------------------------.')
        print('\n')
