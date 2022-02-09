#!/usr/bin/env python
#rotation drive
import rospy
import time
from geometry_msgs.msg import Twist


def time_vel(start_time):
    
    current_time =  rospy.Time.now()
    dt = current_time - start_time

    if dt.to_sec() < 10:
        control_linear_vel = 0
        control_angular_vel = 0
    
    elif dt.to_sec() >= 10 and dt.to_sec() < 15:
        control_linear_vel = 0
        control_angular_vel = 0.06594468891

    elif dt.to_sec() >= 15 and dt.to_sec() < 85:
        control_linear_vel = 0.0448798951 # radius*2*pi/time
        control_angular_vel = 0.08377580410 # 2*pi/time

    elif dt.to_sec() >= 85 and dt.to_sec() < 90:
        control_linear_vel = 0
        control_angular_vel = 0

    elif dt.to_sec() >= 90 and dt.to_sec() < 95:
        control_linear_vel = 0
        control_angular_vel = -0.06594468891

    elif dt.to_sec() >= 95 and dt.to_sec() < 165:
        control_linear_vel = 0.0448798951 # radius*2*pi/time
        control_angular_vel = -0.08377580410 # 2*pi/time

    elif dt.to_sec() >= 165 and dt.to_sec() <170:
        control_linear_vel = 0
        control_angular_vel = 0
    
    elif dt.to_sec() >= 170 and dt.to_sec() < 175:
        control_linear_vel = 0
        control_angular_vel = 0.06594468891

    elif dt.to_sec() >= 175 and dt.to_sec() < 245:
        control_linear_vel = 0.0448798951 # radius*2*pi/time
        control_angular_vel = 0.0897597901 # 2*pi/time

    elif dt.to_sec() >= 245 and dt.to_sec() < 250:
        control_linear_vel = 0
        control_angular_vel = 0
    
    elif dt.to_sec() >= 250 and dt.to_sec() < 255:
        control_linear_vel = 0
        control_angular_vel = -0.06594468891

    elif dt.to_sec() >= 255 and dt.to_sec() < 325:
        control_linear_vel = 0.0448798951 # radius*2*pi/time
        control_angular_vel = -0.06594468891 # 2*pi/time

    else :
        control_linear_vel = 0
        control_angular_vel = 0

    return control_linear_vel, control_angular_vel



if __name__=="__main__":

    rospy.init_node('set_vel')

    pub = rospy.Publisher('cmd_vel', Twist, queue_size=3)

    twist = Twist()

    start_time =  rospy.Time.now()
    rate = rospy.Rate(50) # 10hz

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

