#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtWidgets, QtGui
from datetime import datetime
from ..order.order_type import OrderType
from ..order.order_event import OrderEvent
from ..event.event import LogEvent
import logging

_logger = logging.getLogger(__name__)


class RiskMenu(QtWidgets.QWidget):
    def __init__(self, strategy_manager):
        super(RiskMenu, self).__init__()

        self.strategy_manager = strategy_manager
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Risk Manager')
        self.setWindowIcon(QtGui.QIcon("gui/image/logo.ico"))
        self.resize(800, 500)

        hbox = QtWidgets.QHBoxLayout()
        top = QtWidgets.QFrame()
        top.setFrameShape(QtWidgets.QFrame.StyledPanel)
        control_layout = QtWidgets.QHBoxLayout()
        self.strategy_List = QtWidgets.QComboBox()
        self.strategy_List.addItems([str(i) for i in range(len(self.strategy_manager._strategy_dict)+1)])
        control_layout.addWidget(self.strategy_List)
        self.btn_load = QtWidgets.QPushButton('Load')
        self.btn_load.clicked.connect(self.load_config)
        control_layout.addWidget(self.btn_load)
        top.setLayout(control_layout)

        bottom = QtWidgets.QWidget()
        bottom_layout = QtWidgets.QFormLayout()

        self.order_start_time = QtWidgets.QLineEdit()
        self.order_end_time = QtWidgets.QLineEdit()
        self.single_trade_limit = QtWidgets.QLineEdit()
        self.total_trade_limit = QtWidgets.QLineEdit()
        self.total_cancel_limit = QtWidgets.QLineEdit()
        self.total_active_limit = QtWidgets.QLineEdit()
        self.total_loss_limit = QtWidgets.QLineEdit()
        self.btn_save = QtWidgets.QPushButton('Save')
        self.btn_save.clicked.connect(self.save_config)

        bottom_layout.addRow('order_start_time', self.order_start_time)
        bottom_layout.addRow('order_end_time', self.order_end_time)
        bottom_layout.addRow('single_trade_limit', self.single_trade_limit)
        bottom_layout.addRow('total_trade_limit', self.total_trade_limit)
        bottom_layout.addRow('total_cancel_limit', self.total_cancel_limit)
        bottom_layout.addRow('total_active_limit', self.total_active_limit)
        bottom_layout.addRow('total_loss_limit', self.total_loss_limit)
        bottom_layout.addRow(self.btn_save)

        bottom.setLayout(bottom_layout)

        splitter1 = QtWidgets.QSplitter(QtCore.Qt.Vertical)
        splitter1.addWidget(top)
        splitter1.addWidget(bottom)
        hbox.addWidget(splitter1)
        self.setLayout(hbox)

    def load_config(self):
        sid = self.strategy_List.currentIndex()
        if sid == 0:
            if 'total_trade_limit' in self.strategy_manager._config.kyes():
                if self.strategy_manager._config['total_trade_limit'] is not None:
                    self.total_trade_limit.setText(str(self.strategy_manager._config['total_trade_limit']))

            if 'total_cancel_limit' in self.strategy_manager._config.kyes():
                if self.strategy_manager._config['total_cancel_limit'] is not None:
                    self.total_cancel_limit.setText(str(self.strategy_manager._config['total_cancel_limit']))

            if 'total_active_limit' in self.strategy_manager._config.kyes():
                if self.strategy_manager._config['total_active_limit'] is not None:
                    self.total_active_limit.setText(str(self.strategy_manager._config['total_active_limit']))

            if 'total_loss_limit' in self.strategy_manager._config.kyes():
                if self.strategy_manager._config['total_loss_limit'] is not None:
                    self.total_loss_limit.setText(str(self.strategy_manager._config['total_loss_limit']))
        else:
            if 'order_start_time' in self.strategy_manager._config['strategy'][self.strategy_manager._strategy_dict[sid].name].keys():
                if self.strategy_manager._config['strategy'][self.strategy_manager._strategy_dict[sid].name]['order_start_time'] is not None:
                    self.order_start_time.setText(self.strategy_manager._config['strategy'][self.strategy_manager._strategy_dict[sid].name]['order_start_time'])

            if 'order_end_time' in self.strategy_manager._config['strategy'][self.strategy_manager._strategy_dict[sid].name].keys():
                if self.strategy_manager._config['strategy'][self.strategy_manager._strategy_dict[sid].name]['order_end_time'] is not None:
                    self.order_end_time.setText(self.strategy_manager._config['strategy'][self.strategy_manager._strategy_dict[sid].name]['order_end_time'])

            if 'single_trade_limit' in self.strategy_manager._config['strategy'][self.strategy_manager._strategy_dict[sid].name].keys():
                if self.strategy_manager._config['strategy'][self.strategy_manager._strategy_dict[sid].name]['single_trade_limit'] is not None:
                    self.single_trade_limit.setText(str(self.strategy_manager._config['strategy'][self.strategy_manager._strategy_dict[sid].name]['single_trade_limit']))

            if 'total_trade_limit' in self.strategy_manager._config['strategy'][seglf.strategy_manager._strategy_dict[sid].name].keys():
                if self.strategy_manager._config['strategy'][self.strategy_manager._strategy_dict[sid].name]['total_trade_limit'] is not None:
                    self.total_trade_limit.setText(str(self.strategy_manager._config['strategy'][self.strategy_manager._strategy_dict[sid].name]['total_trade_limit']))

            if 'total_cancel_limit' in self.strategy_manager._config['strategy'][self.strategy_manager._strategy_dict[sid].name].keys():
                if self.strategy_manager._config['strategy'][self.strategy_manager._strategy_dict[sid].name]['total_cancel_limit'] is not None:
                    self.total_cancel_limit.setText(str(self.strategy_manager._config['strategy'][self.strategy_manager._strategy_dict[sid].name]['total_cancel_limit']))

            if 'total_active_limit' in self.strategy_manager._config['strategy'][self.strategy_manager._strategy_dict[sid].name].keys():
                if self.strategy_manager._config['strategy'][self.strategy_manager._strategy_dict[sid].name]['total_active_limit'] is not None:
                    self.total_active_limit.setText(str(self.strategy_manager._config['strategy'][self.strategy_manager._strategy_dict[sid].name]['total_active_limit']))

            if 'total_loss_limit' in self.strategy_manager._config['strategy'][self.strategy_manager._strategy_dict[sid].name].keys():
                if self.strategy_manager._config['strategy'][self.strategy_manager._strategy_dict[sid].name]['total_loss_limit'] is not None:
                    self.total_loss_limit.setText(str(self.strategy_manager._config['strategy'][self.strategy_manager._strategy_dict[sid].name]['total_loss_limit']))

    def save_config(self):
        sid = self.strategy_List.currentIndex()

        if sid == 0:
            if not self.total_trade_limit:
                self.strategy_manager._config['total_trade_limit'] = int(self.total_trade_limit.text())
            else:
                self.strategy_manager._config['total_trade_limit'] = None
            if not self.total_cancel_limit:
                self.strategy_manager._config['total_cancel_limit'] = int(self.total_cancel_limit.text())
            else:
                self.strategy_manager._config['total_cancel_limit'] = None
            if not self.total_active_limit:
                self.strategy_manager._config['total_active_limit'] = int(self.total_active_limit.text())
            else:
                self.strategy_manager._config['total_active_limit'] = None
            if not self.total_loss_limit:
                self.strategy_manager._config['total_loss_limit'] = float(self.total_loss_limit.text())
            else:
                self.strategy_manager._config['total_loss_limit'] = None
        else:
            if not self.order_start_time:
                self.strategy_manager._config['strategy'][self.strategy_manager._strategy_dict[sid].name]['order_start_time'] = self.order_start_time.text()
            else:
                self.strategy_manager._config['order_start_time'] = None
            if not self.order_end_time:
                self.strategy_manager._config['strategy'][self.strategy_manager._strategy_dict[sid].name]['order_end_time'] = self.order_end_time.text()
            else:
                self.strategy_manager._config['order_end_time'] = None
            if not self.single_trade_limit:
                self.strategy_manager._config['strategy'][self.strategy_manager._strategy_dict[sid].name]['single_trade_limit'] = int(self.single_trade_limit.text())
            else:
                self.strategy_manager._config['single_trade_limit'] = None
            if not self.total_trade_limit:
                self.strategy_manager._config['strategy'][self.strategy_manager._strategy_dict[sid].name]['total_trade_limit'] = int(self.total_trade_limit.text())
            else:
                self.strategy_manager._config['total_trade_limit'] = None
            if not self.total_cancel_limit:
                self.strategy_manager._config['strategy'][self.strategy_manager._strategy_dict[sid].name]['total_cancel_limit'] = int(self.total_cancel_limit.text())
            else:
                self.strategy_manager._config['total_cancel_limit'] = None
            if not self.total_active_limit:
                self.strategy_manager._config['strategy'][self.strategy_manager._strategy_dict[sid].name]['total_active_limit'] = int(self.total_active_limit.text())
            else:
                self.strategy_manager._config['total_active_limit'] = None
            if not self.total_loss_limit:
                self.strategy_manager._config['strategy'][self.strategy_manager._strategy_dict[sid].name]['total_loss_limit'] = float(self.total_loss_limit.text())
            else:
                self.strategy_manager._config['total_loss_limit'] = None