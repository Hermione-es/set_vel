#!/usr/bin/env python

import rospy
import time
from geometry_msgs.msg import Twist



def time_vel(start_time):

    duration = time.time() - start_time
    rospy.loginfo(duration)

    if duration < 5:
        control_linear_vel = 0.2
        control_angular_vel = 0

    elif duration > 5 and duration < 15:
        control_linear_vel = -0.2
        control_angular_vel = 0

    elif duration > 15 and duration < 25:
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

    start_time = time.time()
    rate = rospy.Rate(10) # 10hz

    while not rospy.is_shutdown():
        linear_vel, angular_vel = time_vel(start_time)
        
        twist.linear.x = linear_vel
        twist.linear.y = 0.0
        twist.linear.z = 0.0
        twist.angular.x = 0.0
        twist.angular.y = 0.0
        twist.angular.z = angular_vel
        pub.publish(twist)

        rate.sleep()
    
    rospy.spin()
