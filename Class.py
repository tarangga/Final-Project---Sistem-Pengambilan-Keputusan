#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 28 13:08:17 2021

@author: tarangga
"""
from PyQt5 import QtWidgets, QtCore

import apps
import recommend
class MainApps(apps.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        
    
    def get_data(self):
        data = {}
        data['keaktifan'] = self.KeaktifanSlider.value()
        data['min_usia'] = self.cast_int(self.UsiaLeftText.text() )
        data['max_usia'] = self.cast_int(self.UsiaRightText.text())
        data['min_berat'] = self.cast_int(self.BeratLeftText.text())
        data['max_berat'] = self.cast_int(self.BeratRightText.text())
        data['min_ukuran'] = self.cast_int(self.UkuranLeftText.text())
        data['max_ukuran'] = self.cast_int(self.UkuranRightText.text())
        data['warna'] = self.WarnalSlider.value()
        data['bulu'] = self.BuluSlider_3.value()
        print(data)
        return data
    
    def cast_int(self, txt):
        return int(txt) if txt != '' else 0
    
    def setup(self, MainWindow):
        self.setupUi(MainWindow)
        self.Save.clicked.connect(lambda: self.open_result())
        
    def open_result(self):
        self.window = QtWidgets.QMainWindow()
        self.result = RecommendApps('kucing', 'imut')
        self.result.setup(self.window)
        self.window.show()
        
        

class RecommendApps(recommend.Ui_MainWindow):
    def __init__(self, rec, desc):
        super().__init__()
        self.animal = rec
        self.description = desc
    
    def setup(self, window):
        self.setupUi(window)
        _translate = QtCore.QCoreApplication.translate
        self.Recommend.setText(_translate("MainWindow", self.animal))
        self.Description.setText(_translate("MainWindow", self.description))
        
        