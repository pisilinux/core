#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import mesontools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    options = "-Dselinux=disabled \
               -Dman=true \
               -Dgtk_doc=false"


    if get.buildTYPE() == "emul32":
        shelltools.export("CC", "%s -m32" % get.CC())
        shelltools.export("CXX", "%s -m32" % get.CXX())
        shelltools.export("PKG_CONFIG_PATH", "/usr/lib32/pkgconfig")
        options += " --libdir=/usr/lib32 \
                     --bindir=/usr/emul32 \
                     --sbindir=/usr/emul32 \
                     --mandir=/usr/emul32 \
                     --localedir=/usr/emul32/locale \
                     -Dsysprof=disabled \
                     -Dlibmount=disabled"
                     
        shelltools.system("patch -p1 < multilib.diff")
                     
    #else:
        #options += " -Dsysprof=enabled"
        
        
    mesontools.configure(options)


def build():
    mesontools.build()

def install():
    mesontools.install()

    if get.buildTYPE() == "emul32":
        pisitools.domove("/usr/emul32//gio-querymodules", "/usr/bin/32/")
        pisitools.removeDir("/usr/emul32")
        #pisitools.removeDir("/usr/_emul32")
        pisitools.removeDir("/usr/share/gdb")
        for f in shelltools.ls("%s/usr/lib32/pkgconfig" % get.installDIR()):
            #pisitools.dosed("%s/usr/lib32/pkgconfig/%s" % (get.installDIR(), f), "_emul32", "share")
            pisitools.dosed("%s/usr/lib32/pkgconfig/%s" % (get.installDIR(), f), "emul32", "bin")
        return

    
    pisitools.dodoc("COPYING", "README*")
