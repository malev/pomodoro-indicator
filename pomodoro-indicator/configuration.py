#!/usr/bin/env python
#-*- coding:utf-8 -*-

#
# Copyright 2011 malev.com.ar
#
# Author: Marcos Vanetta <marcosvanetta@gmail.com>
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of either or both of the following licenses:
#
# 1) the GNU Lesser General Public License version 3, as published by the
# Free Software Foundation; and/or
# 2) the GNU Lesser General Public License version 2.1, as published by
# the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranties of
# MERCHANTABILITY, SATISFACTORY QUALITY or FITNESS FOR A PARTICULAR
# PURPOSE.  See the applicable version of the GNU Lesser General Public
# License for more details.
#
# You should have received a copy of both the GNU Lesser General Public
# License version 3 and version 2.1 along with this program.  If not, see
# <http://www.gnu.org/licenses/>

"""
Configuration file
"""

import os

def base_directory():
    """Returns the base directory"""
    return os.path.dirname(os.path.realpath(__file__)) + os.path.sep

def icon_directory():
    """Returns the location of the icons"""
    return os.path.dirname(os.path.realpath(__file__)) + os.path.sep + "../images" + os.path.sep

if __name__ == "__main__":
    print __doc__
