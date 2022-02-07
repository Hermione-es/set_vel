#!/usr/bin/env python

import rospy
import time
from geometry_msgs.msg import Twist



def time_vel():

    if time < 50:
        control_linear_vel = 0.2
        control_angular_vel = 0

    elif time > 50 and time < 150:
        control_linear_vel = -0.2
        control_angular_vel = 0

    elif time > 150 and time < 250:
        control_linear_vel = 0.2
        control_angular_vel = 0
        
    else :
        control_linear_vel = 0
        control_angular_vel = 0
    
    return control_linear_vel, control_angular_vel 



if __name__=="__main__":
    rospy.init_node('set_vel')
    
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)

    twist = Twist()

    time = time.time()

    linear_vel, angular_vel = time_vel()
    
    twist.linear.x = linear_vel
    twist.linear.y = 0.0
    twist.linear.z = 0.0
    twist.angular.x = 0.0
    twist.angular.y = 0.0
    twist.angular.z = angular_vel 

    pub.publish(twist)

    rospy.spin()
    
