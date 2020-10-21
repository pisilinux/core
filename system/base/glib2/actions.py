#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

builddir = "build32" if get.buildTYPE() == 'emul32' else "build"

def setup():
    options = "-Dselinux=disabled \
               -Dman=true \
               -Dgtk_doc=false"


    if get.buildTYPE() == "_emul32":
        options += " --libdir=/_emul32/lib32 \
                     --bindir=/_emul32/bin \
                     --sbindir=/_emul32/sbin \
                     --prefix=/_emul32 \
                     -Dlibmount=disabled"
        shelltools.export("CC", "%s -m32" % get.CC())
        shelltools.export("CXX", "%s -m32" % get.CXX())
        shelltools.export("PKG_CONFIG_PATH", "/usr/lib32/pkgconfig")
        shelltools.system("patch -p1 < multilib.diff")
    else :
        options += " --libdir=/usr/lib \
                     --bindir=/usr/bin \
                     --sbindir=/usr/sbin \
                     --datadir=/usr/share \
                     --prefix=/usr"

    #autotools.autoreconf("-vif")
    shelltools.makedirs("%s" %builddir)
    shelltools.cd("%s" %builddir)
    shelltools.system("meson .. %s" % options)

    #pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    #autotools.make("-j1")
    shelltools.cd("%s" %builddir)
    shelltools.system("ninja")

def install():
    shelltools.cd("%s" %builddir)
    #autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    shelltools.system("DESTDIR=%s ninja install" % get.installDIR())

    if get.buildTYPE() == "_emul32":
        pisitools.domove("/_emul32/bin/gio-querymodules", "/usr/bin/32/")
        pisitools.domove("/_emul32/lib32", "/usr")
        pisitools.removeDir("/_emul32")
        for f in shelltools.ls("%s/usr/lib32/pkgconfig" % get.installDIR()):
            pisitools.dosed("%s/usr/lib32/pkgconfig/%s" % (get.installDIR(), f), "_emul32", "usr") 
        return

    
    if get.buildTYPE() != "_emul32":
        pisitools.removeDir("/usr/share/gdb")
        shelltools.cd("..")
        pisitools.dodoc("AUTHORS", "COPYING", "README*")
