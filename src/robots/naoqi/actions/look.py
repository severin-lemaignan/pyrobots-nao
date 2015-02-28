# -*- coding: utf-8 -*-

import logging; logger = logging.getLogger("nao.look")
import time
import math
from random import uniform as rand
from robots.concurrency import action, ActionCancelled
from robots.resources import lock
from robots.naoqi.res import *

def clamp(v, vmin, vmax):
    return max(vmin, min(vmax, v))
    
@action
@lock(HEAD)
def lookat(robot, pose):
    place_eyes_towards(robot, pose)

def place_eyes_towards(robot, pose):
    pan, tilt = robot.poses.pantilt(pose, "CameraTop_frame")
    if pan < -math.pi/2 or pan > math.pi/2:
        #out of field of view!
        #TODO: turn the robot? -> maybe yes if the WHEELS are not locked?
        logger.warning("Desired gaze target out of field of view! pan: %s°, tilt:%s°" % (pan * 180 / math.pi, tilt * 180 / math.pi))
        return

    # vertical field of view
    tilt = clamp(tilt, -math.pi/4, math.pi/3)

    robot.motion.setStiffnesses("Head", 1.0)

    # Example showing how to set angles, using a fraction of max speed
    names  = ["HeadYaw", "HeadPitch"]
    angles  = [pan, tilt]

    fractionMaxSpeed  = 0.2
    
    # get angles    
    #useSensors = False 
    #angles = robot.motion.getAngles(names, useSensors)    

    # convert
    angles[0] = angles[0] 
    angles[1] = angles[1] 
       
    # Interpolate with speed
    robot.motion.angleInterpolationWithSpeed(names, angles, fractionMaxSpeed)  
       
    #robot.motion.setAngles(names, angles, fractionMaxSpeed)

    robot.sleep(3.0)

    robot.motion.setStiffnesses("Head", 0.0)
     

@action
@lock(HEAD)
def track(robot, pose):
    try:
        while True:
            place_eyes_towards(robot, pose)
            time.sleep(0.2)
    except ActionCancelled:
        pass
