# made by @SAILOGGO

import os, sys

dirpath = os.getcwd()
sys.path.append(dirpath)
if getattr(sys, "frozen", False):
    os.chdir(sys._MEIPASS)

from random import randint
import pygame
import math
from pygame import mixer

pygame.init()
screen = pygame.display.set_mode((800, 600))
# arquivos e imagens

intro = pygame.image.load('intro.png')
intro1 = pygame.image.load('intro1.png')
intro2 = pygame.image.load('intro2.png')
intro3 = pygame.image.load('intro3.png')
intro4 = pygame.image.load('intro4.png')
intro5 = pygame.image.load('intro5.png')
intro6 = pygame.image.load('intro6.png')
intro7 = pygame.image.load('intro7.png')

dababby = pygame.image.load('boss.png')
righthandimg = pygame.image.load('righthand.png')
lefthandimg = pygame.image.load('lefthand.png')
dababbyrightimg = pygame.image.load('bossright.png')
bossheadimg = pygame.image.load('bosshead.png')
bossmouthimg = pygame.image.load('bossopenmouth.png')
handkeanaoimg = pygame.image.load('handkeanao2.png')

backgroud = pygame.image.load('fundo.png')
backgroud2 = pygame.image.load('fundo2.png')
morreuimg = pygame.image.load('morreu.png')
viveuimg = pygame.image.load('goodending.png')
easterimg = pygame.image.load('easteregg.png')

keanuimg = pygame.image.load('keanão.png')
keanuimg2 = pygame.image.load('keanão.png')
keanuimg3 = pygame.image.load('keanão.png')
keanufall = pygame.image.load('keanufall.png')
keanozookaimg = pygame.image.load('keanãobzooka.png')
keanozooka2img = pygame.image.load('keanãoreloading.png')
keanufalldamageimg = pygame.image.load('keanufalldamage.png')

enemyimg1 = pygame.image.load('bola-de-canhao.png')
enemyimg2 = pygame.image.load('homi-das-carça.png')
enemyimg3 = pygame.image.load('amongusdrip.png')
enemyimg4 = pygame.image.load('relampago-barro.png')

balaimg = pygame.image.load('bala.png')
armaimg = pygame.image.load('bzooka64.png')

pygame.display.set_caption('KEANÂO THE GAME By @Sailoggo')
pygame.display.set_icon(keanuimg)

running = True
cutscene = True
quiz = True
play = True
goodending = False
badending = False
easteregg = False

backy = -4800
backy_change = 0
backx = -550
backx_change = 0

morreux = morreuy = 0
introx = 0
introy = 530
space = 0
enemy_count = 0
armacollect = 0
x_range_count = 0
damageboss = 0

# posisões dos objetos
keanux = -100
keanux2 = 0
keanuy = 365
keanuy2 = 0
keanuy_change = 0
keanux_change = 0

balax = 0
balay = 365
balax_change = 0
balay_change = 0
bala_state = 'ready'

armax = 30
armay = keanuy

enemy1x = randint(0, 736)
enemy1y = -64
enemy1y_move = 0

enemy2x = randint(0, 736)
enemy2y = -64
enemy2y_move = 0

enemy3x = randint(0, 736)
enemy3y = -64
enemy3y_move = 0

enemy4x = randint(0, 736)
enemy4y = -64
enemy4y_move = 0

bossx = 230
bossy = -590
bossx_change = 0
bossy_change = 0
boss_cut = 0
boss_h = 0
bosshitwall = 0

handattackx = 415
handattacky = 147
handattackx_change = 0
handattacky_change = 0

handattacky2 = 147
handattackx2 = 215
handattackx2_change = 0
handattacky2_change = 0


# defs
def keanao(x, y):
    screen.blit(keanuimg, (x, y))


def keanufally(x, y):
    screen.blit(keanufall, (x, y))


def keanufallydamage(x, y):
    screen.blit(keanufalldamageimg, (x, y))


def keanaozooka(x, y):
    screen.blit(keanozookaimg, (x, y))


def keanaozooka2(x, y):
    screen.blit(keanozooka2img, (x, y))


def bala(x, y):
    global bala_state
    bala_state = 'fire'
    screen.blit(balaimg, (x + 20, y + 37))


def arma(x, y):
    screen.blit(armaimg, (x, y))


def enemy1(x, y):
    screen.blit(enemyimg1, (x, y))


def enemy2(x, y):
    screen.blit(enemyimg2, (x, y))


def enemy3(x, y):
    screen.blit(enemyimg3, (x, y))


def enemy4(x, y):
    screen.blit(enemyimg4, (x, y))


def boss1(x, y):
    screen.blit(dababby, (x, y))


def boss2(x, y):
    screen.blit(dababby, (x, y))


def righthand(x, y):
    screen.blit(righthandimg, (x, y))


def lefthand(x, y):
    screen.blit(lefthandimg, (x, y))


def handkeanao(x, y):
    screen.blit(handkeanaoimg, (x, y))


def colision(enemy1x, enemy1y, keanux, keanuy):
    distance = math.sqrt((math.pow(enemy1x - keanux, 2)) + (math.pow(enemy1y - keanuy, 2)))
    if distance < 64:
        return True
    else:
        return False


def colisiongun(balax, balay, bossx, bossy):
    distance = math.sqrt((math.pow(balax - bossx, 2)) + (math.pow(balay - bossy, 2)))
    if distance < 190:
        return True
    else:
        return False


def colisionboss(handattackx, handattacky, keanux, keanuy):
    distance = math.sqrt((math.pow(handattackx - keanux, 2)) + (math.pow(handattacky - keanuy, 2)))
    if distance < 95:
        return True
    else:
        return False


def morreu(x, y):
    screen.blit(morreuimg, (x, y))


def viveu(x, y):
    screen.blit(viveuimg, (x, y))


def egg(x, y):
    screen.blit(easterimg, (x, y))


while play:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                intro = pygame.image.load('intro.png')
                intro1 = pygame.image.load('intro1.png')
                intro2 = pygame.image.load('intro2.png')
                intro3 = pygame.image.load('intro3.png')
                intro4 = pygame.image.load('intro4.png')
                intro5 = pygame.image.load('intro5.png')
                intro6 = pygame.image.load('intro6.png')
                intro7 = pygame.image.load('intro7.png')

                dababby = pygame.image.load('boss.png')
                righthandimg = pygame.image.load('righthand.png')
                lefthandimg = pygame.image.load('lefthand.png')
                dababbyrightimg = pygame.image.load('bossright.png')
                bossheadimg = pygame.image.load('bosshead.png')
                bossmouthimg = pygame.image.load('bossopenmouth.png')
                handkeanaoimg = pygame.image.load('handkeanao2.png')

                backgroud = pygame.image.load('fundo.png')
                backgroud2 = pygame.image.load('fundo2.png')
                morreuimg = pygame.image.load('morreu.png')
                viveuimg = pygame.image.load('goodending.png')
                easterimg = pygame.image.load('easteregg.png')

                keanuimg = pygame.image.load('keanão.png')
                keanuimg2 = pygame.image.load('keanão.png')
                keanuimg3 = pygame.image.load('keanão.png')
                keanufall = pygame.image.load('keanufall.png')
                keanozookaimg = pygame.image.load('keanãobzooka.png')
                keanozooka2img = pygame.image.load('keanãoreloading.png')
                keanufalldamageimg = pygame.image.load('keanufalldamage.png')

                enemyimg1 = pygame.image.load('bola-de-canhao.png')
                enemyimg2 = pygame.image.load('homi-das-carça.png')
                enemyimg3 = pygame.image.load('amongusdrip.png')
                enemyimg4 = pygame.image.load('relampago-barro.png')

                balaimg = pygame.image.load('bala.png')
                armaimg = pygame.image.load('bzooka64.png')

                running = True
                cutscene = True
                quiz = True
                play = True
                goodending = False
                badending = False
                easteregg = False

                backy = -4800
                backy_change = 0
                backx = -550
                backx_change = 0

                morreux = morreuy = 0
                introx = 0
                introy = 530
                space = 0
                enemy_count = 0
                armacollect = 0
                x_range_count = 0
                damageboss = 0

                # posisões dos objetos
                keanux = -100
                keanux2 = 0
                keanuy = 365
                keanuy2 = 0
                keanuy_change = 0
                keanux_change = 0

                balax = 0
                balay = 365
                balax_change = 0
                balay_change = 0
                bala_state = 'ready'

                armax = 30
                armay = keanuy

                enemy1x = randint(0, 736)
                enemy1y = -64
                enemy1y_move = 0

                enemy2x = randint(0, 736)
                enemy2y = -64
                enemy2y_move = 0

                enemy3x = randint(0, 736)
                enemy3y = -64
                enemy3y_move = 0

                enemy4x = randint(0, 736)
                enemy4y = -64
                enemy4y_move = 0

                bossx = 230
                bossy = -590
                bossx_change = 0
                bossy_change = 0
                boss_cut = 0
                boss_h = 0
                bosshitwall = 0

                handattackx = 415
                handattacky = 147
                handattackx_change = 0
                handattacky_change = 0

                handattacky2 = 147
                handattackx2 = 215
                handattackx2_change = 0
                handattacky2_change = 0

    # cutscene ////////////////////////////////////////////////////////////////////////////////////////////////////////

    while cutscene:
        screen.blit(backgroud, (backx, backy))
        screen.blit(intro, (introx, introy))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                cutscene = False
                running = False
                quiz = False
                play = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    space = space + 1
                    if space == 1:
                        intro = intro1
                    elif space == 2:
                        intro = intro2
                        keanux = 270
                        door = mixer.Sound('door.mp3')
                        door.play()
                    elif space == 3:
                        intro = intro3
                        boss_cut = 1
                        lesgou = mixer.Sound('lesgou.mp3')
                        lesgou.play()
                elif event.key == pygame.K_ESCAPE:
                    keanux = 300
                    cutscene = False

        bossy = bossy - bossy_change
        if boss_cut == 1:
            bossy_change = -1
        if bossy == -150:
            bossy_change = 0
            if space == 4:
                intro = intro4
            elif space == 5:
                intro = intro5
            elif space == 6:
                intro = intro6
            elif space == 7:
                intro = intro7
            elif space == 8:
                cutscene = False
        if space <= 4:
            boss1(bossx, bossy)
        elif space >= 5:
            boss2(bossx, bossy)
        keanao(keanux, keanuy)
        pygame.display.update()

    # o jogo ///////////////////////////////////////////////////////////////////////////////////////////////////////////
    while running:
        screen.blit(backgroud2, (backx, backy))
        # movimentação do fundo
        backy = backy - backy_change

        if backy <= -18056:
            backy_change = -5
            enemy1y_move = 4.2
            enemy2y_move = 6.2

        if backy >= -3800:
            backy_change = 0
            keanuimg = keanuimg2
            bossy_change = 3
            if bossy >= 0:
                bossy = 0
                running = False

        # animação do pulo
        if keanux >= 600 and backy == -4800 or keanux <= 140 and backy == -4800:
            backy_change = 7
            keanuimg = keanufall
            boss_h = 1

        # entrada de comandos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                cutscene = False
                quiz = False
                play = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    keanux_change = -2.5
                if event.key == pygame.K_RIGHT:
                    keanux_change = 2.5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE or pygame.K_LEFT or pygame.K_RIGHT:
                    keanuy_change = 0
                    keanux_change = 0

            # colisão da parede
            if keanux > 764:
                easteregg = True
                quiz = False
                running = False
            elif keanux < -32:
                easteregg = True
                quiz = False
                running = False

        # movimentação do jogador
        keanuy = keanuy + keanuy_change
        keanux = keanux + keanux_change

        # movimentação dos inimigos
        enemy1y = enemy1y + enemy1y_move

        if enemy1y >= 740 and not enemy_count >= 21:
            enemy1y = 0
            enemy1x = randint(0, 736)
            enemy_count = enemy_count + 1

        enemy2y = enemy2y + enemy2y_move

        if enemy2y >= 740 and not enemy_count >= 21:
            enemy2y = 0
            enemy2x = randint(0, 736)

        enemy3y = enemy3y + enemy3y_move

        if enemy3y >= 740 and not enemy_count >= 21:
            enemy3y = 0
            enemy3x = randint(0, 736)

        enemy4y = enemy4y + enemy4y_move

        if enemy4y >= 740 and not enemy_count >= 21:
            enemy4y = 0
            enemy4x = randint(0, 736)

        bossx = bossx + bossx_change
        bossy = bossy + bossy_change
        if boss_h == 1:
            bossy_change = -3
        elif boss_h == 0:
            bossy_change = 0
        if bossy <= -590:
            boss_h = 0

        if bossy <= -590 and boss_h == 0 and enemy_count == 0 and backy_change == 7:
            enemy1y_move = 3
        if enemy_count == 5:
            enemy2y_move = 4
        if enemy_count == 12:
            enemy3y_move = 5
        if enemy_count == 17:
            enemy4y_move = 6

        enemy1(enemy1x, enemy1y)
        enemy2(enemy2x, enemy2y)
        enemy3(enemy3x, enemy3y)
        enemy4(enemy4x, enemy4y)
        boss2(bossx, bossy)

        if colision(enemy1x, enemy1y, keanux, keanuy) or colision(enemy2x, enemy2y, keanux, keanuy) \
                or colision(enemy3x, enemy3y, keanux, keanuy) or colision(enemy4x, enemy4y, keanux, keanuy):
            keanufallydamage(keanux, keanuy)
            quiz = False
            running = False
            badending = True
        else:
            keanao(keanux, keanuy)

        pygame.display.update()

    # quiz /////////////////////////////////////////////////////////////////////////////////////////////////////////////

    while quiz:
        screen.blit(backgroud, (backx, backy))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quiz = False
                running = False
                cutscene = False
                play = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    keanux_change = -2.5

                if event.key == pygame.K_RIGHT:
                    keanux_change = 2.5

                if event.key == pygame.K_SPACE:
                    bala(balax, balay)
                    balax = keanux

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or pygame.K_RIGHT:
                    keanuy_change = 0
                    keanux_change = 0

        if keanux > 764:
            easteregg = True
            quiz = False
            running = False
        elif keanux < -32:
            easteregg = True
            quiz = False
            running = False

        balay = balay + balay_change
        keanux = keanux + keanux_change
        bossx = bossx + bossx_change
        bossy += bossy_change
        handattackx += handattackx_change
        handattacky += handattacky_change
        handattackx2 += handattackx2_change
        handattacky2 += handattacky2_change

        # movimentaçao do boss

        if bossx >= 564:
            bossx = 564
            bossx_change = -4
            bosshitwall += 1
        elif bossx <= -64:
            bossx = -64
            bossx_change = 4

        if colisionboss(handattackx, handattacky, keanux, keanuy) or \
                colisionboss(handattackx2, handattacky2, keanux, keanuy):
            badending = True
            quiz = False
        else:
            if damageboss == 5:
                if bossx > 230:
                    bossx_change = -1
                elif bossx < 230:
                    bossx_change = 1
                if bossx == 230:
                    bossx_change = 0
                    righthand(handattackx, handattacky)
                    handattacky_change = 2.5
                    if 336 <= keanux <= 536:
                        handattackx_change = 1.7
                        dababby = dababbyrightimg
                    elif 536 <= keanux <= 800:
                        handattackx_change = 4
                        dababby = dababbyrightimg
                    elif 0 <= keanux <= 136:
                        handattackx_change = -4
                        dababby = dababbyrightimg
                    elif 136 <= keanux <= 336:
                        handattackx_change = -1.7
                        dababby = dababbyrightimg

                if handattacky >= 700:
                    handattackx_change = 0
                    handattacky_change = 0
                    bossx_change = 4
                    damageboss = 6

        if damageboss == 11:
            bossx_change = -1
            if bossx == 230:
                bossx_change = 0
                lefthand(handattackx2, handattacky2)
                handattacky2_change = 2.5
                if 336 <= keanux <= 536:
                    handattackx2_change = 1.7
                    dababby = bossheadimg
                elif 536 <= keanux <= 800:
                    handattackx2_change = 4
                    dababby = bossheadimg
                elif 0 <= keanux <= 136:
                    handattackx2_change = -4
                    dababby = bossheadimg
                elif 136 <= keanux <= 336:
                    handattackx2_change = -1.7
                    dababby = bossheadimg

            if handattacky2 >= 700:
                handattackx2_change = 0
                handattacky2_change = 0
                bossx_change = 4
                damageboss = 12

        if damageboss == 17:
            bossx_change = -4.5
            dababby = bossmouthimg
            if 336 <= keanux <= 536:
                bossy_change = 3
            elif 536 <= keanux <= 800:
                bossy_change = 1
            elif 0 <= keanux <= 136:
                bossy_change = 4
            elif 136 <= keanux <= 336:
                bossy_change = 6

        if colisionboss(keanux, keanuy, bossx, bossy):
            badending = True
        if colisiongun(balax, balay, bossx, bossy):
            balay = keanuy
            bala_state = 'ready'

            # isso aqui é o inferno em pessoa
            damageboss += 1
            if damageboss == 1:
                damageboss = 1
            # nunca mais vou esquecer esse merda na minha vida

        if colisiongun(balax, balay, bossx, bossy) and balay == keanuy and bala_state == 'ready':
            damageboss += 1

        if bossy >= 800:
            quiz = False
            goodending = True

        # sistema da arma

        if balay <= -350:
            balay = keanuy
            bala_state = 'ready'

        if bala_state == 'fire':
            bala(balax, balay)
            balay = balay - 4

        if colision(armax, armay, keanux, keanuy):
            armacollect = 1
            armax = -100
            bossx_change = -3
        else:
            arma(armax, armay)

        if armacollect == 0:
            keanao(keanux, keanuy)

        if armacollect >= 1:
            if bala_state == 'fire':
                keanaozooka2(keanux, keanuy)
            else:
                keanaozooka(keanux, keanuy)

        boss2(bossx, bossy)
        pygame.display.update()

    if badending is True:
        morreu(0, 0)
    elif goodending is True:
        viveu(0, 0)
    elif easteregg is True:
        egg(0, 0)

    pygame.display.update()
