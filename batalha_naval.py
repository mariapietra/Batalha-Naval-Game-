from ast import Break
import time

print('\n    💥💥💥 BATALHA NAVAL 💥💥💥    \n')
time.sleep(0.8)

print('\n Bem vindo(a) ao Batalha Naval, vamos jogar!!! \n')
time.sleep(0.8)

nLinhas = nColunas = 20
legenda_horizontal = '   1  2  3  4  5  6  7   8   9   10  11  12  13  14  15  16  17  18  19  20'
legenda_vertical = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T']
posicoes_ataque = []
posicoes_acerto = []
pontuacao = 0
acerto_pa = 0
acerto_cr = 0
acerto_fr = 0

def gera_tabuleiro():
    matriz = ['💧'] * nLinhas
    for linha in range(nLinhas):
        matriz[linha] = ['💧'] * nColunas
    return matriz

def imprimir_tabuleiro(tabuleiro):
    linha_tabuleiro = ''
    print(legenda_horizontal)

    for linha in range(nLinhas):
        linha_tabuleiro += legenda_vertical[linha] + '  '
        for coluna in range(nColunas):
            linha_tabuleiro += tabuleiro[linha][coluna] + '  '
        linha_tabuleiro += legenda_vertical[linha] + '  '
        print(linha_tabuleiro)
        linha_tabuleiro = ''
    print(legenda_horizontal)

def acha_linha(letra):
    for index in range(nColunas):
        if(legenda_vertical[index] == letra):
            return index
    return -1


def pega_posição():
    linha = input('informe a linha (A - T) : ')
    linha = acha_linha(linha)
    while linha == -1:
        print('valor invalido digite novamente')
        linha = input('informe a linha (A - T) : ')
        linha = acha_linha(linha)
    
    coluna = int(input('informe a coluna (1 - 20) : ')) -1
    while coluna < 0 or coluna > 18:
        print('valor invalido, digite novamente')
        coluna = int(input('informe a coluna (1 - 20) : ')) -1
    
    print(linha, coluna)
    return [linha, coluna]
    

def valida_posição(tabuleiro, navio, linha, coluna):
    if navio == 'porta_aviao':
        if coluna + 3 > 19:
            return False
        elif (tabuleiro[linha][coluna] != '💧' or tabuleiro[linha][coluna+1] != '💧' or tabuleiro[linha][coluna+2] != '💧' or tabuleiro[linha][coluna+3] != '💧'):
            return False
    
    elif navio == 'cruzador':
        if coluna + 2 > 19:
            return False
        elif (tabuleiro[linha][coluna] != '💧' or tabuleiro[linha][coluna+1] != '💧'or tabuleiro[linha][coluna+2] != '💧'):
            return False
    
    elif navio == 'fragata':
        if coluna + 1 > 19:
            return False
        elif (tabuleiro[linha][coluna] != '💧' or tabuleiro[linha][coluna+1] != '💧'):
            return False
    
    return True

def preenche_tabuleiro_defesa(tabuleiro):
    for navio in range(12):
        if navio < 3:
            print('\n --Posicione o Porta-Aviao 🚢-- \n')
            linha, coluna = pega_posição()
            while not valida_posição(tabuleiro, 'porta_aviao', linha, coluna):
                print('\n Posição invalida, o navio não cabe ou ja esta preenchida \n\n --Posicione o Porta-Aviao 🚢-- \n')
                linha, coluna = pega_posição()
            tabuleiro[linha][coluna] = '🚢'
            tabuleiro[linha][coluna + 1] = '🚢'
            tabuleiro[linha][coluna + 2] = '🚢'
            tabuleiro[linha][coluna + 3] = '🚢'
            imprimir_tabuleiro(tabuleiro)
        
            

        elif navio < 7:
            print('\n --Posicione o cruzador 🛳️ -- \n')
            linha, coluna = pega_posição()
            while not valida_posição(tabuleiro, 'cruzador', linha, coluna):
                print('\n Posição invalida, o navio não cabe ou ja esta preenchida \n\n --Posicione o cruzador 🛳️ -- \n')
                linha, coluna = pega_posição()
            tabuleiro[linha][coluna] = '🛳️'
            tabuleiro[linha][coluna + 1] = '🛳️'
            tabuleiro[linha][coluna + 2] = '🛳️'
            imprimir_tabuleiro(tabuleiro)
            

        else:
            print('\n --Posicione a fragata ⛵-- \n')
            linha, coluna = pega_posição()
            while not valida_posição(tabuleiro, 'fragata', linha, coluna):
                print('\n Posição invalida, o navio não cabe ou ja esta preenchida \n\n--Posicione a fragata ⛵-- \n')
                linha, coluna = pega_posição()
            tabuleiro[linha][coluna] = '⛵'
            tabuleiro[linha][coluna + 1] = '⛵'
            imprimir_tabuleiro(tabuleiro)
    imprimir_tabuleiro(tabuleiro)

def valida_ataque(linha, coluna):
    for posicao in posicoes_ataque:
        if posicao[0] == linha and posicao[1] == coluna:
            return False
    return True

def ataca_navio(tabuleiro_defesa, tabuleiro_ataque):
    linha, coluna = pega_posição()
    while not valida_ataque(linha, coluna):
        print('\n --Voce ja atacou essa posicao-- \n')
        linha, coluna = pega_posição()
    
    posicoes_ataque.append([linha, coluna])
    
    if(tabuleiro_defesa[linha][coluna] != '💧'):
        tabuleiro_ataque[linha][coluna] = '💥'
        posicoes_acerto.append([linha,coluna])
        pontos(tabuleiro_defesa[linha][coluna])
    
    else:    
        tabuleiro_ataque[linha][coluna] = '❌'


def pontos(navio):
    global acerto_pa, acerto_cr, acerto_fr, pontuacao
    
    if navio == '🚢':
        acerto_pa += 1
        if acerto_pa % 4 == 0:
            pontuacao += 30
    
    elif navio == '🛳️':
        acerto_cr += 1
        if acerto_cr % 3 == 0:
            pontuacao += 20
    
    else:
        acerto_fr += 1
        if acerto_fr % 2 == 0:
            pontuacao += 10
    
    

tabuleiro_defesa = gera_tabuleiro()
imprimir_tabuleiro(tabuleiro_defesa)
time.sleep(0.8)
preenche_tabuleiro_defesa(tabuleiro_defesa)
tabuleiro_ataque = gera_tabuleiro()

for cont in range(500):
    print()
print('\n 💥HORA DO ATAQUE💥 \n')
for cont in range(400):
    ataca_navio(tabuleiro_defesa, tabuleiro_ataque)
    imprimir_tabuleiro(tabuleiro_ataque)
    print('\n Sua pontuaçao:', pontuacao)
    if len(posicoes_acerto) == 34:
        print('\n 💣Voce naufragou todas as embarcaçoes!!!💣 \n')
        time.sleep(0.8)
        print('\n ✨Parabens, voce ganhou✨ \n')
    Break
