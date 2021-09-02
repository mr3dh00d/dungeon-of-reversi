import cocos
import pyglet
from dungeon_of_reversi import ChangeSecene
from modules.keyboard import keyboard
from modules.map import getMap
from modules.portal import Portal
from modules.collision import CollisionBlock

class Mover(cocos.actions.Move):
    def step(self, dt):
        super().step(dt)
        speed = 350
        vel_x = (keyboard[pyglet.window.key.RIGHT] - keyboard[pyglet.window.key.LEFT])
        vel_y = (keyboard[pyglet.window.key.UP] - keyboard[pyglet.window.key.DOWN])
        velocity = (vel_x, vel_y)
        if (vel_x != 0 and vel_y != 0):
            speed *= 0.8
        velocity = tuple(map(lambda x: x*speed, velocity))
        min = (40, 55)
        max = (860, 845)
        position = self.target.position

        if (position[0] <= min[0]):
            if (velocity[0] < 0):
                velocity = (0, velocity[1])
            position = (min[0], position[1])
        if (position[0] >= max[0]):
            if (velocity[0] > 0):
                velocity = (0, velocity[1])
            position = (max[0], position[1])
        if (position[1] <= min[1]):
            if (velocity[1] < 0):
                velocity = (velocity[0], 0)
            position = (position[0], min[1])
        if (position[1] >= max[1]):
            if (velocity[1] > 0):
                velocity = (velocity[0], 0)
            position = (position[0], max[1])

        position = CollisionBlock(position, [(400, 400), (500, 500)])
        GameMap = getMap()
        for block in GameMap['blocks']:
            position = CollisionBlock(position, block)
        inPortal = False
        for direction, portal in GameMap['portals'].items():
            if(Portal(portal, position)):
                inPortal = True
                break
        if(inPortal):
            self.target.stop()
            ChangeSecene(direction)
        try:
            self.target.position = position
            self.target.velocity = velocity
        except:
            pass
