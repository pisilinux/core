#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools


def setup():
    options = "-Dselinux=disabled \
               -Dman=true \
               -Dgtk_doc=false"


    if get.buildTYPE() == "_emul32":
        options += " --libdir=/usr/lib32 \
                     --bindir=/_emul32/bin \
                     --sbindir=/_emul32/sbin \
                     --prefix=/usr"
        shelltools.export("CC", "%s -m32" % get.CC())
        shelltools.export("CXX", "%s -m32" % get.CXX())
        shelltools.export("PKG_CONFIG_PATH", "/usr/lib32/pkgconfig")
    else :
        options += " --libdir=/usr/lib \
                     --bindir=/usr/bin \
                     --sbindir=/usr/sbin \
                     --datadir=/usr/share \
                     --prefix=/usr"

    #autotools.autoreconf("-vif")
    shelltools.makedirs("build")
    shelltools.cd("build")
    shelltools.system("meson .. %s" % options)

    #pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    #autotools.make("-j1")
    shelltools.cd("build")
    shelltools.system("ninja")

def install():
    shelltools.cd("build")
    #autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    shelltools.system("ninja install")

    if get.buildTYPE() == "_emul32":
        pisitools.domove("/_emul32/bin/gio-querymodules", "/usr/bin/32/")
        pisitools.removeDir("/_emul32")

    #pisitools.removeDir("/usr/share/gdb")
    
    if get.buildTYPE() != "_emul32":
        shelltools.cd("..")
        pisitools.dodoc("AUTHORS", "COPYING", "README*")
