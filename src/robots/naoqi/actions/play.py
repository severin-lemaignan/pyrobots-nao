# -*- coding: utf-8 -*-
"""
Created on Fri Feb 27 17:48:10 2015

@author: ferran
"""

import logging; logger = logging.getLogger("nao.sound")

from robots.mw import ROS
from robots.concurrency import action, ActionCancelled
from robots.resources import lock
from robots.naoqi.res import *

import sys
import time
from naoqi import ALProxy


#from playwave import WavePlayer

#player = WavePlayer()

#@action
#@lock(AUDIO)
#def playsound(robot, file):
#    try:
#        player.play(file)
#    except ActionCancelled:
#        player.stop()


audio_publisher = None

@action
@lock(AUDIO)
def playsound(robot, file):
    
    IP = "192.168.1.12"
    PORT = 9559
    
    try:
        aup = ALProxy("ALAudioPlayer", IP, PORT)
    except Exception,e:
        print "Could not create proxy to ALAudioPlayer"
        print "Error was: ",e

    #Loads a file and launchs the playing 5 seconds later
    fileId = aup.loadFile("/home/nao/robot.wav")
    time.sleep(5)
    aup.play(fileId)
