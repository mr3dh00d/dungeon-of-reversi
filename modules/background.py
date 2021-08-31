import cocos
import pyglet
from cocos.director import director

class Background(cocos.layer.Layer):

    def __init__(self):
        super().__init__()
        self.setBlock()

    def setBlock(self, path_img=""):
        self.__set(0, path_img)

    def setPosible(self, path_img=""):
        self.__set(1, path_img)
        
    def setSelected(self, path_img=""):
        self.__set(2, path_img)

    def setCorupted(self, path_img=""):
        self.__set(3, path_img)

    def setImage(self, path_img):
        if (path_img == ""):
            path_img = "assets/sprites/scenes/center/center.png"
        self.backgorund_imagen = pyglet.image.ImageGrid(pyglet.image.load(path_img),1,4)

    def __set(self, bkg_img, path_img):
        try:
            self.remove(self.spr)
        except AttributeError:
            pass
        self.setImage(path_img)
        self.spr = cocos.sprite.Sprite(self.backgorund_imagen[bkg_img], scale=0.8)
        self.spr.position = (450, 450)
        self.add(self.spr)