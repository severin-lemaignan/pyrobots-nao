import naoqi

from robots.mw import ROS
from robots import GenericRobot

class Nao(GenericRobot):
    
    def __init__(self,
                 nao_ip ="127.0.0.1", nao_port=9559, 
                 with_ros=True,
                 immediate=False):

        super(Nao, self).__init__(actions = ["robots.naoqi.actions"],
                 supports=ROS if with_ros else 0,
                 dummy=False,
                 immediate=immediate)

        self.motion = naoqi.ALProxy("ALMotion", nao_ip, nao_port)

