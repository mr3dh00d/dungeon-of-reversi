import cocos
import pyglet
import json
from modules.collision import CollisionBlock

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
        # position = CollisionBlock(position, [(200, 200), (300, 300)])
        for block in json.load(open("data/maps.json"))['up-right']['blocks']:
            position = CollisionBlock(position, block) 
        # print(position)


        # center_lateral = (360, 540)
        # center_vertical = (400, 540)
        # if(position[0] <= center_lateral[0]+10):
        #     if(position[0] >= center_lateral[0] and center_vertical[1] > position[1] > center_vertical[0]):
        #         position = (center_lateral[0], position[1])
        # if(position[0] >= center_lateral[1]-10):
        #     if(position[0] <= center_lateral[1] and center_vertical[1] > position[1] > center_vertical[0]):
        #         position = (center_lateral[1], position[1])
        # if(position[1] <= center_vertical[0]+10):
        #     if(position[1] >= center_vertical[0] and center_lateral[1] > position[0] > center_lateral[0]):
        #         position = (position[0], center_vertical[0])
        # if(position[1] >= center_vertical[1]-10):
        #     if(position[1] <= center_vertical[1] and 540 > position[0] > 360):
        #         position = (position[0], center_vertical[1])

        # print(tuple(map(lambda x: int(x), position)))
        self.target.position = position
        self.target.velocity = velocity
