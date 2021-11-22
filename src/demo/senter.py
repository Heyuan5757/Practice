#!/usr/bin/env python

from time import sleep
import psutil
import rospy
from std_msgs.msg import String


def talker():
    pub = rospy.Publisher('yuanhe',String,queue_size=10)
    rospy.init_node('yuanhe',anonymous=True)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        rospy.loginfo('%s' %psutil.cpu_percent(interval=1))
        pub.publish('%s' %psutil.cpu_percent(interval=1))
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass