import pygame
import random
max_x=1200
max_y=700
size_nlo_x=150
size_nlo_y=150
pygame.init()
zapusk=0
screen=pygame.display.set_mode((max_x,max_y))
pygame.display.set_caption("Космический корабль")
myimage=pygame.image.load("kosmas.png").convert()
mynlo=pygame.image.load("nad-orskom-proletel-nlo_1.png").convert()
pechenie=pygame.image.load("еченье.png").convert()
tochka_smerty=pygame.image.load("button.png").convert()
tochka_smerty=pygame.transform.scale(tochka_smerty,(15,10))
tochka_smerty.set_colorkey((255,255,255))
tochka_smerty_2=pygame.image.load("button.png").convert()
tochka_smerty_2=pygame.transform.scale(tochka_smerty,(15,10))
tochka_smerty_2.set_colorkey((255,255,255))
tochka_smerty_3=pygame.image.load("button.png").convert()
tochka_smerty_3=pygame.transform.scale(tochka_smerty,(15,10))
tochka_smerty_3.set_colorkey((255,255,255))
pechenie=pygame.transform.scale(pechenie,(60,45))
pechenie.set_colorkey((255,255,255))
mynlo.set_colorkey((0, 0, 0))
myimage=pygame.transform.scale(myimage,(max_x,max_y))
mynlo=pygame.transform.scale(mynlo,(size_nlo_x, size_nlo_y))
polochenie_x_pechnie=600
polochenie_y_pechenie = 300
polochenie_x_tochka_smerty=1100
polochenie_y_tochka_smerty=400
polochenie_x_tochka_smerty_2=1100
polochenie_y_tochka_smerty_2=400
polochenie_x_tochka_smerty_3=1100
polochenie_y_tochka_smerty_3=400
sdvid_polochenie_y_tochka_smerty = 5
sdvig_polochenie_x_tochka_smerty = 5
sdvid_polochenie_y_tochka_smerty_2 = 5
sdvig_polochenie_x_tochka_smerty_2 = 5
sdvid_polochenie_y_tochka_smerty_3 = 5
sdvig_polochenie_x_tochka_smerty_3 = 5
scorost_smerty=1


pygame.font.init()
myfont=pygame.font.SysFont('Comic Sans MS', 30)
chet=0

mynlo_x=20
mynlo_y=20
move_right=False
move_left=False
move_down=False
move_up=False
game_over=False
while game_over==False:

    for x in pygame.event.get():
        if x.type==pygame.KEYDOWN:
            if x.key==pygame.K_ESCAPE:
                game_over=True
            if x.key==pygame.K_LEFT:
                move_left=True
            if x.key==pygame.K_RIGHT:
                move_right=True
            if x.key==pygame.K_UP:
                move_up=True
            if x.key==pygame.K_DOWN:
                move_down=True
        if x.type == pygame.KEYUP:
            if x.key==pygame.K_LEFT:
                move_left=False
            if x.key==pygame.K_RIGHT:
                move_right=False
            if x.key==pygame.K_UP:
                move_up=False
            if x.key==pygame.K_DOWN:
                move_down=False

    if move_up==True:
        mynlo_y-=1
        if mynlo_y<-50:
            mynlo_y=-50
    if move_down==True:
        mynlo_y+=1
        if mynlo_y>max_y-size_nlo_y+50:
            mynlo_y=max_y-size_nlo_y+50
    if move_right==True:
        mynlo_x+=1
        if mynlo_x>max_x-size_nlo_x:
            mynlo_x=max_x-size_nlo_x
    if move_left==True:
        mynlo_x-=1
        if mynlo_x<0:
            mynlo_x=0

    screen.blit(myimage, (0, 0))
    screen.blit(mynlo, (mynlo_x, mynlo_y))
    play = myfont.render(("Играть "), False, (255, 255, 255))
    screen.blit(play, (550, 300))
    if ((450<mynlo_x<=550 and 150<=mynlo_y<=250) or zapusk>0):
        screen.blit(myimage, (0, 0))
        screen.blit(mynlo, (mynlo_x, mynlo_y))
        polochenie_x_tochka_smerty += sdvig_polochenie_x_tochka_smerty
        polochenie_y_tochka_smerty += sdvid_polochenie_y_tochka_smerty
        zapusk+=1

        if polochenie_x_tochka_smerty > max_x - 10:
            sdvig_polochenie_x_tochka_smerty = sdvig_polochenie_x_tochka_smerty * -1
        if polochenie_x_tochka_smerty < 0:
            sdvig_polochenie_x_tochka_smerty = sdvig_polochenie_x_tochka_smerty * -1
        if polochenie_y_tochka_smerty > max_y - 10:
            sdvid_polochenie_y_tochka_smerty = sdvid_polochenie_y_tochka_smerty * -1
        if polochenie_y_tochka_smerty < -10:
            sdvid_polochenie_y_tochka_smerty = sdvid_polochenie_y_tochka_smerty * -1

        if (
                mynlo_x + 30 <= polochenie_x_tochka_smerty <= mynlo_x + 100 and mynlo_y + 30 <= polochenie_y_tochka_smerty <= mynlo_y + 100):  # +60
            mytext1 = myfont.render(("Вы проиграли "), False, (255, 255, 255))
            sdvig_polochenie_x_tochka_smerty = 0
            sdvid_polochenie_y_tochka_smerty = 0
            mynlo = pygame.image.load("взрыв.png").convert()
            mynlo = pygame.transform.scale(mynlo, (size_nlo_x, size_nlo_y))

            screen.blit(mytext1, (550, 300))

        elif (mynlo_x <= polochenie_x_pechnie <= mynlo_x + (size_nlo_x / 2.5) and mynlo_y <= polochenie_y_pechenie <= mynlo_y + (size_nlo_y / 2.5)):
            polochenie_x_pechnie = random.randint(10, 1100)
            polochenie_y_pechenie = random.randint(0, 600)
            mynlo = pygame.transform.scale(mynlo, (size_nlo_x, size_nlo_y))
            chet += 1

        mytext = myfont.render(("поймано " + str(chet)), False, (255, 255, 255))
        screen.blit(pechenie, (polochenie_x_pechnie, polochenie_y_pechenie))
        screen.blit(mytext, (0, 0))
        screen.blit(tochka_smerty, (polochenie_x_tochka_smerty, polochenie_y_tochka_smerty))
        if chet >= 5:
            polochenie_x_tochka_smerty_2 += sdvig_polochenie_x_tochka_smerty_2
            polochenie_y_tochka_smerty_2 += sdvid_polochenie_y_tochka_smerty_2
            if polochenie_x_tochka_smerty_2 > max_x - 10:
                sdvig_polochenie_x_tochka_smerty_2 = sdvig_polochenie_x_tochka_smerty_2 * -1
            if polochenie_x_tochka_smerty_2 < 0:
                sdvig_polochenie_x_tochka_smerty_2 = sdvig_polochenie_x_tochka_smerty_2 * -1
            if polochenie_y_tochka_smerty_2 > max_y - 10:
                sdvid_polochenie_y_tochka_smerty_2 = sdvid_polochenie_y_tochka_smerty_2 * -1
            if polochenie_y_tochka_smerty_2 < -10:
                sdvid_polochenie_y_tochka_smerty_2 = sdvid_polochenie_y_tochka_smerty_2 * -1
            screen.blit(tochka_smerty_2, (polochenie_x_tochka_smerty_2, polochenie_y_tochka_smerty_2))

            if (mynlo_x + 30 <= polochenie_x_tochka_smerty_2 <= mynlo_x + 100 and mynlo_y + 30 <= polochenie_y_tochka_smerty_2 <= mynlo_y + 100):  # +60
                sdvig_polochenie_x_tochka_smerty_2 = 0
                sdvid_polochenie_y_tochka_smerty_2 = 0
                mynlo = pygame.image.load("взрыв.png").convert()
                mynlo = pygame.transform.scale(mynlo, (size_nlo_x, size_nlo_y))
        if chet >= 10:
            polochenie_x_tochka_smerty_3 += sdvig_polochenie_x_tochka_smerty_3
            polochenie_y_tochka_smerty_3 += sdvid_polochenie_y_tochka_smerty_3
            if polochenie_x_tochka_smerty_3 > max_x - 10:
                sdvig_polochenie_x_tochka_smerty_3 = sdvig_polochenie_x_tochka_smerty_3 * -1
            if polochenie_x_tochka_smerty_3 < 0:
                sdvig_polochenie_x_tochka_smerty_3 = sdvig_polochenie_x_tochka_smerty_3 * -1
            if polochenie_y_tochka_smerty_3 > max_y - 10:
                sdvid_polochenie_y_tochka_smerty_3 = sdvid_polochenie_y_tochka_smerty_3 * -1
            if polochenie_y_tochka_smerty_3 < -10:
                sdvid_polochenie_y_tochka_smerty_3 = sdvid_polochenie_y_tochka_smerty_3 * -1
            screen.blit(tochka_smerty_3, (polochenie_x_tochka_smerty_3, polochenie_y_tochka_smerty_3))

            if (
                    mynlo_x + 30 <= polochenie_x_tochka_smerty_3 <= mynlo_x + 100 and mynlo_y + 30 <= polochenie_y_tochka_smerty_3 <= mynlo_y + 100):  # +60
                sdvig_polochenie_x_tochka_smerty_3 = 0
                sdvid_polochenie_y_tochka_smerty_3 = 0
                mynlo = pygame.image.load("взрыв.png").convert()
                mynlo = pygame.transform.scale(mynlo, (size_nlo_x, size_nlo_y))

    pygame.display.flip()




