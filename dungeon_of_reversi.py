import cocos
import json
import modules.background as background
import modules.player as player
from modules.mover import keyboard
from cocos.director import director

if __name__=="__main__":
    director.init(width=900, height=900, caption="Dungeon of Reversi")
    director.window.push_handlers(keyboard)
    bkg = background.Background()
    plyr = player.Player()
    bkg.setSelected(json.load(open("data/maps.json"))['up-right']['image'])
    Scene = cocos.scene.Scene()
    Scene.add(bkg)
    Scene.add(plyr)
    director.run(Scene)
