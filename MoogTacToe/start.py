import time
import sys
import os
from tkinter  import *
from PIL import ImageTk,Image
import pygame
from pygame import mixer

root = Tk()
pygame.init()

root.title('Moog-Tac-Toe')
root.resizable(False,False)
root['background']= 'yellow'
photo = ImageTk.PhotoImage(Image.open('Moog pics\k-on.png'))
myphoto = Label(image = photo)
myphoto.pack()

def loadGame():
     # the game
     QuickStop()
     root.withdraw()
     os.system('python MoogtacToe.py')
     root.deiconify()
     
     # bring back music
     bgMusic()

def bgMusic():
     pygame.mixer.music.load('Moog sounds\Cagayake!GIRLS8bit.mp3')
     pygame.mixer.music.play(-1)
     pygame.mixer.music.set_volume(0.3)

def QuickStop():
      pygame.mixer.music.fadeout(1000)
      pygame.time.delay(500)

def QuickPlay():
     pygame.mixer.music.rewind()

def soundStart():
      pygame.mixer.music.load('Moog sounds\mixkit-unlock-game-notification-253.wav')
      pygame.mixer.music.play()

def soundQuit():
     pygame.mixer.music.load('Moog sounds\mixkit-negative-game-notification-249.wav')
     pygame.mixer.music.play()

b =Button(root, height=3,width=10,bd = .5, relief = 'ridge',bg = '#ffffb7', text='Start Game', command = lambda:[soundStart(),loadGame()])
b.pack(pady=5)

b2 = Button(root, height=3,width=10,bd = .5, relief = 'ridge',bg = '#f4a9a4', text='Quit', command = lambda:[soundQuit(),time.sleep(1),root.quit()])
b2.pack(pady=5)


bgMusic()
root.mainloop() 
