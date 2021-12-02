#!/home/laicunyi/anaconda3/envs/ros_test/bin/python3.8
# -*-coding:utf-8-*-

import rospy
from std_msgs.msg import String
from systemInfo import SystemInfo


class Talker(object):
    def __init__(self):
        super().__init__()
        rospy.init_node('talker', anonymous=True)

        self.add_topic()
        self.run()

    def run(self):
        rate = rospy.Rate(2)  # 2Hz
        while not rospy.is_shutdown():
            # 步骤3.此处添加自动发布的函数
            self.pub_cpu_usage()
            self.pub_memory_usage()
            rate.sleep()

    def add_topic(self):
        # 步骤1.添加要发布的topic
        self.pub_cpu = rospy.Publisher('cpu_usage', String, queue_size=2)
        self.pub_memory = rospy.Publisher('memory_usage', String, queue_size=2)
    # """
    # 步骤2.添加要发布的topic对应信息函数
    # """
    def pub_cpu_usage(self):
        cpu_str = str(SystemInfo.get_cpu_usage())
        rospy.loginfo("cpu: %s", cpu_str)
        self.pub_cpu.publish(cpu_str)

    def pub_memory_usage(self):
        memory_str = str(SystemInfo.get_memory_usage())
        rospy.loginfo("memory: %s", memory_str)
        self.pub_memory.publish(memory_str)


    


if __name__ == '__main__':
    try:
        talker = Talker()
        talker.run()
    except rospy.ROSInterruptException:
        pass
