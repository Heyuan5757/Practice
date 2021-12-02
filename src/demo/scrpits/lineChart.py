#!/home/laicunyi/anaconda3/envs/ros_test/bin/python3.8
# -*-coding:utf-8-*-

import sys
from PyQt5.QtWidgets import QLabel, QMainWindow, QApplication, QWidget, QVBoxLayout, QGridLayout
from PyQt5.QtChart import QChart, QChartView, QLineSeries, QValueAxis
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor


class LineChart(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.chart = QChart()
        self.chart.setAnimationOptions(QChart.SeriesAnimations)
        self.chart.legend().hide()

        self.line_series = QLineSeries()
        x_values = [1, 2, 3, 4, 5, 6, 7]
        y_values = [1, 2, 4, 3, 1, 3, 50]
        for value in range(0, len(x_values)):
            self.line_series.append(x_values[value], y_values[value])
        # Add line series to chart instance
        self.chart.addSeries(self.line_series)

        self.axis_x = QValueAxis()
        self.axis_x.setLabelFormat("%d")
        self.chart.addAxis(self.axis_x, Qt.AlignBottom)
        self.line_series.attachAxis(self.axis_x)

        self.axis_y = QValueAxis()
        self.axis_y.setLabelFormat("%d")
        self.chart.addAxis(self.axis_y, Qt.AlignLeft)
        self.line_series.attachAxis(self.axis_y)

        self.chart_view = QChartView(self.chart)
        self.chart_view.setRenderHint(QPainter.Antialiasing)

        self.update_times = 8

    def update_data(self, data):
        cpu_usage = float(data.data)
        self.line_series.append(self.update_times, cpu_usage)
        self.update_times += 1
        self.axis_x.setMin(0)
        self.axis_x.setMax(self.update_times)
