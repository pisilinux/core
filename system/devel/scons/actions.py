#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools

def setup():
    # no install man pages into data dir.
    pisitools.dosed("setup.cfg", ",\ \*.1", "")
    pisitools.dosed("setup.cfg", "1$", deleteLine = True)

def build():
    pythonmodules.compile(pyVer = "3")

def install():
    pythonmodules.install("--install-scripts=/usr/bin --install-data=/usr/share", pyVer = "3")

    pisitools.doman("scons.1", "scons-time.1", "sconsign.1")
