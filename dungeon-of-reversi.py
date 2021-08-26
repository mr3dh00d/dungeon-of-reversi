import cocos

class HelloCocos(cocos.layer.Layer):
    def __init__(self):
        super().__init__()
        label = cocos.text.Label("Hello Cocos", font_name="CaskaydiaCove Nerd Font", font_size=32,
                                anchor_x="center", anchor_y="center")
        label.position = 450, 360
        self.add(label)

if __name__=="__main__":
    cocos.director.director.init(width=900, height=675, caption="Dungeon of Reversi")
    hello_layer=HelloCocos()
    test_scene =  cocos.scene.Scene(hello_layer)
    cocos.director.director.run(test_scene)