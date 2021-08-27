import cocos
import modules.background as background
from cocos.director import director

if __name__=="__main__":
    director.init(width=900, height=900, caption="Dungeon of Reversi")
    bkg = background.Background()
    # bkg.setCorupted()
    bkg.setPosible()
    bkg.setBlock()
    test_scene =  cocos.scene.Scene(bkg)
    director.run(test_scene)