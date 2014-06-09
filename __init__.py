# -*- coding: utf-8 -*-
"""
/***************************************************************************
 HouseFinder
                                 A QGIS plugin
 The House Finder plugin
                             -------------------
        begin                : 2014-06-07
        copyright            : (C) 2014 by za
        email                : za@python.or.id
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load HouseFinder class from file HouseFinder.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .house_finder import HouseFinder
    return HouseFinder(iface)
