from direct.showbase.ShowBase import ShowBase
from direct.interval.IntervalGlobal import Sequence,Wait,Func,LerpPosInterval
from direct.task import Task
from panda3d.core import Vec3
from panda3d.core import CardMaker,NodePath
class MyGame(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        ratio = 362/1024
        # imageObject1 = OnscreenImage(image="core.png", pos=(0, 0, 0))
        # imageObject2 = OnscreenImage(image="core2.png", pos=(0, 1, -1+ratio),scale=(1, 1, ratio))
        # 创建一个面片几何体
        
        self.scene = self.loader.loadModel("models/environment")
        # Reparent the model to render.
        self.scene.reparentTo(self.render)
        
        card_maker = CardMaker("card")
        card_maker.set_frame(-1, 1, -1, 1)  # 设置面片的大小，这里为单位正方形
        card_np = NodePath(card_maker.generate())
        card_np.reparent_to(render)

        # 加载纹理
        texture = loader.load_texture("core.png")

        # 将纹理贴在面片上
        card_np.set_texture(texture)

        # 设置面片的位置、旋转和缩放等属性
        card_np.set_pos(0, 0, 6)  # 设置位置
        card_np.set_hpr(0, 0, 0)  # 设置旋转
        card_np.set_scale(5)      # 设置缩放
        self.scene.reparentTo(self.render)
        
                # 创建一个面片几何体
        card_maker2 = CardMaker("card2")
        card_maker2.set_frame(-1, 1, -1, 1)  # 设置面片的大小，这里为单位正方形
        card_np2 = NodePath(card_maker2.generate())
        card_np2.reparent_to(render)

        # 加载纹理
        texture = loader.load_texture("core.png")

        # 将纹理贴在面片上
        card_np2.set_texture(texture)

        # 设置面片的位置、旋转和缩放等属性
        card_np2.set_pos(0, 1, 6)  # 设置位置
        card_np2.set_hpr(0, 0, ratio-1)  # 设置旋转
        card_np2.set_scale(5,5,5*ratio)      # 设置缩放
        self.scene.reparentTo(self.render)
        
        # # Set up the camera
        self.camera.setPos(0, -10, 0)  # Adjust the position of the camera
        self.camera.lookAt(0, 0, 0)     # Make the camera look at the origin

        # # Define the end position
        end_pos = (0, 1, 0.25)

        # # Define the movement duration
        duration = 5

        # # Move the camera from the start position to the end position
        camera_movement = LerpPosInterval(self.camera, duration, end_pos)

        # # Sequence of actions
        # self.move_sequence = Sequence(
        #     camera_movement,
        #     name="CameraMoveSequence"
        # )

        # # Start the sequence
        # self.move_sequence.start()

        # Position the camera
        # self.camera.setPos(0, -10, 2)  # Set the position of the camera
        # self.camera.setHpr(0, 0, 0)     # Set the orientation (heading, pitch, roll) of the camera
        
        # Enable mouse control of the camera
        # ShowBase.oobe()
        
    # def cameraControl(self):
    #     self.accept("arrow_up", self.moveCamera, [Vec3(0, 1, 0)])
    #     self.accept("arrow_down", self.moveCamera, [Vec3(0, -1, 0)])
    #     self.accept("arrow_left", self.moveCamera, [Vec3(-1, 0, 0)])
    #     self.accept("arrow_right", self.moveCamera, [Vec3(1, 0, 0)])
    
    # def moveCamera(self, offset):
    #     self.camera.setPos(self.camera, offset)

game = MyGame()
game.run()
