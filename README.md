# Bisca_JV_num_01
Código Python para rodar o jogo "Bisca", feito enquanto aprendo a utilizar a linguagem.
Autor: João Leal

Sobre:

Trata-se de uma implementação em Python do jogo de cartas “Bisca”. Para mais informações de como o jogo funciona, acesse a página da Wikipedia (https://pt.wikipedia.org/wiki/Bisca).
O intuito deste código foi de treinamento na linguagem Python enquanto gera-se um jogo para o computador 
(embora ele ainda não seja muito divertido com os jogadores “dummies” – máquina – não tendo uma implementação muito adequada ainda;
o desenvolvimento de um melhor jogador virtual por meio de aprendizado de máquina foi iniciado, mas o treinamento da rede neural ainda não está entregando bons resultados).

Arquivos:

Apesar de o projeto ter vários arquivos, a maioria deles se referem ao treinamento da rede neural do jogador virtual “mais esperto”, que ainda não está bem implementado. 
Assim, para jogar uma partida, basta ter os arquivos bisca.py e classes_base.py no mesmo diretório, chamando o primeiro em um terminal. Por exemplo:

C:\...\diretorio_onde_os_programas_foram_salvos\python bisca.py

Jogo:

Ao chamar o programa bisca.py, a primeira coisa que ele irá fazer é perguntar se o jogador atual será um humano (opção 1 no teclado) ou um dummy (opção 2 no teclado). 
Como foi implementado uma partida de quatro jogadores, a ordem em que será preenchido será o jogador 1 (Jog. 1) seguido do 2 (Jog. 2), do 3 (Jog. 3) e, por último, do 4 (Jog. 4).
É possível escolher um humano para todos eles, só não fará sentido uma vez que você mesmo teria de jogar por todos (afinal de contas, esse é um programa simples que não faz
uma conexão em rede com outras máquinas).
Quando todos os quatro jogadores estiverem preenchidos, a mesa será iniciada e o Jog. 1 será o primeiro a jogar. A carta da mesa é destacada no centro e as cartas na mão
estão mais abaixo da tela. Para escolher a carta a jogar, digite 1, 2 ou 3, de acordo com a ordem em que as opções aparecem da esquerda para a direita. 
Atente-se que, nas últimas rodadas, a quantidade de cartas na mão vai diminuído, o que vai restringindo as opções numéricas até acabar as cartas na mão.
Na vez de outros jogadores que tiverem sido escolhidos como dummies, não haverá nenhuma escolha a ser feita. Apenas espere suas jogadas.
Ao fim de cada rodada, a pontuação é contabilizada, o que permite acompanhar o andamento do jogo e ver qual equipe está vencendo. A Equipe A é composta dos 
jogadores Jog.1 e Jog.3, enquanto que a Equipe B dos jogadores Jog. 2 e Jog.4.
De resto, leia a página da wikipédia para saber mais sobre o jogo ou aprenda por tentativa e erro. Na medida do possível, divirta-se!

