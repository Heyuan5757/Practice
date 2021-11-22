#!/usr/bin/env python

import rospy
from std_msgs.msg import String



def callback(data):
    rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data.data)

def listener():
    rospy.init_node('listener', anonymous=True)
    # 初始化节点，节点名称为listener
    rospy.Subscriber('chatter', String, callback)
    # 订阅函数，订阅chatter主题，内容类型是std_msgs.msgs.String
    # 当有新内容，调用callback函数处理。接受到的主题内容作为参数传递给callback
    rospy.spin()
    # 保持节点运行，直到节点关闭

if __name__ == '__main__':
    listener()
    