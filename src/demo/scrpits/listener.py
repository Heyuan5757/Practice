
import sys
import rospy
from std_msgs.msg import String
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QVBoxLayout
from PyQt5.QtChart import QChart, QChartView, QLineSeries, QValueAxis
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor
from mainWindow import MainWindow


class Listener(object):
    def __init__(self):
        super().__init__()
        rospy.init_node('listener', anonymous=True)

    def run(self):
        pass

    def add_topic(self, topic, func):
        rospy.Subscriber(topic, String, func)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()

    listener = Listener()
    listener.add_topic('cpu_usage', w.chart_cpu_usage.update_data)
    listener.add_topic('memory_usage', w.chart_memory_usage.update_data)

    sys.exit(app.exec_())
