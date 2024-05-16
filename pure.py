'''
Author: cyanocitta
Date: 2024-05-14 12:00:17
LastEditTime: 2024-05-16 16:15:20
FilePath: \Code\BackgroundTest\pure.py
Description: 
'''
from direct.showbase.ShowBase import ShowBase

from panda3d.core import CardMaker
class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        camera.setPos(0,-45,0)

        # load the ball model
        self.ball = loader.loadModel("smiley")
        self.ball.reparentTo(render)
        self.ball.setPos(-15,0,0)

        # setup the projectile interval
        self.trajectory = ProjectileInterval(self.ball, duration=1,
                                            startPos=Point3(-15,0,0),
                                            endPos=Point3(15,0, 0))
        self.trajectory.loop()

        # Load texture

if __name__ == "__main__":
    app = MyApp()
    app.run()
