#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import get

def setup():
    shelltools.makedirs("build")
    shelltools.cd("build")
    options = "-DCMAKE_INSTALL_PREFIX=/usr \
               -DCMAKE_INSTALL_LIBDIR=lib \
               -DCMAKE_BUILD_TYPE=Release \
               -DBUILD_STATIC_LIBS=OFF"
               
    if get.buildTYPE() == "emul32":
        shelltools.export("CC", "gcc -m32")
        shelltools.export("CXX", "g++ -m32")        
        options = " -DCMAKE_INSTALL_LIBDIR=lib32 -DBUILD_STATIC_LIBS=OFF"
    
    cmaketools.configure(options, sourceDir=".." )

def build():
    shelltools.cd("build")
    cmaketools.make()

def install():
    shelltools.cd("build")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    
    shelltools.cd("..")
    pisitools.dodoc("COPYING", "README", "ChangeLog", "AUTHORS", "NEWS")
