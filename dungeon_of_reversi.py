import cocos
import pyglet
from cocos.scenes import *
import modules.background as background
import modules.player as player
import modules.map as Map
from modules.keyboard import keyboard
from modules.director import director

if __name__=="__main__":
    director.window.push_handlers(keyboard)
    bkg = background.Background()
    plyr = player.Player()
    bkg.setSelected(Map.getMap()['image'])
    Scene = cocos.scene.Scene()
    print(Map.actual_position)
    Scene.add(bkg)
    Scene.add(plyr)
    director.run(Scene)

def ChangeSecene(direction):
    global director
    Map.setPosition(direction)
    map = Map.getMap()
    print(Map.actual_position)
    new_bkg = background.Background()
    new_plyr = player.Player()
    # new_plyr.can_move_it = False
    if(direction == "left"):
        new_plyr.keys_pressed.add(pyglet.window.key.LEFT)
        new_plyr.setDown((750, 450))
    elif(direction == "up"):
        new_plyr.keys_pressed.add(pyglet.window.key.UP)
        new_plyr.setDown((450, 150))
    elif(direction == "right"):
        new_plyr.keys_pressed.add(pyglet.window.key.RIGHT)
        new_plyr.setDown((150, 450))
    elif(direction == "down"):
        new_plyr.keys_pressed.add(pyglet.window.key.DOWN)
        new_plyr.setDown((450, 750))
    new_plyr.updateSprite()
    if(Map.inSelect()):
        new_bkg.setSelected(map['image'])
    elif(Map.inLost()):
        new_bkg.setCorupted(map['image'])
    else:
        new_bkg.setBlock(map['image'])
    New_scene = cocos.scene.Scene()
    New_scene.add(new_bkg)
    New_scene.add(new_plyr)
    director.replace(FadeTRTransition(New_scene, duration=0.3))
    # # # new_plyr.can_move_it = True
