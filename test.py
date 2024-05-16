'''
Author: cyanocitta
Date: 2024-05-13 19:29:03
LastEditTime: 2024-05-16 16:59:03
FilePath: \Code\BackgroundTest\test.py
Description: 
'''
from math import pi, sin, cos
from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from panda3d.core import CardMaker,NodePath,TransparencyAttrib,WindowProperties,Lens
from direct.interval.LerpInterval import LerpPosInterval,LerpFunc

class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)      
        # ratio = 362/1024

        properties = WindowProperties()
        properties.setSize(1920, 1080)
        self.win.requestProperties(properties)
                
        # Load the environment model.
        self.scene = self.loader.loadModel("models/environment")
        # Reparent the model to render.
        self.scene.reparentTo(self.render)
        # Apply scale and position transforms on the model.
        self.scene.setScale(2, 2, 2)
        self.scene.setPos(0, -20, 0)
        
        # 创建一个面片几何体
        card_maker = CardMaker("card")
        card_maker.set_frame(-1, 1, -1, 1)  # 设置面片的大小，这里为单位正方形
        card_np = NodePath(card_maker.generate())
        card_np.reparent_to(render)

        # 加载纹理
        texture = loader.load_texture("ComfyUI_00339_.png")

        # 将纹理贴在面片上
        card_np.set_texture(texture)

        # 设置面片的位置、旋转和缩放等属性
        card_np.set_pos(0, 0, 10)  # 设置位置
        card_np.set_hpr(0, 0, 0)  # 设置旋转
        card_np.set_scale(10)      # 设置缩放
########################################################
        # 创建一个面片几何体
        card_maker = CardMaker("card")
        card_maker.set_frame(-1, 1, -1, 1)  # 设置面片的大小，这里为单位正方形
        card_np2 = NodePath(card_maker.generate())        
        card_np2.setTransparency(TransparencyAttrib.MAlpha)
        card_np2.reparent_to(render)

        # 加载纹理
        texture = loader.load_texture("ComfyUI_00340_.png")

        # 将纹理贴在面片上
        card_np2.set_texture(texture)

        # # 设置面片的位置、旋转和缩放等属性
        # card_np2.set_pos(0, -5, 5-5*ratio)       # 设置位置        
        card_np2.set_pos(0, -9, 10)       # 设置位置
        card_np2.set_hpr(0, 0, 0)                # 设置旋转
        card_np2.set_scale(10,10,10)       # 设置缩放


        self.camera.setPos(0, -100, 10)        
        self.camera.lookAt(0, 0, 10)     # Make the camera look at the origin

        
        # Add the spinCameraTask procedure to the task manager.            
        # self.taskMgr.add(self.spinCameraTask, "SpinCameraTask")
        self.taskMgr.add(self.zoomCameraTask, "zoomCameraTask")
        # self.taskMgr.add(self.zoomCameraSliderTask, "zoomCameraSliderTask")

    # Define a procedure to move the camera.
    # spin around to check the scene
    def spinCameraTask(self, task):
        angleDegrees = task.time * 6.0 -60
        angleRadians = angleDegrees * (pi / 180.0)
        cameraradians = 50
        self.camera.setPos(cameraradians * sin(angleRadians), -cameraradians * cos(angleRadians), 10)
        self.camera.setHpr(angleDegrees, 0, 0)
        return Task.cont
    def zoomCameraTask(self, task):
        self.camera.setPos(0, -40, 10)        
        self.camera.lookAt(0, 0, 12)     # Make the camera look at the origin
        end_pos = (2, -6, 11)        
        duration = 8
        camera_movement = LerpPosInterval(self.camera, duration, end_pos)        
        camera_movement.start()
        # self.camLens.set_fov(170)
        # camera_Lens = LerpFunc(self.camLens.setFov,1,40, 110)        
        self.camLens.setFov(120 - 80/(1+task.time/10))
        # camera_Lens.loop()
        return Task.cont

    def zoomCameraSliderTask(self, task):
        self.camera.setPos(0, -62, 5)        
        self.camera.lookAt(0, 0, 10)     # Make the camera look at the origin
        end_pos = (2, -12, 15)        
        duration = 5
        camera_movement = LerpPosInterval(self.camera, duration, end_pos)
        
        camera_movement.start()
        return Task.cont
app = MyApp()
app.run()