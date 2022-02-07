#!/usr/bin/env python

import rospy
import time
from geometry_msgs.msg import Twist


class get_vel():

    def __init__(self, control_linear_vel=0.2, control_angular_vel=0):

        self.pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)

        self.twist = Twist()

        self.time = time.time()
        self.control_linear_vel = control_linear_vel
        self.control_angular_vel = control_angular_vel

        self.time_vel()
        self.publish()

    def time_vel(self):

        if self.time < 50:
            self.control_linear_vel = 0.2
            self.control_angular_vel = 0

        elif self.time > 50 and self.time < 150:
            self.control_linear_vel = -0.2
            self.control_angular_vel = 0

        elif self.time > 150 and self.time < 250:
            self.control_linear_vel = 0.2
            self.control_angular_vel = 0
        
        else :
            self.control_linear_vel = 0
            self.control_angular_vel = 0


    def publish(self):
        self.twist.linear.x = 10
        self.twist.linear.y = 0.0
        self.twist.linear.z = 0.0
        self.twist.angular.x = 0.0
        self.twist.angular.y = 0.0
        self.twist.angular.z = 10

        self.pub.publish(self.twist)

if __name__=="__main__":
    rospy.init_node('set_vel')
    
    vel = get_vel()

    rospy.spin()