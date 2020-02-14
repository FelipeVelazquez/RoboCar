#!/usr/bin/env python3
# license removed for brevity


#import rospy
#from std_msgs.msg import String
#import board
#import busio
#import adafruit_pca9685
import xbox
from adafruit_servokit import ServoKit
import math

joy = xbox.Joystick() 


kit = ServoKit(channels=16)


def controlFun():
	#pub = rospy.Publisher('ControlBase', String, queue_size=10)
	#rospy.init_node('control', anonymous=True)
	#rate = rospy.Rate(10) # 10hz
	#while not rospy.is_shutdown():
	while joy.back() != 1:
		direc = joy.leftY() * -1
		kit.servo[0].angle = math.degrees(math.acos(direc))
		data = "El canal 0: " + str(math.degrees(math.acos(direc))) + ", el valor del canal 1: " 
		#rospy.loginfo(data)
		#pub.publish(data)
		#rate.sleep()

if __name__ == '__main__':
	#try:
	controlFun()
	#except rospy.ROSInterruptException:
	#	pass
