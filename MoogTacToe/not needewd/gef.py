# import pyglet

# animation =  pyglet.image.load_animation('moogstrong.gif')
# animSprite = pyglet.sprite.Sprite(animation)


# w = animSprite.width
# h = animSprite.height

# window = pyglet.window.Window(width = w, height = h)

# @window.event
# def on_draw():
#     animSprite.draw()

# pyglet.app.run()

from PIL import Image
from tkinter  import *

root = Tk()


root.iconbitmap('favicon1.ico')
root.title('MoogTacToe                                                ©Bry')

root.resizable(False,False)

im = Image.open("moogstrong.gif")

# To iterate through the entire gif
try:
    while 1:
        im.seek(im.tell()+1)
        # do something to im
except EOFError:
    pass # end of sequence




root.mainloop()