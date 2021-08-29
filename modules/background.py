import cocos
import pyglet
from cocos.director import director

class Background(cocos.layer.Layer):

    def __init__(self):
        super().__init__()
        self.backgorund_imagen=pyglet.image.ImageGrid(pyglet.image.load("assets/sprites/scenes/center/center.png"),1,4)
        self.setBlock()

    def setBlock(self):
        self.__set(0)

    def setPosible(self):
        self.__set(1)
        
    def setSelected(self):
        self.__set(2)

    def setCorupted(self):
        self.__set(3)

    def __set(self, bkg_img):
        try:
            self.remove(self.spr)
        except AttributeError:
            pass
        self.spr = cocos.sprite.Sprite(self.backgorund_imagen[bkg_img], scale=0.8)
        self.spr.position = director.get_window_size()[0]/2, director.get_window_size()[1]/2
        self.add(self.spr)