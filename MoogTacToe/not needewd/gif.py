from tkinter  import *
import tkinter.messagebox
import pygame
from pygame import mixer



root = Tk()
pygame.init()

clock = pygame.time.Clock()

root.iconbitmap('favicon1.ico')
root.title('MoogTacToe')

root.resizable(False,False)


mixer.music.load('HoneySweetTeaTime.mp3')
mixer.music.play(-1)





root.mainloop()
