# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 15:18:48 2019

@author: edoardottt
"""
print("https://www.edoardoottavianelli.it")
# pygame libraries required
import pygame
import random
from Enemy import Enemy
from Missile import Missile
from Bomb import Bomb
import results
import sys

#initialize pygame-------------------------------------------------------------
pygame.init()

# display game definitions-----------------------------------------------------
screenWidth=800
screenHeight=600
screen = pygame.display.set_mode((screenWidth,screenHeight)) # set the screen dimension
pygame.display.set_caption("edoGame") # set the title of the screen
pygame.key.set_repeat(0,0) # allow repeat key with 1st (before the first reapeat) and 2st(between 2 repeats)

edo = pygame.image.load("edo.jpg")
screenDisplay = pygame.image.load("wallpaper.png")
missilepaint = pygame.image.load("missile.png")
hitlersx = pygame.image.load("hitlersx.png")
hitlerdx = pygame.image.load("hitlerdx.png")
explo = pygame.image.load("explosion.png")
bomb = pygame.image.load("bomb.png")
end = pygame.image.load("end.jpg")
gameoverdisplay = pygame.image.load("gameover.jpg")
x = (screenWidth*0.45)
y = (screenHeight*0.74)


#function definitions----------------------------------------------------------
def paintEdo(x,y):
    screen.blit(edo,(x,y))
def paintExplo(x,y):
    screen.blit(explo,(x,y))

# variables definitions--------------------------------------------------------
timee = 0
movimentox = 0
incrementoy = 25
incrementohit = 30
y_missile = y - 15
inc_bomba = 15
nemici_sconfitti = 0
bombe_evitate = 0
missili_sparati = 0
missilen = 0
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
missili = []
nemici = []
bombe = []
loopGame = True
spara = False
hit = False
bombes = False
pressright = False
pressleft = False
abbassa = False
gameover = False
quitting = False
fine = True

# The game---------------------------------------------------------------------
while(loopGame):
    if (gameover):
        loopGame=False
    else:
        for event in pygame.event.get():
            if (event.type==pygame.QUIT):
                loopGame=False
                quitting = True
                fine = False
            if (event.type==pygame.KEYDOWN): # if I press a key
                if (event.key==pygame.K_RIGHT): # right button held down
                    movimentox = 26
                    pressright= True
                if (event.key==pygame.K_LEFT): # left button held down
                    movimentox = -26
                    pressleft= True
            if (event.type==pygame.KEYUP): # if I release a key
                if (event.key==pygame.K_RIGHT): # right button released
                    pressright= False
                    if (pressleft):
                        movimentox = -26
                    else:
                        movimentox = 0
                elif (event.key==pygame.K_LEFT): # left button released
                    pressleft = False
                    if (pressright):
                        movimentox = 26
                    else:
                        movimentox = 0
                if (event.key==pygame.K_SPACE):
                    y_missile = y - 15
                    missile = missili.append(Missile(x+30,y_missile))
                    incrementoy = 28
                    spara = True
                    missili_sparati +=1
            #print(event) display events
        #screen.fill(white)
        screen.blit(screenDisplay,(0,0))
        x = x + movimentox
        if (x < 0):
            x = 0
        elif (x > 700):
            x = 700
        timee = timee + 1
        result = []
        for item in missili:
          if (item.y_m<-10) is False:
            result.append(item)
        missili = result
        if (spara):
            for i in range(len(missili)):
                missile = missili[i]
                missile.y_m = missile.y_m -incrementoy
                missile.paintMissile(missile.x_m,missile.y_m,missilepaint,screen)
        result = []
        for item in nemici:
          if (item.y_n<-10) is False:
            result.append(item)
        nemici = result
        if (hit):
            for i in range(len(nemici)):
                nemico = nemici[i]
                if (490<=nemico.y_n<=600 and 0<=nemico.x_n<=760):
                    gameover = True
                if (nemico.destra):
                    nemico.x_n = nemico.x_n + incrementohit
                else:
                    nemico.x_n = nemico.x_n - incrementohit
                if (nemico.x_n>=730):
                    nemico.destra = False
                    abbassa = True
                elif (nemico.x_n<=0):
                    nemico.destra = True
                    abbassa = True
                if (nemico.destra):
                    nemico.paintNemico(nemico.x_n,nemico.y_n,hitlerdx,screen)
                    if(abbassa):
                        abbassa = False
                        nemico.y_n = nemico.y_n + 90
                else:
                    nemico.paintNemico(nemico.x_n,nemico.y_n,hitlersx,screen)
                    if(abbassa):
                        abbassa = False
                        nemico.y_n = nemico.y_n + 90
        result = []
        for item in bombe:
          if (item.y_m<-10) is False:
            result.append(item)
        bombe = result
        if(bombes):
            for i in range(len(bombe)):
                bomba = bombe[i]
                if (x-25<=bomba.x_m<=x+90 and y-50<=bomba.y_m<=y+155):
                    paintExplo(bomba.x_m,bomba.y_m-100)
                    paintExplo(bomba.x_m,bomba.y_m-50)
                    paintExplo(bomba.x_m,bomba.y_m)
                    paintExplo(bomba.x_m+100,bomba.y_m-100)
                    paintExplo(bomba.x_m-100,bomba.y_m-100)
                    gameover = True
                if (bomba.y_m>500):
                    paintExplo(bomba.x_m,bomba.y_m-100)
                    bombe[i].__del__()
                    bombe_evitate += 1
                bomba.y_m = bomba.y_m + inc_bomba
                bomba.paintBomb(bomba.x_m,bomba.y_m,bomb,screen)
                        
        for i in range(len(missili)):
            for j in range(len(nemici)):
                x_missile = missili[i].x_m
                y_missile = missili[i].y_m
                x_nemico = nemici[j].x_n
                y_nemico = nemici[j].y_n
                if (x_nemico<x_missile<x_nemico+70):
                    if (y_nemico<y_missile<y_nemico+90):
                        paintExplo(x_nemico,y_nemico)
                        nemici[j].__del__()
                        nemici_sconfitti += 1
        result = []
        for item in nemici:
          if (item.y_n<-10) is False:
            result.append(item)
        nemici = result
        if (timee%8==0):
            hit = True
            random1 = random.randint(1,600)
            nemico = nemici.append(Enemy(random1,0))
        if (timee%17==0):
            bombes = True
            lennemici = len(nemici) - 1
            if(lennemici>=1):
                random2 = random.randint(1,lennemici)
                bombarolo = nemici[random2]
                bomba = bombe.append(Bomb(bombarolo.x_n,bombarolo.y_n))
        if (0<=x<=693):
            paintEdo(x,y)
        elif (x<0):
            paintEdo(0,y)
        else:
            paintEdo(693,y)
        #pygame.display.update() update only a part of the screen
        pygame.display.flip() #update the whole screen
        
# RESULT SAVING AND RECORD CHECKING-------------------------------------
if(not quitting):
    screen.blit(gameoverdisplay,(0,0))
    pygame.display.flip() #update the whole screen
    stringarecord = results.save(missili_sparati,bombe_evitate,nemici_sconfitti)  
    pygame.time.wait(4000)
    record = False
    if (int(stringarecord[0])==bombe_evitate or int(stringarecord[1])==missili_sparati or int(stringarecord[2])==nemici_sconfitti):
        record = True
        
#------------------------------------------------------------------------------
    
if(fine):
    pygame.font.init()
    font = pygame.font.Font('freesansbold.ttf', 32) 
    stringaresult = "Bombs: " + str(bombe_evitate) + " | Missiles: " + str(missili_sparati) + " | Enemies: " + str(nemici_sconfitti)
    text = font.render(stringaresult, True, green, blue)
    screen.fill(white)
    screen.blit(end,(0,0))
    screen.blit(text, (100,0))
    if (record):
        text1 = font.render("VERY NICE!! NEW RECORD!", True, green, blue)
        screen.blit(text1, (150,100))
    text2 = font.render("BOMBS RECORD: " + stringarecord[0], True, green, blue)
    screen.blit(text2, (150,250))
    text3 = font.render("MISSILES RECORD: " + stringarecord[1], True, green, blue)
    screen.blit(text3, (150,310))
    text4 = font.render("ENEMIES RECORD: " + stringarecord[2], True, green, blue)
    screen.blit(text4, (150,370))
    text5 = font.render("?ENTER TO QUIT", True, red, white)
    screen.blit(text5, (250,550))
    pygame.display.flip() #update the whole screen
    yes = True
    while(yes):
        for event in pygame.event.get():
            if (event.type==pygame.KEYDOWN): # if I press a key
                if (event.key==pygame.K_RETURN): # right button held down
                    yes = False
pygame.quit()
sys.exit()