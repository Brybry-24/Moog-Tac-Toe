import pygame
from pygame import mixer


pygame.init()

def bgMusic():
     pygame.mixer.music.load('HoneySweetTeaTime.mp3')
     pygame.mixer.music.play()

     pygame.mixer.music.fadeout(2000)