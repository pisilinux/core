#!/usr/bin/python
# -*- coding: utf-8 -*-

# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import get

def setup():
    pisitools.flags.remove("-DNDEBUG")
    #shelltools.system("./autogen.sh")
    #autotools.configure("--prefix=/usr \
                         #--disable-static \
                         #--enable-shared")

    #pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")
    
    cmaketools.configure("-DBUILD_SHARED_LIBS=ON \
                          -DSNAPPY_BUILD_TESTS=OFF \
                          -DSNAPPY_BUILD_BENCHMARKS=OFF \
		                  -DCMAKE_INSTALL_LIBDIR=lib")
                          
                    

def build():
    cmaketools.make()

#def check():
    #cmaketools.make("test")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("README.md", "COPYING", "AUTHORS")
