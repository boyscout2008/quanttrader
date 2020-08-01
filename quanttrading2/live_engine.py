#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import argparse
import yaml
from PyQt5 import QtCore, QtWidgets, QtGui
from .gui.ui_main_window import MainWindow
import atexit
from signal import signal, SIGINT, SIG_DFL
from os import kill
from multiprocessing import Process

# https://stackoverflow.com/questions/4938723/what-is-the-correct-way-to-make-my-pyqt-application-quit-when-killed-from-the-co
signal(SIGINT, SIG_DFL)

def main(config_file):
    config = None
    try:
        # path = os.path.abspath(os.path.dirname(__file__))
        # config_file = os.path.join(path, 'config.yaml')
        with open(os.path.expanduser(config_file), encoding='utf8') as fd:
            config = yaml.load(fd)
    except IOError:
        print("config.yaml is missing")

    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow(config)

    if config['theme'] == 'dark':
        import qdarkstyle
        app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

    mainWindow.showMaximized()
    sys.exit(app.exec_())


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Live Engine')
    parser.add_argument('-f', '--config_file', dest = 'config_file', help='config yaml file')
    args = parser.parse_args()

    main(args.config_file)