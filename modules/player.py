from re import I
import cocos
import pyglet
from cocos.director import director
from pyglet import image

class Player(cocos.layer.Layer):
    def __init__(self):
        super().__init__()
        self.setDown((director.get_window_size()[0]/2, director.get_window_size()[1]/2))

    def setDown(self, position):
        self.__setImage("assets/characters/red hood/down.png", (1,1), position)
    def setDownRun(self, position):
        self.__setImage("assets/characters/red hood/down-run.png", (1,2), position, animated=True)
    def setUp(self, position):
        self.__setImage("assets/characters/red hood/up.png", (1,1), position)
    def setUpRun(self, position):
        self.__setImage("assets/characters/red hood/up-run.png", (1,2), position, animated=True)
    def setRight(self, position):
        self.__setImage("assets/characters/red hood/right.png", (1,1), position)
    def setRightRun(self, position):
        self.__setImage("assets/characters/red hood/right-run.png", (1,4), position, animated=True)
    def setLeft(self, position):
        self.__setImage("assets/characters/red hood/left.png", (1,1), position)
    def setLeftRun(self, position):
        self.__setImage("assets/characters/red hood/left-run.png", (1,4), position, animated=True)

    def __setImage(self, image, grid, position, animated=False):
        try:
            self.remove(self.spr)
        except AttributeError:
            pass
        img = pyglet.image.load(image)
        img = pyglet.image.ImageGrid(img, grid[0], grid[1])
        if(animated):
            anim =  pyglet.image.Animation.from_image_sequence(img[0:], 0.15, loop=True)
        else:
            anim = img[0]
        self.spr = cocos.sprite.Sprite(anim, position)
        self.add(self.spr)


