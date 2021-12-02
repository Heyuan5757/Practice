#!/home/laicunyi/anaconda3/envs/ros_test/bin/python3.8
# -*-coding:utf-8-*-

import sys
from PyQt5.QtWidgets import QLabel, QMainWindow, QApplication, QWidget, QVBoxLayout, QGridLayout
from PyQt5.QtChart import QChart, QChartView, QLineSeries, QValueAxis
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor
from lineChart import LineChart


class MainWindow(object):
    def __init__(self, *args):
        super(MainWindow, self).__init__(*args)
    
    def show(self):
        self.grid = QGridLayout()
        self.grid.setSpacing(4)

        # 添加CPU使用率折线图
        self.chart_cpu_usage = LineChart()
        self.label_cpu_usage = QLabel('CPU USAGE')
        self.grid.addWidget(self.label_cpu_usage, 1, 0)
        self.grid.addWidget(self.chart_cpu_usage.chart_view, 1, 1)

        # 添加内存使用率折线图
        self.chart_memory_usage = LineChart()
        self.label_memory_usage = QLabel('MEMORY USAGE')
        self.grid.addWidget(self.label_memory_usage, 2, 0)
        self.grid.addWidget(self.chart_memory_usage.chart_view, 2, 1)

        # 添加主窗口配置信息
        self.mainwindow = QWidget()
        self.mainwindow.setGeometry(300, 300, 1200, 900)
        self.mainwindow.setWindowTitle('ROS机制学习之系统性能监控')    
        self.mainwindow.setLayout(self.grid)
        self.mainwindow.show()
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())