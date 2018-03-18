import pygame
from random import randint

# Cores
white = (255, 255, 255)
slategray = (198, 226, 255)
salmon = (198, 113, 113)
red = (255, 0, 0)
black = (0, 0, 0)

# Inicialização Pygame
try:
    pygame.init()
    except pygame.error:
    print('O modulo pygame nao foi iniciado')
    
# Tamanho Tela e Cobra
largura = 320
altura = 240
tamanho = 10

relogio = pygame.time.Clock()  # FPS (Velocidade Cobra)
fundo = pygame.display.set_mode((largura, altura))  # Tamanho tela
pygame.display.set_caption('Py.Snake')  # Titulo janela
font = pygame.font.SysFont(None, 15)  # Estilo e tamanho da fonte


# Função texto
def texto(msg, cor):
    texto1 = font.render(msg, True, cor)
    fundo.blit(texto1, [largura / 10, altura / 2])


# Função colisão
def cobra(CobraXY):
    for XY in CobraXY:
        pygame.draw.rect(fundo, white, [XY[0], XY[1], tamanho, tamanho])


# Função maça
def apple(pos_x, pos_y):
    pygame.draw.rect(fundo, red, [pos_x, pos_y, tamanho, tamanho])


# Função jogo
def jogo():
    sair = True
    fimdejogo = False
    pos_x = randint(0, (largura - tamanho) / 10) * 10
    pos_y = randint(0, (altura - tamanho) / 10) * 10
    apple_x = randint(0, (largura - tamanho) / 10) * 10
    apple_y = randint(0, (altura - tamanho) / 10) * 10
    velocidade_x = 0
    velocidade_y = 0
    CobraXY = []
    cobraComp = 1


# Game Over
    while sair:
        while fimdejogo:
            fundo.fill(black)
            texto("Fim de jogo, para continuar clique C ou S para sair!", slategray)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sair = False
                    fimdejogo = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        jogo()
                    if event.key == pygame.K_s:
                        sair = False
                        fimdejogo = False

        # (Movimentos)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and velocidade_x != tamanho:
                    velocidade_y = 0
                    velocidade_x = -tamanho
                if event.key == pygame.K_RIGHT and velocidade_x != -tamanho:
                    velocidade_y = 0
                    velocidade_x = tamanho
                if event.key == pygame.K_UP and velocidade_y != tamanho:
                    velocidade_x = 0
                    velocidade_y = -tamanho
                if event.key == pygame.K_DOWN and velocidade_y != -tamanho:
                    velocidade_x = 0
                    velocidade_y = tamanho

        fundo.fill(black)
        pos_x += velocidade_x
        pos_y += velocidade_y

        # Frente da cobra
        CobraInicio = []
        CobraInicio.append(pos_x)
        CobraInicio.append(pos_y)
        CobraXY.append(CobraInicio)
        if len(CobraXY) > cobraComp:
            del CobraXY[0]

        # Colisão
        if any(Bloco == CobraInicio for Bloco in CobraXY[:-1]):
            fimdejogo = True

        # Incrementação do comprimeto
        cobra(CobraXY)
        if pos_x == apple_x and pos_y == apple_y:
            apple_x = randint(0, (largura - tamanho) / 10) * 10
            apple_y = randint(0, (altura - tamanho) / 10) * 10
            cobraComp += 1

        apple(apple_x, apple_y)
        pygame.display.update()
        relogio.tick(20)

        # Bordas
        if pos_x > largura:
            pos_x = 0
        if pos_x < 0:
            pos_x = largura - tamanho
        if pos_y > altura:
            pos_y = 0
        if pos_y < 0:
            pos_y = altura - tamanho


jogo()
pygame.QUIT()
