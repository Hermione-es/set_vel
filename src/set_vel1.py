#!/usr/bin/env python
#linear drive(translation)
import rospy
import time
from geometry_msgs.msg import Twist


def time_vel(start_time):

    duration = time.time() - start_time

    if duration < 10:
        control_linear_vel = 0
        control_angular_vel = 0

    elif duration >= 10 and duration < 40:
        control_linear_vel = 0.03
        control_angular_vel = 0

    elif duration >= 40 and duration < 100:
        control_linear_vel = -0.03
        control_angular_vel = 0

    elif duration >= 100 and duration < 130:
        control_linear_vel = 0.03
        control_angular_vel = 0

    elif duration >= 130 and duration < 135:
        control_linear_vel = 0
        control_angular_vel = 0
    
    elif duration >= 135 and duration < 145:
        control_linear_vel = 0
        control_angular_vel = 0.15708

    elif duration >= 145 and duration < 150:
        control_linear_vel = 0
        control_angular_vel = 0

    elif duration >= 150 and duration < 180:
        control_linear_vel = 0.03
        control_angular_vel = 0

    elif duration >= 180 and duration < 240:
        control_linear_vel = -0.03
        control_angular_vel = 0
        
    elif duration >= 240 and duration < 270:
        control_linear_vel = 0.03
        control_angular_vel = 0
    
    elif duration >= 270 and duration < 275:
        control_linear_vel = 0
        control_angular_vel = 0

    elif duration >= 275 and duration < 285:
        control_linear_vel = 0
        control_angular_vel = -0.15708

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
