#!/usr/bin/env python

import roslaunch
import time
import subprocess
import os
import tkMessageBox
import rospy
from std_msgs.msg import String

def launchturtlebot():
    
    #Initialize Roscore
    roscore = subprocess.Popen('roscore')
    time.sleep(1)

    #Setup connection with TurtleBot
    os.system("gnome-terminal -e 'bash -c \"roslaunch turtlebot_bringup minimal.launch; exec bash\"'")
    time.sleep(1)

    #From WavePoint A
    os.system("gnome-terminal -e 'bash -c \"roslaunch amcl_demo_a.launch map_file:=/home/turtlebot/Documents/map.yaml; exec bash\"'")
    time.sleep(20)

    #To WavePoint D
    os.system("gnome-terminal -e 'bash -c \"python ~/Desktop/FYP/PythonCodes/Turtlebot/WavePoints/wavepointD.py; exec bash\"'")

    #Launch Music
    os.system("gnome-terminal -e 'bash -c \"python ~/Desktop/FYP/PythonCodes/Turtlebot/WavePoints/runmusic.py; exec bash\"'")

    #Launch a Popup Box of the WavePoint D Selected
    tkMessageBox.showinfo(title="Greetings", message="Point D Selected!!")

if __name__ == '__main__':
    try:
        launchturtlebot()
    except rospy.ROSInterruptException:
        pass

