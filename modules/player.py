import json
import cocos
import pyglet
import modules.mover as mover
from modules.portal import Portal
from modules.map import getMap

character = json.load(open("data/characters.json"))

class Player(cocos.layer.Layer):
    is_event_handler = True
    def __init__(self):
        super().__init__()
        self.keys_pressed = set()
        self.can_move_it = True
        self.setDown((350, 450))

    def setDown(self, position):
        self.__setImage(character["player"]["assets"]["down"], (1,1), position)
    def setDownRun(self, position):
        self.__setImage(character["player"]["assets"]["down-run"], (1,2), position, animated=True)
    def setUp(self, position):
        self.__setImage(character["player"]["assets"]["up"], (1,1), position)
    def setUpRun(self, position):
        self.__setImage(character["player"]["assets"]["up-run"], (1,2), position, animated=True)
    def setRight(self, position):
        self.__setImage(character["player"]["assets"]["right"], (1,1), position)
    def setRightRun(self, position):
        self.__setImage(character["player"]["assets"]["right-run"], (1,4), position, animated=True)
    def setLeft(self, position):
        self.__setImage(character["player"]["assets"]["left"], (1,1), position)
    def setLeftRun(self, position):
        self.__setImage(character["player"]["assets"]["left-run"], (1,4), position, animated=True)

    def on_key_press (self, key, modifiers):
        try:
            self.keys_pressed.add(key)
            self.updateSprite()
        except:
            pass


    def on_key_release (self, key, modifiers):
        try:
            self.keys_pressed.remove(key)
            self.updateSprite()
        except:
            pass

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
        action = mover.Mover()
        inPortal = False
        for portal in getMap()['portals'].values():
            if(Portal(portal, self.spr.position)):
                inPortal = True
                break
        if(not inPortal and self.can_move_it):
            self.spr.do(action)
        self.add(self.spr)


