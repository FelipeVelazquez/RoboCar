#!/usr/bin/env python

import rospy 
from sensor_msgs.msg import LaserScan


def callback(msg):
    print (msg.ranges[90])

 
rospy.init_node('scan_test')

sub = rospy.Subscriber('/scan', LaserScan, callback)
rospy.spin()