# -*- coding: utf-8 -*-
#
################################################################################
#
# Copyright 2013 Crown copyright (c)
# Land Information New Zealand and the New Zealand Government.
# All rights reserved
#
# This program is released under the terms of the new BSD license. See the 
# LICENSE file for more information.
#
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from qgis.core import *

from .LandXmlDialog import LandXmlDialog

class LandXmlPlugin:

    def __init__(self, iface):
        self._iface = iface

    def initGui(self):
        self._action = QAction(QIcon(":/plugins/LandXml/LandXmlIcon.png"), 
        "LandXml", self._iface.mainWindow())
        self._action.setWhatsThis("Import a LandXml file")
        self._action.triggered.connect(self.run)
        # self.iface.addToolBarIcon(self.action)
        self._iface.addPluginToMenu("&LandXml", self._action)

    def unload(self):
        self._iface.removePluginMenu("&LandXml",self._action)
        # self.iface.removeToolBarIcon(self.action)

    def run(self):
        settings = QSettings()
        prjSetting = settings.value("/Projections/defaultBehaviour")
        try:
           settings.setValue("/Projections/defaultBehaviour","")
           dlg = LandXmlDialog(self._iface)
           dlg.exec_()
        finally:
           if prjSetting:
               settings.setValue("/Projections/defaultBehaviour",prjSetting)

