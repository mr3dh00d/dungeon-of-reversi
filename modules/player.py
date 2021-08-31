import cocos
import pyglet
import modules.mover as mover
from cocos.director import director

class Player(cocos.layer.Layer):
    is_event_handler = True
    def __init__(self):
        super().__init__()
        self.keys_pressed = set()
        self.setDown((350, 450))

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

    def on_key_press (self, key, modifiers):
        self.keys_pressed.add(key)
        self.updateSprite()


    def on_key_release (self, key, modifiers):
        self.keys_pressed.remove(key)
        self.updateSprite()

    def updateSprite(self):
        for key in self.keys_pressed:
            if key == pyglet.window.key.RIGHT:
                self.setRightRun(self.spr.position)
            elif key == pyglet.window.key.LEFT:
                self.setLeftRun(self.spr.position)
            elif key == pyglet.window.key.UP:
                self.setUpRun(self.spr.position)
            elif key == pyglet.window.key.DOWN:
                self.setDownRun(self.spr.position)
        if(len(self.keys_pressed) == 0):
            self.setDown(self.spr.position)


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
        self.spr.velocity = (0,0)
        self.spr.do(mover.Mover())
        self.add(self.spr)


