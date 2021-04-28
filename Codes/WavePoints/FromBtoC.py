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

    #From WavePoint B
    os.system("gnome-terminal -e 'bash -c \"roslaunch amcl_demo_b.launch map_file:=/home/turtlebot/Documents/map.yaml; exec bash\"'")
    time.sleep(20)

    #To WavePoint C
    os.system("gnome-terminal -e 'bash -c \"python ~/Desktop/FYP/PythonCodes/Turtlebot/WavePoints/wavepointC.py; exec bash\"'")

    #Launch Music
    os.system("gnome-terminal -e 'bash -c \"python ~/Desktop/FYP/PythonCodes/Turtlebot/WavePoints/runmusic.py; exec bash\"'")

    #Launch a Popup Box of the WavePoint C Selected
    tkMessageBox.showinfo(title="Greetings", message="Point C Selected!!")

if __name__ == '__main__':
    try:
        launchturtlebot()
    except rospy.ROSInterruptException:
        pass

