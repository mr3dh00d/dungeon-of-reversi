import cocos
import pyglet

keyboard = pyglet.window.key.KeyStateHandler()

class Mover(cocos.actions.Move):
    def step(self, dt):
        super().step(dt)
        speed = 400
        vel_x = (keyboard[pyglet.window.key.RIGHT] - keyboard[pyglet.window.key.LEFT])
        vel_y = (keyboard[pyglet.window.key.UP] - keyboard[pyglet.window.key.DOWN])
        velocity = (vel_x, vel_y)
        if (vel_x != 0 and vel_y != 0):
            speed *= 0.8
        self.target.velocity = tuple(map(lambda x: x*speed, velocity))
