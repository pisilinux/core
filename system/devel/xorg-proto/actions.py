#!/usr/bin/python
# -*- coding: utf-8 -*-

# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.system("sed -i 's|datadir|libdir|g' meson.build")
    
    shelltools.makedirs("build")
    shelltools.cd("build")
    shelltools.system("meson .. --prefix=/usr --libdir=lib -Dlegacy=true")
    
def build():
    shelltools.cd("build")
    shelltools.system("ninja")
    
def install():
    shelltools.cd("build")
    shelltools.system("DESTDIR=%s ninja install" % get.installDIR())
    
    shelltools.cd("..")
    pisitools.dodoc("README*", "COPYING*", "AUTHORS")
    
    pisitools.remove("/usr/include/X11/extensions/apple*")
    pisitools.remove("/usr/include/X11/extensions/windows*")
    pisitools.remove("/usr/share/doc/xorg-proto/COPYING-windowswmproto")
    pisitools.remove("/usr/share/doc/xorg-proto/COPYING-applewmproto")
    pisitools.remove("/usr/lib/pkgconfig/applewmproto.pc")
    pisitools.remove("/usr/lib/pkgconfig/windowswmproto.pc")
    
    #libX11
    pisitools.remove("/usr/include/X11/extensions/vldXvMC.h")
    pisitools.remove("/usr/include/X11/extensions/XKBgeom.h")
