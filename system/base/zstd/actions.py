#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt
import os
from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.makedirs("bld")
    shelltools.cd("bld")
    shelltools.system("meson setup \
		              ../build/meson \
		              --prefix=/usr \
					  -Dlegacy-level=7 \
		              -Dzlib=enabled \
		              -Dlzma=enabled \
		              -Dlz4=enabled \
					  ")

def build():
    shelltools.cd("bld")
    shelltools.system("ninja")

def install():
    shelltools.cd("bld")
    shelltools.system("DESTDIR=%s ninja install" % get.installDIR())
