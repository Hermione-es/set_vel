#!/usr/bin/env python
#rotation drive
import rospy
import math




import time
from geometry_msgs.msg import Twist


def time_vel(start_time):

    duration = time.time() - start_time

    if duration < 10:
        control_linear_vel = 0
        control_angular_vel = 0

    elif duration >= 10 and duration < 150:
        control_linear_vel = 0.0224399475
        control_angular_vel = 0.0074*math.PI

    elif duration >= 150 and duration < 155:
        control_linear_vel = 0
        control_angular_vel = 0

    elif duration >= 155 and duration <295:
        control_linear_vel = 0.0224399475
        control_angular_vel = -0.0074*math.PI

    elif duration >= 295 and duration <300:
        control_linear_vel = 0
        control_angular_vel = 0

    elif duration >= 300 and duration <310:
        control_linear_vel = 0
        control_angular_vel = 0.15708

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

