#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt
import os
from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import mesontools
from pisi.actionsapi import get

def setup():
    shelltools.cd("build/meson")
    mesontools.configure("-Dlegacy_level=7 \
                          -Dzlib=enabled \
                          -Dlzma=enabled \
                          -Dbin_contrib=true \
                          -Dlz4=enabled")
    

def build():
    shelltools.cd("build/meson")
    mesontools.build()
    
def install():
    shelltools.cd("build/meson")
    mesontools.install()
