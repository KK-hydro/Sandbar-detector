# -*- coding: utf-8 -*-
"""
/***************************************************************************
 SandbarDetector
                                 A QGIS plugin
 Sandbar Detector
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2024-01-14
        copyright            : (C) 2024 by Klaudia Kryniecka
        email                : klaudia.kryniecka@gmail.com
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

__author__ = 'Klaudia Kryniecka'
__date__ = '2024-01-14'
__copyright__ = '(C) 2024 by Klaudia Kryniecka'


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load SandbarDetector class from file SandbarDetector.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .sandbar_detector import SandbarDetectorPlugin
    return SandbarDetectorPlugin()