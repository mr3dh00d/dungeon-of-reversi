import cocos
import modules.background as background
import modules.player as player
from cocos.director import director

if __name__=="__main__":
    director.init(width=900, height=900, caption="Dungeon of Reversi")
    bkg = background.Background()
    plyr = player.Player()
    plyr.setDownRun((450,450))
    Scene = cocos.scene.Scene()
    Scene.add(bkg)
    Scene.add(plyr)
    director.run(Scene)