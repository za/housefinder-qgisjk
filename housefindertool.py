#!/usr/bin/python

from PyQt4.QtGui import *

from qgis.gui import *
from qgis.core import *

from qgis.utils import iface

class HouseFinderTool(QgsMapTool):
  def __init__(self, canvas):
      self.canvas = canvas
      QgsMapTool.__init__(self, self.canvas)
  def canvasPressEvent(self, e):
      #QMessageBox.information(None, "hello", "click!")
      pt_canvas = e.pos()
      pt_map = self.toMapCoordinates(pt_canvas)
      geom = QgsGeometry.fromPoint(pt_map)
      minDist = 99999999
      minName = ""
      layer = iface.activeLayer()
      for f in layer.getFeatures():
          dist = f.geometry().distance(geom)
          if dist < minDist:
              minDist = dist
              minName = f["name"]
      QMessageBox.information(None, "Minimal distance", "%s -- only %f" % (minName, minDist))
