import cocos
import pyglet
import modules.mover as mover
from cocos.director import director

class Player(cocos.layer.Layer):
    is_event_handler = True
    def __init__(self):
        super().__init__()
        # self.move=False
        self.keys_pressed = set()
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

    def on_key_press (self, key, modifiers):
        # print(pyglet.window.key.symbol_string(key))
        # if key == pyglet.window.key.DOWN:
        #     print(pyglet.window.key.symbol_string(key))
        #     self.spr.do(cocos.actions.MoveBy((0,-100)))
        #     print(self.spr.position)
        self.keys_pressed.add(key)
        self.updateSprite()
    #     if key == pyglet.window.key.RIGHT:
    #         self.setRightRun(self.spr.position)
    #     elif key == pyglet.window.key.LEFT:
    #         self.setLeftRun(self.spr.position)
    #     elif key == pyglet.window.key.UP:
    #         self.setUpRun(self.spr.position)
    #     elif key == pyglet.window.key.DOWN:
    #         self.setDownRun(self.spr.position)


    def on_key_release (self, key, modifiers):
        self.keys_pressed.remove(key)
        self.updateSprite()

    def updateSprite(self):
        # key_names = [pyglet.window.key.symbol_string (k) for k in self.keys_pressed]
        # text = 'Keys: '+','.join (key_names)
        # print(text)
        for key in self.keys_pressed:
            if key == pyglet.window.key.RIGHT:
                # print("entre")
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


